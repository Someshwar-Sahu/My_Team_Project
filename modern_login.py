from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
    QHBoxLayout, QFrame, QGraphicsDropShadowEffect, QGraphicsOpacityEffect
)
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QFont

class InputField(QWidget):
    def __init__(self, placeholder, icon_text=""):
        super().__init__()
        self.icon = QLabel(icon_text)
        self.icon.setFixedSize(34, 34)
        self.icon.setAlignment(Qt.AlignCenter)
        self.icon.setObjectName("inputIcon")

        self.edit = QLineEdit()
        self.edit.setPlaceholderText(placeholder)
        self.edit.setFixedHeight(40)
        self.edit.setObjectName("inputEdit")

        row = QHBoxLayout(self)
        row.setContentsMargins(0, 0, 0, 0)
        row.setSpacing(10)
        row.addWidget(self.icon)
        row.addWidget(self.edit)

class LoginCard(QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName("card")
        self.setFixedSize(640, 440)

        title = QLabel("Sign up")
        title.setAlignment(Qt.AlignCenter)
        title.setObjectName("cardTitle")
        title.setFont(QFont("Segoe UI", 28, QFont.Bold))

        name = InputField("Full name", "👤")
        email = InputField("Email", "✉️")
        password = InputField("Password", "🔒")
        password.edit.setEchoMode(QLineEdit.Password)

        self.primary_btn = QPushButton("Sign up")
        self.primary_btn.setFixedHeight(44)
        self.primary_btn.setObjectName("primaryBtn")

        or_label = QLabel("Or")
        or_label.setAlignment(Qt.AlignCenter)
        or_label.setObjectName("orLabel")

        google_btn = QPushButton("  Continue with Google")
        google_btn.setFixedHeight(44)
        google_btn.setObjectName("googleBtn")
        g_icon = QLabel("G")
        g_icon.setFixedSize(20, 20)
        g_icon.setAlignment(Qt.AlignCenter)
        g_icon.setObjectName("gIcon")
        google_layout = QHBoxLayout(google_btn)
        google_layout.setContentsMargins(12, 0, 12, 0)
        google_layout.setSpacing(8)
        google_layout.addWidget(g_icon, 0, Qt.AlignLeft)

        form = QVBoxLayout()
        form.setSpacing(18)
        form.addWidget(title)
        form.addStretch()
        form.addWidget(name)
        form.addWidget(email)
        form.addWidget(password)
        form.addWidget(self.primary_btn)
        form.addWidget(or_label)
        form.addWidget(google_btn)
        form.addStretch()
        form.setContentsMargins(72, 28, 72, 28)

        self.setLayout(form)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(28)
        shadow.setXOffset(0)
        shadow.setYOffset(10)
        shadow.setColor(Qt.black)
        self.setGraphicsEffect(shadow)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modern Login")
        self.resize(1100, 720)
        self.setup_ui()
        self.apply_styles()
        self.fade_in_card()

    def setup_ui(self):
        outer = QHBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setAlignment(Qt.AlignCenter)

        self.card = LoginCard()
        outer.addWidget(self.card)

    def fade_in_card(self):
        eff = QGraphicsOpacityEffect(self.card)
        self.card.setGraphicsEffect(eff)
        anim = QPropertyAnimation(eff, b"opacity", self)
        anim.setDuration(650)
        anim.setStartValue(0.0)
        anim.setEndValue(1.0)
        anim.setEasingCurve(QEasingCurve.OutCubic)
        anim.start(QPropertyAnimation.DeleteWhenStopped)

    def apply_styles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #69e0ff, stop:0.25 #5fe6d6, stop:1 #6bbafe);
                font-family: "Segoe UI";
                color: #dbe8f8;
            }
            QFrame#card {
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #21455a, stop:1 #0f2b45);
                border-radius: 12px;
            }
            QLabel#cardTitle {
                color: #79caff;
                font-size: 34px;
            }
            QWidget InputField {
                background: transparent;
            }
            QLabel#inputIcon {
                background-color: rgba(0,0,0,0.18);
                border-radius: 6px;
                color: #dbe8f8;
                font-size: 14px;
            }
            QLineEdit#inputEdit {
                background-color: rgba(0,0,0,0.28);
                border: none;
                border-radius: 6px;
                padding-left: 10px;
                color: #dbe8f8;
                font-size: 14px;
            }
            QLineEdit#inputEdit:focus {
                background-color: rgba(0,0,0,0.36);
            }
            QPushButton#primaryBtn {
                background-color: #58befe;
                color: #062033;
                border: none;
                border-radius: 8px;
                font-weight: 600;
                font-size: 15px;
            }
            QPushButton#primaryBtn:pressed {
                background-color: #3ea6f6;
            }
            QLabel#orLabel {
                color: #c7dff6;
                font-size: 13px;
            }
            QPushButton#googleBtn {
                background-color: #ffffff;
                color: #0b2340;
                border-radius: 8px;
                font-size: 14px;
                text-align: left;
            }
            QLabel#gIcon {
                color: #de5246;
                font-weight: bold;
            }
        """)

if __name__ == "__main__":
    app = QApplication([])
    w = MainWindow()
    w.show()
    app.exec()
