import sys
from PySide6.QtWidgets import QApplication, QStackedWidget, QMainWindow
from login_page import LoginPage
from signup_page import SignupPage
from dashboard import DashboardPage

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    main_window = QMainWindow()
    main_window.setWindowTitle("AI Stock Analyzer")
    main_window.resize(800, 600)
    
    stacked_widget = QStackedWidget()
    
    main_window.setStyleSheet("""
        QStackedWidget {
        background-color: qlineargradient(
        x1: 0, y1: 0, x2: 0, y2: 1,
        stop: 0   #0f0c29,       /* deep midnight blue */
        stop: 0.25 #1a1a52,       /* indigo shade */
        stop: 0.50 #302b63,       /* muted violet */
        stop: 0.75 #3b3a76,       /* soft lavender-blue */
        stop: 1   #24243e        /* dark slate */
    );
    }
    """)



    login_page = LoginPage(stacked_widget)
    signup_page = SignupPage(stacked_widget)
    dashboard_page = DashboardPage(stacked_widget)

    stacked_widget.addWidget(login_page)        # index 0
    stacked_widget.addWidget(signup_page)       # index 1
    stacked_widget.addWidget(dashboard_page)    # index 2

    main_window.setCentralWidget(stacked_widget)
    
    main_window.show()
    sys.exit(app.exec())
