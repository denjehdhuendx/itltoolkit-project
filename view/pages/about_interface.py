from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from qfluentwidgets import *

class AboutInterface(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setFixedSize(336, 400)

        self.vBoxLayout = QVBoxLayout(self)
        self.title = QLabel('关于', self)
        self.vBoxLayout.addWidget(self.title)
        self.__initWidget()

    def __initWidget(self):
            
        self.setObjectName('aboutInterface')    
        self.vBoxLayout.setContentsMargins(10, 10, 10, 10)
        self.vBoxLayout.setSpacing(10)

