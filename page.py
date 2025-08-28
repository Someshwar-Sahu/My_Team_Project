from abc import ABC, abstractmethod
from PySide6.QtWidgets import QWidget

class Page(QWidget, ABC):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget   # shared navigation

    @abstractmethod
    def apply_styles(self):
        """Each page must define its own styles"""
        pass
