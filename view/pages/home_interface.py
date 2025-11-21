from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from qfluentwidgets import *

########################################
# He1l0Wor1d-ice ©️ 2025               #
# home_interface.py  ,ITLTookit的一部分。#                            #
########################################

class HomeInterface(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setFixedSize(336, 400)

        self.vBoxLayout = QVBoxLayout(self)
        self.title = QLabel('主页', self)
        self.vBoxLayout.addWidget(self.title)
        
        self.__initWidget()

    def __initWidget(self):
        self.setObjectName('homeInterface')
        
        self.vBoxLayout.setContentsMargins(10, 10, 10, 10)
        self.vBoxLayout.setSpacing(10)
