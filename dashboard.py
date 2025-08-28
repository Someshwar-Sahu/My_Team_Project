from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QComboBox, QFrame
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class DashboardPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # ---- Top Bar ----
        top_bar = QHBoxLayout()
        title = QLabel("📊 Stock Predictor Dashboard")
        title.setFont(QFont("Segoe UI", 18, QFont.Bold))
        title.setAlignment(Qt.AlignLeft)
        title.setStyleSheet("""
            QLabel {
                background-color: transparent;
                color: #89b4fa;
            }
        """)

        logout_btn = QPushButton("Logout")
        logout_btn.setFixedHeight(35)
        logout_btn.setStyleSheet("""
            QPushButton {
                background-color: #f38ba8;
                border: none;
                border-radius: 8px;
                color: white;
                font-weight: bold;
                padding: 8px 15px;
            }
            QPushButton:hover { background-color: #f87171; }
        """)
        logout_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))

        top_bar.addWidget(title)
        top_bar.addStretch()
        top_bar.addWidget(logout_btn)

        # ---- Search Bar ----
        search_bar = QHBoxLayout()
        self.stock_input = QLineEdit()
        self.stock_input.setPlaceholderText("Enter stock symbol (e.g., AAPL, TSLA)")
        self.stock_input.setFixedHeight(40)
        self.stock_input.setStyleSheet("""
            QLineEdit {
                background-color: #313244;
                border: 1px solid #45475a;
                border-radius: 8px;
                padding: 10px;
                color: #cdd6f4;
                font-size: 14px;
            }
        """)

        self.search_btn = QPushButton("Predict")
        self.search_btn.setFixedHeight(40)
        self.search_btn.setStyleSheet("""
            QPushButton {
                background-color: #a6e3a1;
                border: none;
                border-radius: 8px;
                color: #1e1e2e;
                font-weight: bold;
                padding: 8px 15px;
            }
            QPushButton:hover { background-color: #b8f3b3; }
        """)

        search_bar.addWidget(self.stock_input)
        search_bar.addWidget(self.search_btn)

        # ---- Placeholder for Chart ----
        chart_frame = QFrame()
        chart_frame.setStyleSheet("background-color: #313244; border-radius: 12px;")
        chart_frame.setFixedHeight(300)

        chart_label = QLabel("📈 Stock Price Chart will appear here")
        chart_label.setAlignment(Qt.AlignCenter)
        chart_label.setStyleSheet("color: #cdd6f4; font-size: 16px;")
        chart_layout = QVBoxLayout(chart_frame)
        chart_layout.addWidget(chart_label)

        # ---- Stats Section ----
        stats_layout = QHBoxLayout()

        self.price_card = self.create_stat_card("Current Price", "$0.00")
        self.change_card = self.create_stat_card("Change", "0%")
        self.pred_card = self.create_stat_card("Prediction", "N/A")

        stats_layout.addWidget(self.price_card)
        stats_layout.addWidget(self.change_card)
        stats_layout.addWidget(self.pred_card)

        # ---- Assemble Layout ----
        main_layout.addLayout(top_bar)
        main_layout.addLayout(search_bar)
        main_layout.addWidget(chart_frame)
        main_layout.addLayout(stats_layout)
        self.setLayout(main_layout)

        self.setStyleSheet("background-color: #1e1e2e;")

    def create_stat_card(self, title, value):
        frame = QFrame()
        frame.setStyleSheet("background-color: #45475a; border-radius: 10px;")
        frame.setFixedHeight(100)
        layout = QVBoxLayout(frame)
        layout.setAlignment(Qt.AlignCenter)

        lbl_title = QLabel(title)
        lbl_title.setStyleSheet("color: #89b4fa; font-size: 14px;")
        lbl_value = QLabel(value)
        lbl_value.setStyleSheet("color: #cdd6f4; font-size: 18px; font-weight: bold;")

        layout.addWidget(lbl_title)
        layout.addWidget(lbl_value)
        return frame
