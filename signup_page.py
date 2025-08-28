from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from base_page import BasePage
from PySide6.QtWidgets import QGraphicsDropShadowEffect
from PySide6.QtGui import QColor

class SignupPage(BasePage):
    def __init__(self, stacked_widget):
        super().__init__(stacked_widget)
        self.stacked_widget = stacked_widget

        title_label = QLabel("Create Account")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setObjectName("titleLabel")

        self.input_newuser = QLineEdit()
        self.input_newuser.setPlaceholderText("New Username")
        self.input_newuser.setFixedHeight(40)

        self.input_newpass = QLineEdit()
        self.input_newpass.setPlaceholderText("New Password")
        self.input_newpass.setEchoMode(QLineEdit.Password)
        self.input_newpass.setFixedHeight(40)

        self.btn_register = QPushButton("Register")
        self.btn_register.setFixedHeight(40)
        self.btn_register.setObjectName("loginButton")
        self.btn_register.clicked.connect(self.register_user)

        self.btn_back = QPushButton("Back to Login")
        self.btn_back.setFixedHeight(40)
        self.btn_back.setObjectName("signupButton")
        self.btn_back.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))

        self.inner_layout.addStretch()
        self.inner_layout.addWidget(title_label)
        self.inner_layout.addWidget(self.input_newuser)
        self.inner_layout.addWidget(self.input_newpass)
        self.inner_layout.addWidget(self.btn_register)
        self.inner_layout.addWidget(self.btn_back)
        self.inner_layout.addStretch()

        self.apply_styles()

    def register_user(self):
        QMessageBox.information(self, "Registered", "Account created successfully!")
        self.stacked_widget.setCurrentIndex(0)

    def apply_styles(self):
            self.setFont(QFont("Segoe UI", 10))
            # Add drop shadow to container (simulate "box-shadow")
            shadow = QGraphicsDropShadowEffect(self)
            shadow.setBlurRadius(25)
            shadow.setXOffset(0)
            shadow.setYOffset(6)
            shadow.setColor(QColor(0, 0, 0, 150))
            self.container.setGraphicsEffect(shadow)
            self.container.setStyleSheet("background-color: rgba(33, 69, 90, 180); ")