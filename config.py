#!/usr/bin/env python
"""
Configuration management for AppGen
"""
import json
from pathlib import Path
from typing import Dict, Any, Optional
from rich.console import Console

console = Console()

# Default configuration
DEFAULT_CONFIG = {
    "frameworks": {
        "interactive": {
            "nextjs": {
                "name": "Next.js",
                "description": "React framework for production",
                "routers": ["app", "pages"],
                "features": ["typescript", "tailwind"],
                "default_features": ["typescript", "tailwind"],
                "feature_descriptions": {
                    "typescript": "Add TypeScript support",
                    "tailwind": "Add Tailwind CSS for styling"
                }
            },
            "reactjs": {
                "name": "React",
                "description": "JavaScript library for building user interfaces",
                "features": ["typescript", "tailwind"],
                "default_features": ["typescript", "tailwind"],
                "feature_descriptions": {
                    "typescript": "Add TypeScript support",
                    "tailwind": "Add Tailwind CSS for styling"
                }
            }
        },
        "simple": {
            "express": {
                "name": "Express.js",
                "description": "Fast, unopinionated web framework for Node.js",
                "databases": ["none", "mongodb", "postgresql", "supabase"],
                "default_database": "none",
                "database_descriptions": {
                    "none": "No database (basic Express setup)",
                    "mongodb": "MongoDB with Mongoose ODM",
                    "postgresql": "PostgreSQL with Sequelize ORM",
                    "supabase": "Supabase (PostgreSQL with real-time features)"
                }
            },
            "flask": {
                "name": "Flask",
                "description": "Lightweight WSGI web application framework"
            }
        }
    },
    "ui": {
        "welcome_message": "Welcome to AppGen!",
        "welcome_subtitle": "Let's create your next project together.",
        "default_project_name": "my-project",
        "colors": {
            "primary": "cyan",
            "secondary": "magenta",
            "success": "green",
            "warning": "yellow",
            "error": "red"
        }
    },
    "templates": {
        "base_path": "templates",
        "auto_cleanup": True,
        "merge_package_json": True
    }
}

class ConfigManager:
    def __init__(self, config_path: Optional[Path] = None):
        self.config_path = config_path or self._get_default_config_path()
        self.config = self._load_config()
    
    def _get_default_config_path(self) -> Path:
        """Get the default config file path"""
        user_config = Path.home() / ".appgen" / "config.yaml"
        local_config = Path("appgen.config.yaml")
        if user_config.exists():
            return user_config
        elif local_config.exists():
            return local_config
        else:
            return user_config
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file or create default"""
        if self.config_path.exists():
            try:
                with self.config_path.open('r') as f:
                    if self.config_path.suffix == '.yaml':
                        import yaml
                        return yaml.safe_load(f)
                    elif self.config_path.suffix == '.json':
                        return json.load(f)
                    else:
                        console.print(f"[yellow]Unsupported config format: {self.config_path.suffix}[/yellow]")
                        return DEFAULT_CONFIG
            except Exception as e:
                console.print(f"[red]Error loading config: {e}[/red]")
                return DEFAULT_CONFIG
        else:
            self._create_default_config()
            return DEFAULT_CONFIG
    
    def _create_default_config(self):
        """Create default configuration file"""
        try:
            self.config_path.parent.mkdir(parents=True, exist_ok=True)
            with self.config_path.open('w') as f:
                if self.config_path.suffix == '.yaml':
                    import yaml
                    yaml.dump(DEFAULT_CONFIG, f, default_flow_style=False, indent=2)
                else:
                    json.dump(DEFAULT_CONFIG, f, indent=2)
            console.print(f"[green]Created default config at: {self.config_path}[/green]")
        except Exception as e:
            console.print(f"[red]Error creating config: {e}[/red]")
    
    def get_interactive_frameworks(self) -> Dict[str, Any]:
        return self.config.get("frameworks", {}).get("interactive", {})
    
    def get_simple_frameworks(self) -> Dict[str, Any]:
        return self.config.get("frameworks", {}).get("simple", {})
    
    def get_framework_config(self, framework: str) -> Optional[Dict[str, Any]]:
        interactive = self.get_interactive_frameworks()
        simple = self.get_simple_frameworks()
        if framework in interactive:
            return interactive[framework]
        elif framework in simple:
            return simple[framework]
        return None
    
    def get_ui_config(self) -> Dict[str, Any]:
        return self.config.get("ui", {})
    
    def get_template_config(self) -> Dict[str, Any]:
        return self.config.get("templates", {})
    
    def add_framework(self, framework_type: str, name: str, config: Dict[str, Any]):
        if framework_type not in ["interactive", "simple"]:
            raise ValueError("framework_type must be 'interactive' or 'simple'")
        self.config["frameworks"][framework_type][name] = config
        self._save_config()
    
    def remove_framework(self, framework_type: str, name: str):
        if framework_type not in ["interactive", "simple"]:
            raise ValueError("framework_type must be 'interactive' or 'simple'")
        if name in self.config["frameworks"][framework_type]:
            del self.config["frameworks"][framework_type][name]
            self._save_config()
    
    def add_feature(self, framework: str, feature: str, description: str):
        framework_config = self.get_framework_config(framework)
        if not framework_config:
            raise ValueError(f"Framework '{framework}' not found")
        if "features" not in framework_config:
            framework_config["features"] = []
        if feature not in framework_config["features"]:
            framework_config["features"].append(feature)
        if "feature_descriptions" not in framework_config:
            framework_config["feature_descriptions"] = {}
        framework_config["feature_descriptions"][feature] = description
        self._save_config()
    
    def _save_config(self):
        try:
            with self.config_path.open('w') as f:
                if self.config_path.suffix == '.yaml':
                    import yaml
                    yaml.dump(self.config, f, default_flow_style=False, indent=2)
                else:
                    json.dump(self.config, f, indent=2)
        except Exception as e:
            console.print(f"[red]Error saving config: {e}[/red]")

# Global config instance
config_manager = ConfigManager() 