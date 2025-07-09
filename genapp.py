#!/usr/bin/env python
import typer
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich.table import Table
from typing import Optional, List
from generator.generate import generate_project
from config import config_manager

app = typer.Typer()
console = Console()

def show_framework_selection() -> str:
    """Show interactive framework selection"""
    interactive_frameworks = config_manager.get_interactive_frameworks()
    simple_frameworks = config_manager.get_simple_frameworks()
    ui_config = config_manager.get_ui_config()
    
    table = Table(title="Available Frameworks")
    table.add_column("Framework", style=ui_config.get("colors", {}).get("primary", "cyan"), no_wrap=True)
    table.add_column("Description", style=ui_config.get("colors", {}).get("secondary", "magenta"))
    table.add_column("Interactive", style=ui_config.get("colors", {}).get("success", "green"))
    
    for framework, info in interactive_frameworks.items():
        table.add_row(framework, info["description"], "✅ Yes")
    
    for framework, info in simple_frameworks.items():
        table.add_row(framework, info["description"], "❌ No")
    
    console.print(table)
    
    while True:
        framework = Prompt.ask(
            "Choose a framework",
            choices=list(interactive_frameworks.keys()) + list(simple_frameworks.keys()),
            default="nextjs"
        )
        
        if framework in interactive_frameworks:
            return framework
        else:
            # For simple frameworks, we'll use command-line mode
            console.print(f"[yellow]Note: {framework} uses simple command-line mode. Use --help for options.[/yellow]")
            return framework

def show_nextjs_options() -> tuple[str, List[str]]:
    """Show interactive Next.js configuration"""
    framework_config = config_manager.get_framework_config("nextjs")
    ui_config = config_manager.get_ui_config()
    
    console.print(Panel.fit(
        f"[bold {ui_config.get('colors', {}).get('primary', 'cyan')}]Next.js Configuration[/bold {ui_config.get('colors', {}).get('primary', 'cyan')}]\n"
        "Let's configure your Next.js project!",
        border_style=ui_config.get("colors", {}).get("primary", "cyan")
    ))
    
    # Router selection
    router_table = Table(title="Router Options")
    router_table.add_column("Router", style=ui_config.get("colors", {}).get("primary", "cyan"))
    router_table.add_column("Description", style=ui_config.get("colors", {}).get("secondary", "magenta"))
    router_table.add_column("Recommended", style=ui_config.get("colors", {}).get("success", "green"))
    
    router_table.add_row("app", "App Router (Next.js 13+)", "✅ New projects")
    router_table.add_row("pages", "Pages Router (Traditional)", "✅ Existing codebases")
    
    console.print(router_table)
    
    router = Prompt.ask(
        "Choose router type",
        choices=framework_config.get("routers", ["app", "pages"]),
        default="app"
    )
    
    # Feature selection
    console.print("\n[bold]Available Features:[/bold]")
    features = framework_config.get("features", [])
    feature_descriptions = framework_config.get("feature_descriptions", {})
    
    selected_features = []
    for feature in features:
        description = feature_descriptions.get(feature, feature)
        
        if Confirm.ask(f"Add {feature}? ({description})", default=True):
            selected_features.append(feature)
    
    return router, selected_features

def show_reactjs_options() -> List[str]:
    """Show interactive React configuration"""
    framework_config = config_manager.get_framework_config("reactjs")
    ui_config = config_manager.get_ui_config()
    
    console.print(Panel.fit(
        f'''[bold {ui_config.get('colors', {}).get('primary', 'cyan')}]React Configuration[/bold {ui_config.get('colors', {}).get('primary', 'cyan')}]
Let's configure your React project!''',
        border_style=ui_config.get("colors", {}).get("primary", "cyan")
    ))
    
    # Feature selection
    console.print("\n[bold]Available Features:[/bold]")
    features = framework_config.get("features", [])
    feature_descriptions = framework_config.get("feature_descriptions", {})
    
    selected_features = []
    for feature in features:
        description = feature_descriptions.get(feature, feature)
        
        if Confirm.ask(f"Add {feature}? ({description})", default=True):
            selected_features.append(feature)
    
    return selected_features

def get_project_directory() -> str:
    """Get project directory with validation"""
    ui_config = config_manager.get_ui_config()
    default_name = ui_config.get("default_project_name", "my-project")
    
    while True:
        dir_name = Prompt.ask(
            "Enter project directory name",
            default=default_name
        )
        
        if Confirm.ask(f"Create project in './{dir_name}'?"):
            return dir_name

@app.command()
def create(
    framework: Optional[str] = typer.Option(None, help="Framework to use"),
    features: str = typer.Option("", help="Comma-separated features"),
    dir: Optional[str] = typer.Option(None, help="Target directory"),
    router: str = typer.Option("pages", help="Router type for Next.js"),
    interactive: bool = typer.Option(False, "--interactive", "-i", help="Use interactive mode")
):
    """
    Create a new project with the specified framework and features.
    
    Use --interactive for guided setup with Next.js and React projects.
    """
    
    # Determine if we should use interactive mode
    use_interactive = interactive or (framework is None and dir is None)
    
    if use_interactive:
        ui_config = config_manager.get_ui_config()
        console.print(Panel.fit(
            f'''[bold {ui_config.get('colors', {}).get('success', 'green')}]{ui_config.get('welcome_message', 'Welcome to AppGen!')}[/bold {ui_config.get('colors', {}).get('success', 'green')}]
{ui_config.get('welcome_subtitle', "Let's create your next project together.")}''',
            border_style=ui_config.get("colors", {}).get("success", "green")
        ))
        
        # Interactive framework selection
        framework = show_framework_selection()
        
        # Handle interactive frameworks
        interactive_frameworks = config_manager.get_interactive_frameworks()
        if framework in interactive_frameworks:
            if framework == "nextjs":
                router, selected_features = show_nextjs_options()
                feature_list = [router] + selected_features
            elif framework == "reactjs":
                selected_features = show_reactjs_options()
                feature_list = selected_features
            else:
                feature_list = []
            
            # Get project directory
            dir = get_project_directory()
            
        else:
            # Simple framework - fall back to command line
            console.print(f"[yellow]Using simple mode for {framework}[/yellow]")
            if not dir:
                ui_config = config_manager.get_ui_config()
                default_name = ui_config.get("default_project_name", "my-project")
                dir = Prompt.ask("Enter project directory name", default=f"my-{framework}")
            feature_list = [f.strip().lower() for f in features.split(",") if f.strip()]
    
    else:
        # Command-line mode
        if not framework:
            typer.echo("[red]Framework is required in non-interactive mode[/red]")
            raise typer.Exit(1)
        
        if not dir:
            typer.echo("[red]Directory is required in non-interactive mode[/red]")
            raise typer.Exit(1)
        
        feature_list = [f.strip().lower() for f in features.split(",") if f.strip()]
        
        if framework.lower() == "nextjs":
            framework_config = config_manager.get_framework_config("nextjs")
            valid_routers = framework_config.get("routers", ["app", "pages"])
            if router not in valid_routers:
                typer.echo(f"[red]Please specify --router {' or '.join(valid_routers)} for Next.js.[/red]")
                raise typer.Exit(1)
            feature_list = [router] + feature_list
    
    # Show final configuration
    if use_interactive:
        console.print("\n[bold]Final Configuration:[/bold]")
        console.print(f"Framework: [cyan]{framework}[/cyan]")
        console.print(f"Directory: [cyan]{dir}[/cyan]")
        console.print(f"Features: [cyan]{feature_list if feature_list else 'None'}[/cyan]")
        
        if not Confirm.ask("\nProceed with project creation?"):
            console.print("[yellow]Project creation cancelled.[/yellow]")
            raise typer.Exit()
    
    # Generate the project
    generate_project(framework.lower(), feature_list, dir)

@app.command()
def list_frameworks():
    """List all available frameworks and their features"""
    interactive_frameworks = config_manager.get_interactive_frameworks()
    simple_frameworks = config_manager.get_simple_frameworks()
    ui_config = config_manager.get_ui_config()
    
    console.print(Panel.fit(
        "[bold green]Available Frameworks[/bold green]",
        border_style="green"
    ))
    
    # Interactive frameworks
    console.print("\n[bold cyan]Interactive Frameworks:[/bold cyan]")
    for framework, info in interactive_frameworks.items():
        console.print(f"  [cyan]{framework}[/cyan] - {info['description']}")
        if 'features' in info:
            console.print(f"    Features: {', '.join(info['features'])}")
    
    # Simple frameworks
    console.print("\n[bold yellow]Simple Frameworks:[/bold yellow]")
    for framework, info in simple_frameworks.items():
        console.print(f"  [yellow]{framework}[/yellow] - {info['description']}")

@app.command()
def config():
    """Show current configuration"""
    console.print(Panel.fit(
        "[bold green]AppGen Configuration[/bold green]",
        border_style="green"
    ))
    
    console.print(f"Config file: {config_manager.config_path}")
    console.print(f"Config exists: {config_manager.config_path.exists()}")
    
    if config_manager.config_path.exists():
        console.print("\n[bold]Current Configuration:[/bold]")
        import json
        console.print(json.dumps(config_manager.config, indent=2))

@app.command()
def preset(
    name: Optional[str] = typer.Argument(None, help="Name of the preset (e.g., mern)"),
    dir: Optional[str] = typer.Option(None, help="Base directory to generate the project in")
):
    """
    Generate a fullstack project using a preset (e.g., MERN).
    """
    presets = config_manager.config.get("presets", {})
    if not name or name not in presets:
        if not presets:
            console.print("[red]No presets defined in config.[/red]")
            raise typer.Exit(1)
        console.print("[bold green]Available Presets:[/bold green]")
        for key, val in presets.items():
            console.print(f"  [cyan]{key}[/cyan]: {val.get('name', key)} - {val.get('description', '')}")
        if not name:
            raise typer.Exit()
        else:
            console.print(f"[red]Preset '{name}' not found.[/red]")
            raise typer.Exit(1)
    preset = presets[name]
    base_dir = dir or Prompt.ask("Enter base directory for the project", default=f"{name}-fullstack")
    frontend = preset.get("frontend")
    backend = preset.get("backend")
    if not frontend or not backend:
        console.print(f"[red]Preset '{name}' is missing frontend or backend definition.[/red]")
        raise typer.Exit(1)
    # Generate frontend
    frontend_dir = f"{base_dir}/{frontend['directory']}"
    console.print(f"[bold green]Generating frontend:[/bold green] {frontend['framework']} in {frontend_dir}")
    generate_project(frontend["framework"], frontend.get("features", []), frontend_dir)
    # Generate backend
    backend_dir = f"{base_dir}/{backend['directory']}"
    console.print(f"[bold green]Generating backend:[/bold green] {backend['framework']} in {backend_dir}")
    generate_project(backend["framework"], backend.get("features", []), backend_dir)
    console.print(f"[bold green]🎉 Fullstack preset '{name}' created at {base_dir}![/bold green]")

if __name__ == "__main__":
    app()