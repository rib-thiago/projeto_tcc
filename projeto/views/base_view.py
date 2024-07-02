class BaseView:
    def __init__(self, view_manager):
        self.view_manager = view_manager

    def get_doc_controller(self):
        return self.view_manager.doc_controller

    def get_para_controller(self):
        return self.view_manager.para_controller
