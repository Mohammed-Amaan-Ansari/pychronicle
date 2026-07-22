from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static


class PyChronicleApp(App):

    TITLE = "PyChronicle"

    SUB_TITLE = "Time Travel Debugger"

    def compose(self) -> ComposeResult:

        yield Header()

        yield Static(
            " Code Viewer (Coming Soon)",
            id="code_view",
        )

        yield Static(
            "Timeline (Coming Soon)",
            id="timeline",
        )

        yield Footer()


if __name__ == "__main__":
    PyChronicleApp().run()