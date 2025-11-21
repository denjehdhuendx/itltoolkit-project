from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from qfluentwidgets import *
from qfluentwidgets import FluentIcon as FIF, NavigationItemPosition
from view.pages.home_interface import HomeInterface
from view.pages.about_interface import AboutInterface
from view.pages.launcher_interface import LauncherInterface
from view.pages.jiyuinterface import JiyuInterface
#导入块到此结束


class MainWindow(FluentWindow):
    def __init__(self):
        super().__init__()
        
        # 初始化界面
        self.homeInterface = HomeInterface(self)
        self.launcherInterface = LauncherInterface(self)
        self.aboutInterface = AboutInterface(self)
        self.jiyuinterface = JiyuInterface(self)

        self.navigationInterface.setAcrylicEnabled(True)
        # 初始化窗口
        self.initWindow()
        
        # 初始化导航
        self.initNavigation()
        
        
        # 设置主题监听器
        self.themeListener = SystemThemeListener(self)
        
    def initNavigation(self):
        self.addSubInterface(self.homeInterface, FIF.HOME, self.tr('主页'))
        self.addSubInterface(self.jiyuinterface, FIF.CAMERA, self.tr('极域助手'))
        self.navigationInterface.addSeparator()
        self.addSubInterface(self.launcherInterface, FIF.PLAY, self.tr('启动器'))

        
        self.addSubInterface(
            self.aboutInterface, FIF.INFO, self.tr('关于'), NavigationItemPosition.BOTTOM)
        
    def initWindow(self):
        self.setWindowTitle('Information Technology Lesson Toolkit V1.0') 
        self.setWindowIcon(QIcon('logo.png'))
        self.setMinimumSize(800, 600)