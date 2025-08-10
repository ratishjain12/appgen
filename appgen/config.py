#!/usr/bin/env python
"""
Configuration management for AppGen
"""
import json
from pathlib import Path
from typing import Dict, Any, Optional
from rich.console import Console

console = Console()

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
            },
            "astrojs": {
                "name": "Astro",
                "description": "Static site generator for modern web projects",
              
            },

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
            },
            "django": {
                "name": "Django",
                "description": "The web framework for perfectionists with deadlines"
            },
            "svelte": {
                "name": "Svelte",
                "description": "Cybernetically enhanced web apps"
            },
            "serverless": {
                "name": "Serverless",
                "description": "Serverless application template (AWS Lambda, etc.)",
                "languages": ["javascript", "typescript", "python", "go"],
                "default_language": "javascript",
                "language_descriptions": {
                    "javascript": "Node.js (JavaScript) runtime for AWS Lambda, etc.",
                    "typescript": "TypeScript runtime for AWS Lambda, etc.",
                    "python": "Python 3.x runtime for AWS Lambda, etc.",
                    "go": "Go 1.x runtime for AWS Lambda, etc."
                }
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
        # Get config file path from package directory
        self.config_path = config_path or self._get_package_config_path()
        # Don't cache config - always load fresh
        self._config = None
    
    def _get_package_config_path(self) -> Path:
        """Get the config file path from the package directory"""
        # Since config.py is now in the appgen package, 
        # the YAML file will be in the same directory
        current_dir = Path(__file__).parent
        package_config = current_dir / "appgen.config.yaml"
        console.print(f"[blue]Looking for config in package: {package_config}[/blue]")
        return package_config
    
    def _get_default_config_path(self) -> Path:
        """Get the default config file path - package directory only"""
        return self._get_package_config_path()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from YAML file - NO CACHING, always fresh load"""
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
            console.print(f"[yellow]Config file not found: {self.config_path}[/yellow]")
            console.print("[yellow]Using default configuration[/yellow]")
            return DEFAULT_CONFIG
    
    @property
    def config(self) -> Dict[str, Any]:
        """Always load fresh config - no caching"""
        return self._load_config()
    
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
        """Get interactive frameworks - always fresh load"""
        return self.config.get("frameworks", {}).get("interactive", {})
    
    def get_simple_frameworks(self) -> Dict[str, Any]:
        """Get simple frameworks - always fresh load"""
        return self.config.get("frameworks", {}).get("simple", {})
    
    def get_framework_config(self, framework: str) -> Optional[Dict[str, Any]]:
        """Get framework config - always fresh load"""
        interactive = self.get_interactive_frameworks()
        simple = self.get_simple_frameworks()
        if framework in interactive:
            return interactive[framework]
        elif framework in simple:
            return simple[framework]
        return None
    
    def get_ui_config(self) -> Dict[str, Any]:
        """Get UI config - always fresh load"""
        return self.config.get("ui", {})
    
    def get_template_config(self) -> Dict[str, Any]:
        """Get template config - always fresh load"""
        return self.config.get("templates", {})
    
    def add_framework(self, framework_type: str, name: str, config: Dict[str, Any]):
        """Add framework - NO PERSISTENCE (read-only from YAML)"""
        console.print("[yellow]Warning: Cannot modify configuration - using read-only YAML config[/yellow]")
        raise NotImplementedError("Configuration is read-only from YAML file")
    
    def remove_framework(self, framework_type: str, name: str):
        """Remove framework - NO PERSISTENCE (read-only from YAML)"""
        console.print("[yellow]Warning: Cannot modify configuration - using read-only YAML config[/yellow]")
        raise NotImplementedError("Configuration is read-only from YAML file")
    
    def add_feature(self, framework: str, feature: str, description: str):
        """Add feature - NO PERSISTENCE (read-only from YAML)"""
        console.print("[yellow]Warning: Cannot modify configuration - using read-only YAML config[/yellow]")
        raise NotImplementedError("Configuration is read-only from YAML file")
    
    def get_presets(self) -> Dict[str, Any]:
        """Get presets - always fresh load"""
        return self.config.get("presets", {})
    
    def _save_config(self):
        """Save configuration - DISABLED (read-only from YAML)"""
        console.print("[yellow]Warning: Cannot save configuration - using read-only YAML config[/yellow]")
        pass

# Global config instance
config_manager = ConfigManager() 