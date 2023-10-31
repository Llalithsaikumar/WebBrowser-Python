import sys
import typing
import requests
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QWidget

class MainScreen(QMainWindow):
    def __init__(self):
        super(MainScreen,self).__init__()
        self.Browser = QWebEngineView()
        self.Browser.setUrl(QUrl("https://www.google.com"))
        self.setCentralWidget(self.Browser)
        self.showMaximized()
        # Navigation Bar
        navbar = QToolBar()
        self.addToolBar(navbar)
        # Back Button
        back_btn = QAction("Back", self)
        back_btn.triggered.connect(self.Browser.back)
        navbar.addAction(back_btn)
        # Forward Button
        forward_btn = QAction("Forward", self)
        forward_btn.triggered.connect(self.Browser.forward)
        navbar.addAction(forward_btn)
        # Reload Button
        reload_btn = QAction("Reload", self)
        reload_btn.triggered.connect(self.Browser.reload)
        navbar.addAction(reload_btn)
        # Home Button
        home_btn = QAction("Home", self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)
        # URL Bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        self.Browser.urlChanged.connect(self.update_url)
    def navigate_home(self):
        self.Browser.setUrl(QUrl("https://www.google.com"))
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.Browser.setUrl(QUrl(url))
    def update_url(self, q):
        self.url_bar.setText(q.toString())
app = QApplication(sys.argv)
QApplication.setApplicationName("Web Browser by @LalithSaiKumar")
url = "https://www.google.com"
response = requests.get(url)
if response.status_code == 200:
    print("Connected to the internet")
    cookies = response.cookies
    for cookie in cookies:
        print(f"Cookie Name: {cookie.name}")
        print(f"Cookie Value: {cookie.value}")
    with open("cookies.txt", "w") as cookies_file:
        for cookie in cookies:
            cookies_file.write(f"Cookie Name: {cookie.name}\n")
            cookies_file.write(f"Cookie Value: {cookie.value}\n")
        print("Cookies saved to cookies.txt")
else:
    print("Not connected to the internet")

        
window = MainScreen()
app.exec_()
