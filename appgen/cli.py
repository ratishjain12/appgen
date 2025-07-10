"""
Main CLI module that orchestrates the entire application.
"""

import typer
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from typing import Optional, List
from .ui_helper import UIHelper, console
from .framework_selector import FrameworkSelector
from .project_manager import ProjectManager
from config import config_manager
from generator.generate import generate_project

# Initialize Typer app
app = typer.Typer()


class AppGenCLI:
    """Main CLI application class with clean organization"""
    
    def __init__(self):
        self.config_manager = config_manager
        self.framework_selector = FrameworkSelector(config_manager)
        self.project_manager = ProjectManager(config_manager)
        self.ui = UIHelper(config_manager)
    
    def show_welcome(self) -> None:
        """Display welcome message"""
        self.ui.show_welcome()
    
    def run_interactive_mode(self) -> None:
        """Run the interactive project creation flow"""
        self.show_welcome()
        
        # Get framework choice
        framework = self.framework_selector.show_framework_selection()
        
        # Get framework-specific options
        interactive_frameworks = self.config_manager.get_interactive_frameworks()
        if framework in interactive_frameworks:
            features = self.framework_selector.get_framework_options(framework)
        else:
            console.print(f"[yellow]Note: {framework} uses simple mode[/yellow]")
            features = self.framework_selector.get_framework_options(framework)
        
        # Get project directory
        dir_name = self.project_manager.get_project_directory()
        
        # Show configuration summary
        if not self.project_manager.show_configuration_summary(framework, features, dir_name):
            console.print("[yellow]Project generation cancelled.[/yellow]")
            raise typer.Exit()
        
        # Generate project
        self.project_manager.generate_with_progress(framework, features, dir_name)
        
        # Show post-generation info
        self.project_manager.show_post_generation_info(dir_name)


# Initialize CLI instance
cli_instance = AppGenCLI()


@app.command()
def create(
    framework: Optional[str] = typer.Option(None, help="Framework to use"),
    features: str = typer.Option("", help="Comma-separated features"),
    dir: Optional[str] = typer.Option(None, help="Target directory"),
    router: str = typer.Option("pages", help="Router type for Next.js"),
    db: str = typer.Option("", "--db", help="Database type for Express (mongodb, postgresql, supabase, serverless)"),
    interactive: bool = typer.Option(False, "--interactive", "-i", help="Use interactive mode")
):
    """Create a new project with the specified framework and features."""
    
    # Determine if we should use interactive mode
    use_interactive = interactive or (framework is None and dir is None)
    
    if use_interactive:
        cli_instance.run_interactive_mode()
    else:
        # Command-line mode
        if not framework:
            typer.echo("[red]Framework is required in non-interactive mode[/red]")
            raise typer.Exit(1)
        
        if not dir:
            typer.echo("[red]Directory is required in non-interactive mode[/red]")
            raise typer.Exit(1)
        
        feature_list = [f.strip().lower() for f in features.split(",") if f.strip()]
        
        # Handle framework-specific logic
        if framework.lower() == "nextjs":
            framework_config = config_manager.get_framework_config("nextjs")
            valid_routers = framework_config.get("routers", ["app", "pages"])
            if router not in valid_routers:
                typer.echo(f"[red]Please specify --router {' or '.join(valid_routers)} for Next.js.[/red]")
                raise typer.Exit(1)
            feature_list = [router] + feature_list
        elif framework.lower() == "express" and db:
            valid_databases = ["mongodb", "postgresql", "supabase", "serverless"]
            if db.lower() not in valid_databases:
                typer.echo(f"[red]Invalid database '{db}'. Valid options: {', '.join(valid_databases)}[/red]")
                raise typer.Exit(1)
            feature_list = [db.lower()]
        
        # Generate project
        generate_project(framework, feature_list, dir)
        console.print(f"[green]✅ Project '{framework}' created successfully at {dir}![/green]")


@app.command()
def list_frameworks():
    """List all available frameworks and their features."""
    interactive_frameworks = config_manager.get_interactive_frameworks()
    simple_frameworks = config_manager.get_simple_frameworks()
    ui_config = config_manager.get_ui_config()
    
    table = Table(title="📚 Available Frameworks", show_header=True)
    table.add_column("Framework", style=ui_config.get("colors", {}).get("primary", "cyan"), no_wrap=True)
    table.add_column("Description", style=ui_config.get("colors", {}).get("secondary", "magenta"))
    table.add_column("Type", style=ui_config.get("colors", {}).get("success", "green"))
    table.add_column("Features", style=ui_config.get("colors", {}).get("warning", "yellow"))
    
    for framework, info in interactive_frameworks.items():
        features = ", ".join(info.get("features", []))
        table.add_row(framework, info["description"], "🔄 Interactive", features)
    
    for framework, info in simple_frameworks.items():
        databases = info.get("databases", [])
        db_info = f"DB: {', '.join(databases)}" if databases else "Basic setup"
        table.add_row(framework, info["description"], "⚡ Simple", db_info)
    
    console.print(table)


@app.command()
def config():
    """Show current configuration."""
    ui_config = config_manager.get_ui_config()
    
    table = Table(title="⚙️  Current Configuration", show_header=True)
    table.add_column("Setting", style=ui_config.get("colors", {}).get("primary", "cyan"))
    table.add_column("Value", style=ui_config.get("colors", {}).get("secondary", "magenta"))
    
    table.add_row("Config Path", str(config_manager.config_path))
    table.add_row("Default Project Name", ui_config.get("default_project_name", "my-project"))
    table.add_row("Welcome Message", ui_config.get("welcome_message", "Welcome to AppGen!"))
    
    console.print(table)


@app.command()
def preset(
    name: Optional[str] = typer.Argument(None, help="Name of the preset (e.g., mern)"),
    dir: Optional[str] = typer.Option(None, help="Base directory to generate the project in")
):
    """Generate a project using a predefined preset."""
    presets = {
        "mern": {
            "description": "MongoDB + Express + React + Node.js",
            "framework": "express",
            "features": ["mongodb"]
        },
        "nextjs-fullstack": {
            "description": "Next.js with Prisma and TypeScript",
            "framework": "nextjs",
            "features": ["app", "typescript", "prisma"]
        }
    }
    
    if not name:
        # Interactive preset selection
        console.print("[bold]🎯 Available Presets:[/bold]")
        for i, (preset_name, preset_info) in enumerate(presets.items(), 1):
            console.print(f"{i}. {preset_name} - {preset_info['description']}")
        
        choice = cli_instance.ui.get_user_choice("Choose preset number", len(presets))
        name = list(presets.keys())[choice - 1]
    
    if name not in presets:
        console.print(f"[red]❌ Unknown preset: {name}[/red]")
        console.print(f"Available presets: {', '.join(presets.keys())}")
        raise typer.Exit(1)
    
    preset_info = presets[name]
    
    if not dir:
        dir = Prompt.ask(f"Enter project directory name", default=f"my-{name}")
    
    console.print(f"[cyan]🚀 Generating {name} preset...[/cyan]")
    generate_project(preset_info["framework"], preset_info["features"], dir)
    console.print(f"[green]✅ {name} project created successfully at {dir}![/green]")


@app.callback(invoke_without_command=True)
def main_callback(
    ctx: typer.Context,
    interactive: bool = typer.Option(False, "--interactive", "-i", help="Use interactive mode (shortcut for 'create --interactive')")
):
    """AppGen - Modern Project Generator for Web Development"""
    if interactive and ctx.invoked_subcommand is None:
        # Call the create command with interactive mode
        ctx.invoke(create, interactive=True)
        raise typer.Exit()


if __name__ == "__main__":
    app() 