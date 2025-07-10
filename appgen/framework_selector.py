"""
Framework Selector module for handling framework selection and configuration.
"""

from rich.prompt import Confirm
from typing import List
from .ui_helper import UIHelper, console


class FrameworkSelector:
    """Handles framework selection and configuration"""
    
    def __init__(self, config_manager):
        self.config_manager = config_manager
        self.ui = UIHelper(config_manager)
    
    def show_framework_selection(self) -> str:
        """Display framework selection table and get user choice"""
        interactive_frameworks = self.config_manager.get_interactive_frameworks()
        simple_frameworks = self.config_manager.get_simple_frameworks()
        
        # Create framework selection table
        columns = [
            ("#", "dim"),
            ("Framework", "primary"),
            ("Description", "secondary"),
            ("Type", "success"),
            ("Features", "warning")
        ]
        table = self.ui.create_table("🎯 Choose Your Framework", columns)
        
        all_frameworks = {}
        counter = 1
        
        # Add interactive frameworks
        for framework, info in interactive_frameworks.items():
            features = ", ".join(info.get("features", []))
            table.add_row(
                str(counter),
                framework,
                info.get("description", ""),
                "🔄 Interactive",
                features
            )
            all_frameworks[counter] = framework
            counter += 1
        
        # Add simple frameworks
        for framework, info in simple_frameworks.items():
            databases = info.get("databases", [])
            db_info = f"DB: {', '.join(databases)}" if databases else "Basic setup"
            
            table.add_row(
                str(counter),
                framework,
                info.get("description", ""),
                "⚡ Simple",
                db_info
            )
            all_frameworks[counter] = framework
            counter += 1
        
        console.print(table)
        
        # Get user choice
        choice = self.ui.get_user_choice("Choose framework number", len(all_frameworks))
        selected_framework = all_frameworks[choice]
        console.print(f"[green]✅ Selected: {selected_framework}[/green]")
        
        return selected_framework
    
    def get_framework_options(self, framework: str) -> List[str]:
        """Get framework-specific options based on framework type"""
        if framework == "nextjs":
            return self._get_nextjs_options()
        elif framework == "reactjs":
            return self._get_reactjs_options()
        elif framework == "express":
            return self._get_express_options()
        else:
            return []
    
    def _get_nextjs_options(self) -> List[str]:
        """Get Next.js specific options (router + features)"""
        self.ui.show_panel("⚡ Next.js Configuration", "Let's configure your Next.js project!")
        
        # Router selection
        router_table = self.ui.create_table("🛣️  Router Selection", [
            ("#", "dim"),
            ("Router", "primary"),
            ("Description", "secondary"),
            ("Recommended", "success")
        ])
        
        routers = [
            ("app", "App Router (Next.js 13+)", "✅ New projects"),
            ("pages", "Pages Router (Traditional)", "✅ Existing codebases")
        ]
        
        for i, (router, desc, rec) in enumerate(routers, 1):
            router_table.add_row(str(i), router, desc, rec)
        
        console.print(router_table)
        router_choice = self.ui.get_user_choice("Choose router type", 2)
        router = routers[router_choice - 1][0]
        
        # Feature selection
        features = self._get_feature_selection("nextjs")
        return [router] + features
    
    def _get_reactjs_options(self) -> List[str]:
        """Get React.js specific options"""
        self.ui.show_panel("⚛️  React Configuration", "Let's configure your React project!")
        return self._get_feature_selection("reactjs")
    
    def _get_express_options(self) -> List[str]:
        """Get Express.js specific options (database selection)"""
        self.ui.show_panel("🚀 Express Configuration", "Let's configure your Express project!")
        
        framework_config = self.config_manager.get_framework_config("express")
        databases = framework_config.get("databases", [])
        database_descriptions = framework_config.get("database_descriptions", {})
        default_database = framework_config.get("default_database", "none")
        
        if not databases:
            return []
        
        # Database selection table
        db_table = self.ui.create_table("📊 Choose Your Database", [
            ("#", "dim"),
            ("Database", "primary"),
            ("Description", "secondary")
        ])
        
        for i, db in enumerate(databases, 1):
            description = database_descriptions.get(db, db)
            db_table.add_row(str(i), db, description)
        
        console.print(db_table)
        
        default_choice = databases.index(default_database) + 1 if default_database in databases else 1
        db_choice = self.ui.get_user_choice("Choose database number", len(databases), default_choice)
        selected_db = databases[db_choice - 1]
        
        console.print(f"[green]✅ Selected database: {selected_db}[/green]")
        return [selected_db] if selected_db != "none" else []
    
    def _get_feature_selection(self, framework: str) -> List[str]:
        """Generic feature selection for frameworks"""
        framework_config = self.config_manager.get_framework_config(framework)
        features = framework_config.get("features", [])
        feature_descriptions = framework_config.get("feature_descriptions", {})
        default_features = framework_config.get("default_features", [])
        
        console.print("\n[bold]🎨 Available Features:[/bold]")
        
        selected_features = []
        for i, feature in enumerate(features, 1):
            description = feature_descriptions.get(feature, feature)
            default = feature in default_features
            
            if Confirm.ask(f"{i}. Add {feature}? ({description})", default=default):
                selected_features.append(feature)
        
        return selected_features 