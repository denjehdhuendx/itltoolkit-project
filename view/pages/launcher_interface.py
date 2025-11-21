from PyQt5.QtWidgets import QWidget

class LauncherInterface(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setFixedSize(336, 400)
        self.setObjectName('launcherInterface')