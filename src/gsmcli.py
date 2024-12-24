from textual.app import App, ComposeResult, RenderResult
from textual.containers import ScrollableContainer, Horizontal, HorizontalScroll, Vertical
from textual.widgets import Header, Footer, Static, Digits, Label
from textual.widget import Widget
from datetime import datetime

from modules.misc import Greeter

class GsmCliApp(App):
    """A TUI app to manage the Galileo Compute Cluster System"""
    CSS_PATH = "./styles/default.tcss"
    BINDINGS = [("q", "quit_app", "Exit application now"),
                ("d", "toggle_dark", "Toggle dark mode"),
                ("l", "toggle_lockscreen", "Toggle lockscreen")
                ]
    
    locked = True

    def compose(self) -> ComposeResult:
        yield Header(id="header")
        yield Horizontal(Greeter(), id="mainbox")
        yield Footer(id="footer")

    def action_toggle_dark(self) -> None:
        """An action to toggle dark colours"""
        self.dark = not self.dark
    
    def action_toggle_lockscreen(self) -> None:
        """An action to toggle the lockscreen"""
        greeter = self.query(Greeter)
        greeter.set_class(self.locked, "hidden")
        self.locked = not self.locked

    def action_quit_app(self) -> None:
        """An action to exit the application altogether"""
        self.exit()

if __name__ == "__main__":
    app = GsmCliApp()
    app.run()