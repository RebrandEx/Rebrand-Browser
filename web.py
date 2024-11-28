import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class SimpleBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a QWebEngineView widget to display web pages
        self.browser = QWebEngineView()

        # Set the default webpage (e.g., Google's homepage)
        self.browser.setUrl(QUrl("https://rebrandex.github.io/Rebrand"))

        # Set the browser widget as the central widget
        self.setCentralWidget(self.browser)

        # Create a navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Back button
        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # Forward button
        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # Reload button
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # URL bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        # Update the URL bar when the page is loaded
        self.browser.urlChanged.connect(self.update_url_bar)

        self.showMaximized()
        self.setWindowTitle("Rebrand Webbrowser")

    def update_url_bar(self, q):
        self.url_bar.setText(q.toString())

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

# Initialize the application
app = QApplication(sys.argv)
QApplication.setApplicationName("Rebrand Browser")
window = SimpleBrowser()
app.exec_()
