from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from base_page import BasePage
from PySide6.QtWidgets import QGraphicsDropShadowEffect
from PySide6.QtGui import QColor


class LoginPage(BasePage):
    def __init__(self, stacked_widget):
        super().__init__(stacked_widget)
        self.stacked_widget = stacked_widget
        

        title_label = QLabel("Welcome Back")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setObjectName("titleLabel")

        self.input_username = QLineEdit()
        self.input_username.setPlaceholderText("Username")
        self.input_username.setFixedHeight(40)

        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("Password")
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_password.setFixedHeight(40)

        self.btn_login = QPushButton("Login")
        self.btn_login.setFixedHeight(40)
        self.btn_login.setObjectName("loginButton")
        self.btn_login.clicked.connect(self.check_login)

        self.btn_signup = QPushButton("Create an Account")
        self.btn_signup.setFixedHeight(40)
        self.btn_signup.setObjectName("signupButton")
        self.btn_signup.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))

        self.inner_layout.addStretch()
        self.inner_layout.addWidget(title_label)
        self.inner_layout.addWidget(self.input_username)
        self.inner_layout.addWidget(self.input_password)
        self.inner_layout.addWidget(self.btn_login)
        self.inner_layout.addWidget(self.btn_signup)
        self.inner_layout.addStretch()

        self.apply_styles()

    def check_login(self):
        if self.input_username.text() == "admin" and self.input_password.text() == "1234":
            QMessageBox.information(self, "Success", "Login successful!")
            if self.stacked_widget.count() > 2:
                self.stacked_widget.setCurrentIndex(2)
        else:
            QMessageBox.warning(self, "Error", "Invalid username or password.")

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