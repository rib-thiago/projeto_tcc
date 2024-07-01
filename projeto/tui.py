from projeto.controllers.document_controller import DocumentController
from projeto.views.main_menu_view import MainMenuView

class TUI:
    def __init__(self, mongo_config):
        self.doc_controller = DocumentController(mongo_config)

    def run(self):
        current_view = MainMenuView(self.doc_controller)
        while current_view:
            current_view = current_view.display()
