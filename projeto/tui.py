# tui.py
from projeto.views.main_menu_view import MainMenuView

class TUI:
    def __init__(self, doc_controller, para_controller):
        self.doc_controller = doc_controller
        self.para_controller = para_controller

    def run(self):
        current_view = MainMenuView(self.doc_controller, self.para_controller)
        while current_view:
            current_view = current_view.display()
