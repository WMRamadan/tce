"""
TCE - Terminal Code Editor.
"""

import os

from rich.syntax import Syntax
from rich.traceback import Traceback

from textual import events
from textual.app import App, ComposeResult
from textual.containers import Container, Vertical
from textual.reactive import var
from textual.widgets import DirectoryTree, Footer, Header, Static


class TceApp(App):
    """Terminal code editor app."""
    TITLE = "Terminal Code Editor"
    CSS_PATH = "tce.css"
    BINDINGS = [
        ("ctrl+f", "toggle_files", "Toggle Files"),
        ("ctrl+q", "quit", "Quit"),
    ]

    show_tree = var(True)

    def watch_show_tree(self, show_tree: bool) -> None:
        """Called when show_tree is modified."""
        self.set_class(show_tree, "-show-tree")

    def compose(self) -> ComposeResult:
        """Compose the UI."""
        path = os.getcwd()
        yield Header()
        yield Container(
            DirectoryTree(path, id="tree-view"),
            Vertical(Static(id="code", expand=True), id="code-view"),
        )
        yield Footer()

    def on_mount(self, event: events.Mount) -> None:
        self.query_one(DirectoryTree).focus()

    def on_directory_tree_file_selected(
        self, event: DirectoryTree.FileSelected
    ) -> None:
        """Called when the user clicks a file in the directory tree."""
        event.stop()
        code_view = self.query_one("#code", Static)
        try:
            syntax = Syntax.from_path(
                event.path,
                line_numbers=True,
                word_wrap=False,
                indent_guides=True,
                theme="github-dark",
            )
        except Exception:
            code_view.update(Traceback(theme="github-dark", width=None))
            self.sub_title = "ERROR"
        else:
            code_view.update(syntax)
            self.query_one("#code-view").scroll_home(animate=False)
            self.sub_title = event.path

    def action_toggle_files(self) -> None:
        """Called in response to key binding."""
        self.show_tree = not self.show_tree

def main() -> None:
    TceApp().run()
