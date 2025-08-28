from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt
from styles import BASE_STYLES

class BasePage(QWidget):
    """A base class for all pages to handle common setup."""
    def __init__(self, stacked_widget):
        super().__init__()
        # Encapsulation: The stacked_widget is now part of the BasePage's state.
        self._stacked_widget = stacked_widget
        
        # Common UI setup is encapsulated within this class.
        self._setup_base_ui()

    def _setup_base_ui(self):
        """Creates the basic container and layout for a page."""
        outer_layout = QHBoxLayout(self)
        outer_layout.setContentsMargins(0, 0, 0, 0)
        outer_layout.setAlignment(Qt.AlignCenter)

        self.container = QWidget()
        self.container.setFixedWidth(400)
        self.container.setFixedHeight(400)
        
        self.inner_layout = QVBoxLayout(self.container)
        self.inner_layout.setContentsMargins(50, 50, 50, 50)
        self.inner_layout.setSpacing(15)
        
        outer_layout.addWidget(self.container)

        self.setStyleSheet(BASE_STYLES)