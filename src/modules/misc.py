from textual.app import RenderResult, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Digits, Static, Label
from datetime import datetime

class Greeter(Static):
    def compose(self) -> ComposeResult:
        yield Static("SCREEN IS LOCKED", classes="clocklabel")
        yield GreeterBox( classes="clocklabel")
        yield Static("GCCS MANAGING TOOLS (C) 2024 - MIKEL ICETA CNB-CSIC", classes="clocklabel")

class GreeterBox(Static):
    """A widget for greeting"""

    def compose(self) -> ComposeResult:
        yield Static("GALILEO COMPUTE SYSTEM v1", classes="clocklabel")
        yield Digits("", id="clock")
        yield Static("GALILEO SYSTEM WELCOMES YOU ^_^ PRESS L TO UNLOCK", classes="clocklabel")

    def on_mount(self) -> None:
        self.update_clock()
        self.set_interval(1, self.update_clock)

    def update_clock(self) -> None:
        clock = datetime.now()
        self.query_one(Digits).update(f"{clock:%x} -- {clock:%X}")

    
    

    
    
    
    