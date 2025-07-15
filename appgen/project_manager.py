"""
Project Manager module for handling project creation and management.
"""

import subprocess
import sys
from pathlib import Path
from rich.prompt import Prompt, Confirm
from rich.progress import Progress, SpinnerColumn, TextColumn
from typing import List
from .ui_helper import UIHelper, console
from generator.generate import generate_project


class ProjectManager:
    """Handles project creation and management"""
    
    def __init__(self, config_manager):
        self.config_manager = config_manager
        self.ui = UIHelper(config_manager)
    
    def get_project_directory(self) -> str:
        """Get project directory name from user"""
        default_name = self.ui.ui_config.get("default_project_name", "my-project")
        console.print(f"\n[bold]📁 Project Directory[/bold]")
        
        while True:
            dir_name = Prompt.ask("Enter project directory name", default=default_name)
            
            if dir_name.strip():
                return dir_name.strip()
            else:
                console.print("[red]❌ Directory name cannot be empty[/red]")
    
    def show_configuration_summary(self, framework: str, features: List[str], dir_name: str) -> bool:
        """Show project configuration summary and get confirmation"""
        summary_table = self.ui.create_table("📋 Project Configuration Summary", [
            ("Setting", "primary"),
            ("Value", "secondary")
        ])
        
        summary_table.add_row("Framework", framework)
        summary_table.add_row("Directory", dir_name)
        summary_table.add_row("Features", ", ".join(features) if features else "None")
        
        console.print(summary_table)
        
        return Confirm.ask("🚀 Proceed with project generation?", default=True)
    
    def generate_with_progress(self, framework: str, features: List[str], dir_name: str) -> None:
        """Generate project with progress indicator"""
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("Generating project...", total=None)
            generate_project(framework, features, dir_name)
            progress.update(task, description="✅ Project generated successfully!")
    
    def show_post_generation_info(self, dir_name: str, framework: str = None) -> None:
        """Show post-generation information and next steps"""
        project_path = Path(dir_name).resolve()
        console.print(f"\n[bold green]🎉 Project created successfully![bold green]")
        console.print(f"[blue]📁 Location:[/blue] {project_path}")

        # Show next steps
        next_steps = [
            f"cd {dir_name}",
            "npm install",
            "npm run dev"
        ]
        console.print(f"\n[bold]🚀 Next Steps:[/bold]")
        for step in next_steps:
            console.print(f"  $ {step}")

        # Offer to install dependencies for JS/TS frameworks
        js_frameworks = ["nextjs", "reactjs", "express"]
        if framework and framework.lower() in js_frameworks:
            self.install_dependencies_interactive(project_path)

        # Ask if user wants to open in editor
        if Confirm.ask("\n📝 Open project in code editor?", default=True):
            self.open_project_in_editor(dir_name)

    def install_dependencies_interactive(self, project_path: Path) -> None:
        """Prompt for and install dependencies using chosen package manager"""
        from shutil import which
        package_managers = [
            ("npm", "npm install"),
            ("yarn", "yarn install"),
            ("pnpm", "pnpm install"),
            ("bun", "bun install")
        ]
        available = [(name, cmd) for name, cmd in package_managers if which(name)]
        if not available:
            console.print("[yellow]⚠️  No supported package managers (npm, yarn, pnpm, bun) found in PATH.[/yellow]")
            return
        if not Confirm.ask("\n📦 Would you like to install dependencies now?", default=True):
            return
        # Show menu of available managers
        console.print("\n[bold]Choose your package manager:[/bold]")
        for i, (name, _) in enumerate(available, 1):
            console.print(f"  {i}. {name}")
        while True:
            try:
                choice = int(Prompt.ask("Enter number", default="1"))
                if 1 <= choice <= len(available):
                    break
                else:
                    console.print(f"[red]Invalid choice. Please select 1-{len(available)}[/red]")
            except ValueError:
                console.print("[red]Please enter a valid number[/red]")
        name, cmd = available[choice - 1]
        console.print(f"[cyan]Running: {cmd} in {project_path}...[/cyan]")
        import subprocess
        try:
            subprocess.run(cmd.split(), cwd=project_path, check=True)
            console.print(f"[green]✅ Dependencies installed with {name}![/green]")
        except Exception as e:
            console.print(f"[red]❌ Failed to install dependencies with {name}: {e}[/red]")
    
    def open_project_in_editor(self, dir_name: str) -> None:
        """Open project in user's preferred code editor"""
        project_path = Path(dir_name).resolve()
        from shutil import which
        # Common editors and their commands
        editors = {
            "code": "Visual Studio Code",
            "subl": "Sublime Text",
            "atom": "Atom",
            "vim": "Vim",
            "nano": "Nano",
            "cursor": "Cursor"
        }
        console.print(f"\n[bold]📝 Choose your editor:[/bold]")
        editor_table = self.ui.create_table("Code Editors", [
            ("#", "dim"),
            ("Editor", "primary"),
            ("Command", "secondary"),
            ("Installed?", "success")
        ])
        editor_choices = list(editors.items())
        installed_status = [which(cmd) is not None for cmd, _ in editor_choices]
        for i, ((cmd, name), is_installed) in enumerate(zip(editor_choices, installed_status), 1):
            status = "✅" if is_installed else "❌"
            editor_table.add_row(str(i), name, cmd, status)
        console.print(editor_table)
        while True:
            choice = self.ui.get_user_choice("Select editor", len(editors))
            editor_cmd, editor_name = editor_choices[choice - 1]
            if which(editor_cmd):
                self._open_with_editor(editor_cmd, project_path, editor_name)
                break
            else:
                console.print(f"[red]❌ {editor_name} is not installed. Please select another editor.[/red]")
    
    def _open_with_editor(self, editor_cmd: str, project_path: Path, editor_name: str) -> None:
        """Open project with specified editor"""
        try:
            if sys.platform == "darwin":  # macOS
                subprocess.run(["open", "-a", editor_name, str(project_path)])
            elif sys.platform == "win32":  # Windows
                subprocess.run(["start", editor_cmd, str(project_path)], shell=True)
            else:  # Linux
                subprocess.run(["xdg-open", str(project_path)])
            
            console.print(f"[green]✅ Project opened in {editor_name}![/green]")
        except subprocess.CalledProcessError as e:
            console.print(f"[red]❌ Failed to open with {editor_name}: {e}[/red]")
        except Exception as e:
            console.print(f"[yellow]⚠️  Could not open project: {e}[/yellow]") 