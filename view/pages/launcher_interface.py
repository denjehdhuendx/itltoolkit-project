from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from qfluentwidgets import *
from qfluentwidgets import FluentIcon as FIF
from view.pages.home_interface import HomeInterface

class LauncherInterface(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setFixedSize(336, 400)
        self.setObjectName('launcherInterface')