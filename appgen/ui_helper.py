"""
UI Helper module for consistent user interface operations.
"""

from rich.console import Console
from rich.prompt import IntPrompt
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from rich.text import Text
from typing import List, Tuple

console = Console()


class UIHelper:
    """Helper class for UI-related operations"""
    
    def __init__(self, config_manager):
        self.config_manager = config_manager
        self.ui_config = config_manager.get_ui_config()
        self.colors = self.ui_config.get('colors', {})
    
    def create_table(self, title: str, columns: List[Tuple[str, str]]) -> Table:
        """Create a styled table with consistent formatting"""
        table = Table(title=title, show_header=True, header_style=f"bold {self.colors.get('primary', 'cyan')}")
        
        for col_name, style in columns:
            table.add_column(col_name, style=self.colors.get(style, 'white'))
        
        return table
    
    def show_panel(self, title: str, content: str, style: str = "primary") -> None:
        """Display a styled panel"""
        console.print(Panel.fit(
            f"[bold {self.colors.get(style, 'cyan')}]{title}[/bold {self.colors.get(style, 'cyan')}]\n{content}",
            border_style=self.colors.get(style, "cyan")
        ))
    
    def get_user_choice(self, prompt: str, max_choice: int, default: int = 1) -> int:
        """Get validated user choice from a numbered list"""
        while True:
            try:
                choice = IntPrompt.ask(prompt, default=default, show_default=True)
                if 1 <= choice <= max_choice:
                    return choice
                else:
                    console.print(f"[red]❌ Invalid choice. Please select 1-{max_choice}[/red]")
            except ValueError:
                console.print("[red]❌ Please enter a valid number[/red]")
    
    def show_welcome(self) -> None:
        """Display welcome message"""
        welcome_msg = self.ui_config.get('welcome_message', 'Welcome to AppGen!')
        subtitle = self.ui_config.get('welcome_subtitle', "Let's create your next project together.")
        
        welcome_text = Text()
        welcome_text.append(welcome_msg, style=f"bold {self.colors.get('success', 'green')}")
        welcome_text.append("\n")
        welcome_text.append(subtitle, style=self.colors.get('secondary', 'magenta'))
        
        console.print(Panel(
            Align.center(welcome_text),
            border_style=self.colors.get("success", "green"),
            padding=(1, 2)
        )) 