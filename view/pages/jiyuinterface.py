from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from qfluentwidgets import *


class JiyuInterface(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setFixedSize(336, 400)

        self.vBoxLayout = QVBoxLayout(self)
        self.title = QLabel('极域助手', self)
        self.vBoxLayout.addWidget(self.title)
        
        self.__initWidget()

    def __initWidget(self):
        self.setObjectName('jiyuinterface')
        
        self.vBoxLayout.setContentsMargins(10, 10, 10, 10)
        self.vBoxLayout.setSpacing(10)
