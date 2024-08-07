from textual.app import RenderResult, ComposeResult
from textual.widgets import Digits, Static, Label
from datetime import datetime

class Greeter(Static):
    """A widget for greeting"""

    def compose(self) -> ComposeResult:
        yield Static("GALILEO COMPUTE SYSTEM\n", classes="clocklabel")
        yield Digits("", id="clock")
        yield Static("\nGALILEO SYSTEM WELCOMES YOU ^_^ PRESS L TO UNLOCK", classes="clocklabel")

    def on_mount(self) -> None:
        self.update_clock()
        self.set_interval(1, self.update_clock)

    def update_clock(self) -> None:
        clock = datetime.now()
        self.query_one(Digits).update(f"{clock:%x} -- {clock:%X}")

    
    

    
    
    
    