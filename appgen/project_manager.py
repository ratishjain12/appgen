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
    
    def show_post_generation_info(self, dir_name: str) -> None:
        """Show post-generation information and next steps"""
        project_path = Path(dir_name).resolve()
        
        console.print(f"\n[bold green]🎉 Project created successfully![/bold green]")
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
        
        # Ask if user wants to open in editor
        if Confirm.ask("\n📝 Open project in code editor?", default=True):
            self.open_project_in_editor(dir_name)
    
    def open_project_in_editor(self, dir_name: str) -> None:
        """Open project in user's preferred code editor"""
        project_path = Path(dir_name).resolve()
        
        # Common editors and their commands
        editors = {
            "code": "Visual Studio Code",
            "subl": "Sublime Text",
            "atom": "Atom",
            "vim": "Vim",
            "nano": "Nano"
        }
        
        console.print(f"\n[bold]📝 Choose your editor:[/bold]")
        editor_table = self.ui.create_table("Code Editors", [
            ("#", "dim"),
            ("Editor", "primary"),
            ("Command", "secondary")
        ])
        
        editor_choices = list(editors.items())
        for i, (cmd, name) in enumerate(editor_choices, 1):
            editor_table.add_row(str(i), name, cmd)
        
        console.print(editor_table)
        
        choice = self.ui.get_user_choice("Select editor", len(editors))
        editor_cmd, editor_name = editor_choices[choice - 1]
        
        self._open_with_editor(editor_cmd, project_path, editor_name)
    
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