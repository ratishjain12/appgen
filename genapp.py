#!/usr/bin/env python
import typer
from rich.console import Console
from rich.prompt import Prompt, Confirm, IntPrompt
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.align import Align
from rich.text import Text
from pathlib import Path
from typing import Optional, List, Dict, Any
from generator.generate import generate_project
from config import config_manager

app = typer.Typer()
console = Console()

class EnhancedAppGenCLI:
    def __init__(self):
        self.config_manager = config_manager
        self.console = console
    
    def show_welcome(self):
        """Display enhanced welcome message"""
        ui_config = self.config_manager.get_ui_config()
        welcome_msg = ui_config.get('welcome_message', 'Welcome to AppGen!')
        subtitle = ui_config.get('welcome_subtitle', "Let's create your next project together.")
        
        # Create a more visually appealing welcome
        welcome_text = Text()
        welcome_text.append(welcome_msg, style=f"bold {ui_config.get('colors', {}).get('success', 'green')}")
        welcome_text.append("\n")
        welcome_text.append(subtitle, style=ui_config.get('colors', {}).get('secondary', 'magenta'))
        
        self.console.print(Panel(
            Align.center(welcome_text),
            border_style=ui_config.get("colors", {}).get("success", "green"),
            padding=(1, 2)
        ))
    
    def show_framework_selection(self) -> str:
        """Enhanced framework selection with better UX"""
        interactive_frameworks = self.config_manager.get_interactive_frameworks()
        simple_frameworks = self.config_manager.get_simple_frameworks()
        ui_config = self.config_manager.get_ui_config()
        
        # Create a more detailed table
        table = Table(title="🎯 Choose Your Framework", show_header=True, header_style=f"bold {ui_config.get('colors', {}).get('primary', 'cyan')}")
        table.add_column("#", style="dim", width=3)
        table.add_column("Framework", style=ui_config.get("colors", {}).get("primary", "cyan"), no_wrap=True)
        table.add_column("Description", style=ui_config.get("colors", {}).get("secondary", "magenta"))
        table.add_column("Type", style=ui_config.get("colors", {}).get("success", "green"))
        table.add_column("Features", style=ui_config.get("colors", {}).get("warning", "yellow"))
        
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
            table.add_row(
                str(counter),
                framework,
                info.get("description", ""),
                "⚡ Simple",
                "Basic setup"
            )
            all_frameworks[counter] = framework
            counter += 1
        
        self.console.print(table)
        
        # Enhanced selection with validation
        while True:
            try:
                choice = IntPrompt.ask(
                    "Choose framework number",
                    default=1,
                    show_default=True
                )
                
                if choice in all_frameworks:
                    selected_framework = all_frameworks[choice]
                    self.console.print(f"[green]✅ Selected: {selected_framework}[/green]")
                    return selected_framework
                else:
                    self.console.print(f"[red]❌ Invalid choice. Please select 1-{len(all_frameworks)}[/red]")
            except ValueError:
                self.console.print("[red]❌ Please enter a valid number[/red]")
    
    def show_nextjs_options(self) -> tuple[str, List[str]]:
        """Enhanced Next.js configuration"""
        framework_config = self.config_manager.get_framework_config("nextjs")
        ui_config = self.config_manager.get_ui_config()
        
        self.console.print(Panel.fit(
            f"[bold {ui_config.get('colors', {}).get('primary', 'cyan')}]⚡ Next.js Configuration[/bold {ui_config.get('colors', {}).get('primary', 'cyan')}]\n"
            "Let's configure your Next.js project!",
            border_style=ui_config.get("colors", {}).get("primary", "cyan")
        ))
        
        # Enhanced router selection
        router_table = Table(title="🛣️  Router Selection", show_header=True)
        router_table.add_column("#", style="dim", width=3)
        router_table.add_column("Router", style=ui_config.get("colors", {}).get("primary", "cyan"))
        router_table.add_column("Description", style=ui_config.get("colors", {}).get("secondary", "magenta"))
        router_table.add_column("Recommended", style=ui_config.get("colors", {}).get("success", "green"))
        
        routers = [
            ("app", "App Router (Next.js 13+)", "✅ New projects"),
            ("pages", "Pages Router (Traditional)", "✅ Existing codebases")
        ]
        
        for i, (router, desc, rec) in enumerate(routers, 1):
            router_table.add_row(str(i), router, desc, rec)
        
        self.console.print(router_table)
        
        while True:
            try:
                router_choice = IntPrompt.ask(
                    "Choose router type",
                    default=1,
                    show_default=True
                )
                if router_choice in [1, 2]:
                    router = routers[router_choice - 1][0]
                    break
                else:
                    self.console.print("[red]❌ Please select 1 or 2[/red]")
            except ValueError:
                self.console.print("[red]❌ Please enter a valid number[/red]")
        
        # Enhanced feature selection
        self.console.print("\n[bold]🎨 Available Features:[/bold]")
        features = framework_config.get("features", [])
        feature_descriptions = framework_config.get("feature_descriptions", {})
        default_features = framework_config.get("default_features", [])
        
        selected_features = []
        for i, feature in enumerate(features, 1):
            description = feature_descriptions.get(feature, feature)
            default = feature in default_features
            
            if Confirm.ask(f"{i}. Add {feature}? ({description})", default=default):
                selected_features.append(feature)
        
        return router, selected_features
    
    def show_reactjs_options(self) -> List[str]:
        """Enhanced React configuration"""
        framework_config = self.config_manager.get_framework_config("reactjs")
        ui_config = self.config_manager.get_ui_config()
        
        self.console.print(Panel.fit(
            f"[bold {ui_config.get('colors', {}).get('primary', 'cyan')}]⚛️  React Configuration[/bold {ui_config.get('colors', {}).get('primary', 'cyan')}]\n"
            "Let's configure your React project!",
            border_style=ui_config.get("colors", {}).get("primary", "cyan")
        ))
        
        # Enhanced feature selection
        self.console.print("\n[bold]🎨 Available Features:[/bold]")
        features = framework_config.get("features", [])
        feature_descriptions = framework_config.get("feature_descriptions", {})
        default_features = framework_config.get("default_features", [])
        
        selected_features = []
        for i, feature in enumerate(features, 1):
            description = feature_descriptions.get(feature, feature)
            default = feature in default_features
            
            if Confirm.ask(f"{i}. Add {feature}? ({description})", default=default):
                selected_features.append(feature)
        
        return selected_features
    
    def get_project_directory(self) -> str:
        """Enhanced project directory input with validation"""
        ui_config = self.config_manager.get_ui_config()
        default_name = ui_config.get("default_project_name", "my-project")
        
        self.console.print(f"\n[bold]📁 Project Directory[/bold]")
        
        while True:
            dir_name = Prompt.ask(
                "Enter project directory name",
                default=default_name
            )
            
            if not dir_name.strip():
                self.console.print("[red]❌ Directory name cannot be empty[/red]")
                continue
            
            dir_path = Path(dir_name)
            if dir_path.exists():
                self.console.print(f"[yellow]⚠️  Directory '{dir_name}' already exists[/yellow]")
                if Confirm.ask("Overwrite existing directory?", default=False):
                    return dir_name
                else:
                    continue
            else:
                return dir_name
    
    def show_configuration_summary(self, framework: str, features: List[str], dir_name: str) -> bool:
        """Enhanced configuration summary"""
        ui_config = self.config_manager.get_ui_config()
        
        summary_table = Table(title="📋 Project Configuration Summary", show_header=True)
        summary_table.add_column("Setting", style=ui_config.get("colors", {}).get("primary", "cyan"))
        summary_table.add_column("Value", style=ui_config.get("colors", {}).get("secondary", "magenta"))
        
        summary_table.add_row("Framework", framework)
        summary_table.add_row("Directory", dir_name)
        summary_table.add_row("Features", ", ".join(features) if features else "None")
        
        self.console.print(summary_table)
        
        return Confirm.ask("\n🚀 Proceed with project generation?", default=True)
    
    def generate_with_progress(self, framework: str, features: List[str], dir_name: str):
        """Generate project with enhanced progress indicator"""
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=self.console
        ) as progress:
            task = progress.add_task("Generating project...", total=None)
            
            try:
                generate_project(framework, features, dir_name)
                progress.update(task, description="✅ Project generated successfully!")
            except Exception as e:
                progress.update(task, description=f"❌ Generation failed: {str(e)}")
                raise
    
    def show_post_generation_info(self, dir_name: str):
        """Enhanced post-generation information"""
        ui_config = self.config_manager.get_ui_config()
        
        success_text = Text()
        success_text.append("🎉 Project created successfully!", style=f"bold {ui_config.get('colors', {}).get('success', 'green')}")
        success_text.append("\n\n")
        success_text.append("Next steps:\n", style="bold")
        success_text.append(f"1. cd {dir_name}\n", style="cyan")
        success_text.append("2. npm install (or yarn install)\n", style="cyan")
        success_text.append("3. npm run dev (or yarn dev)\n", style="cyan")
        success_text.append("\nHappy coding! 🚀", style="bold")
        
        self.console.print(Panel(
            Align.left(success_text),
            border_style=ui_config.get("colors", {}).get("success", "green"),
            padding=(1, 2)
        ))
        
        # Ask if user wants to open the project
        if Confirm.ask("Would you like to open the project in an editor?", default=False):
            self.open_project_in_editor(dir_name)
    
    def open_project_in_editor(self, dir_name: str):
        """Interactive editor selection"""
        import subprocess
        import platform
        import shutil
        
        # Get absolute path
        project_path = Path(dir_name).resolve()
        
        # Define available editors with their commands and descriptions
        editors = [
            ("cursor", "Cursor - AI-first code editor"),
            ("code", "Visual Studio Code"),
            ("subl", "Sublime Text"),
            ("atom", "Atom"),
            ("vim", "Vim"),
            ("nano", "Nano"),
            ("finder", "Finder (macOS) / Explorer (Windows) / File Manager (Linux)"),
            ("none", "Don't open anything")
        ]
        
        # Check which editors are available
        available_editors = []
        for editor_cmd, editor_desc in editors:
            if editor_cmd in ["finder", "none"]:
                available_editors.append({
                    'name': f"{editor_desc}",
                    'value': editor_cmd,
                    'disabled': False
                })
            elif shutil.which(editor_cmd):
                available_editors.append({
                    'name': f"{editor_desc}",
                    'value': editor_cmd,
                    'disabled': False
                })
            else:
                available_editors.append({
                    'name': f"{editor_desc} (not installed)",
                    'value': editor_cmd,
                    'disabled': True
                })
        
        # Show editor selection table
        table = Table(title="📝 Choose Your Editor", show_header=True)
        table.add_column("#", style="dim", width=3)
        table.add_column("Editor", style="cyan")
        table.add_column("Status", style="green")
        
        for i, editor in enumerate(available_editors, 1):
            status = "✅ Available" if not editor['disabled'] else "❌ Not installed"
            table.add_row(str(i), editor['name'], status)
        
        self.console.print(table)
        
        # Interactive selection
        while True:
            try:
                choice = IntPrompt.ask(
                    "Choose editor number",
                    default=1,
                    show_default=True
                )
                
                if choice in range(1, len(available_editors) + 1):
                    selected_editor = available_editors[choice - 1]
                    
                    if selected_editor['disabled']:
                        self.console.print(f"[red]❌ {selected_editor['name']} is not installed[/red]")
                        continue
                    
                    if selected_editor['value'] == "none":
                        self.console.print("[yellow]Project not opened in any editor.[/yellow]")
                        return
                    
                    # Open the project
                    self.open_with_editor(selected_editor['value'], project_path, selected_editor['name'])
                    break
                else:
                    self.console.print(f"[red]❌ Invalid choice. Please select 1-{len(available_editors)}[/red]")
            except ValueError:
                self.console.print("[red]❌ Please enter a valid number[/red]")
    
    def open_with_editor(self, editor_cmd: str, project_path: Path, editor_name: str):
        """Open project with the selected editor"""
        import subprocess
        import platform
        
        try:
            if editor_cmd == "finder":
                if platform.system() == "Darwin":  # macOS
                    subprocess.run(["open", str(project_path)])
                elif platform.system() == "Windows":
                    subprocess.run(["explorer", str(project_path)])
                else:  # Linux
                    subprocess.run(["xdg-open", str(project_path)])
                self.console.print(f"[green]✅ Project opened in {editor_name}![/green]")
            else:
                # Open with code editor
                subprocess.run([editor_cmd, str(project_path)], check=True)
                self.console.print(f"[green]✅ Project opened in {editor_name}![/green]")
                
        except subprocess.CalledProcessError as e:
            self.console.print(f"[red]❌ Failed to open with {editor_name}: {e}[/red]")
        except Exception as e:
            self.console.print(f"[yellow]⚠️  Could not open project: {e}[/yellow]")

# CLI instance
cli_instance = EnhancedAppGenCLI()

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
    
    Use --interactive for guided setup with enhanced UX.
    """
    
    # Determine if we should use interactive mode
    use_interactive = interactive or (framework is None and dir is None)
    
    if use_interactive:
        cli_instance.show_welcome()
        
        # Get framework choice
        framework = cli_instance.show_framework_selection()
        
        # Handle different framework types
        interactive_frameworks = config_manager.get_interactive_frameworks()
        
        if framework in interactive_frameworks:
            if framework == "nextjs":
                router, selected_features = cli_instance.show_nextjs_options()
                feature_list = [router] + selected_features
            elif framework == "reactjs":
                selected_features = cli_instance.show_reactjs_options()
                feature_list = selected_features
            else:
                feature_list = []
            
            # Get project directory
            dir_name = cli_instance.get_project_directory()
        else:
            # Simple framework
            console.print(f"[yellow]Note: {framework} uses simple mode[/yellow]")
            if not dir:
                dir_name = cli_instance.get_project_directory()
            else:
                dir_name = dir
            feature_list = [f.strip().lower() for f in features.split(",") if f.strip()]
        
        # Show configuration summary
        if not cli_instance.show_configuration_summary(framework, feature_list, dir_name):
            console.print("[yellow]Project generation cancelled.[/yellow]")
            raise typer.Exit()
        
        # Generate project with progress
        cli_instance.generate_with_progress(framework, feature_list, dir_name)
        
        # Show post-generation info
        cli_instance.show_post_generation_info(dir_name)
        
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
        
        # Generate project
        generate_project(framework, feature_list, dir)
        console.print(f"[green]✅ Project '{framework}' created successfully at {dir}![/green]")

@app.command()
def list_frameworks():
    """List all available frameworks and their features with enhanced display."""
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
        table.add_row(framework, info["description"], "⚡ Simple", "Basic setup")
    
    console.print(table)

@app.command()
def config():
    """Show current configuration with enhanced display."""
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
    """Generate a project using a predefined preset with enhanced UX."""
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
        
        while True:
            try:
                choice = IntPrompt.ask("Choose preset number", default=1)
                if choice in range(1, len(presets) + 1):
                    name = list(presets.keys())[choice - 1]
                    break
                else:
                    console.print(f"[red]❌ Please select 1-{len(presets)}[/red]")
            except ValueError:
                console.print("[red]❌ Please enter a valid number[/red]")
    
    if name not in presets:
        console.print(f"[red]❌ Unknown preset: {name}[/red]")
        console.print(f"Available presets: {', '.join(presets.keys())}")
        raise typer.Exit(1)
    
    preset_info = presets[name]
    
    if not dir:
        dir = Prompt.ask(
            f"Enter project directory name",
            default=f"my-{name}"
        )
    
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