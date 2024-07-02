class ViewManager:
    def __init__(self, doc_controller, para_controller):
        self.doc_controller = doc_controller
        self.para_controller = para_controller
        self.views = {}

    def register_view(self, view_name, view_class):
        self.views[view_name] = view_class

    def get_view(self, view_name, *args, **kwargs):
        if view_name in self.views:
            return self.views[view_name](self, *args, **kwargs)
        else:
            raise ValueError(f"View '{view_name}' não registrada.")

    def start(self, initial_view):
        current_view = initial_view
        while current_view:
            current_view = current_view.display()
