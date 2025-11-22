from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from qfluentwidgets import *
from qfluentwidgets import FluentIcon as FIF, NavigationItemPosition
from view.pages.home_interface import *
from view.pages.about_interface import *
from view.pages.launcher_interface import *
from view.pages.jiyuinterface import *
import os
#导入块到此结束


class MainWindow(FluentWindow):
    def __init__(self):
        super().__init__()
        
        # 设置自定义字体
        self.setCustomFont()
        
        # 初始化界面
        self.homeInterface = HomeInterface(self)
        self.launcherInterface = LauncherInterface(self)
        self.aboutInterface = AboutInterface(self)
        self.jiyuInterface = JiyuInterface(self)

        self.navigationInterface.setAcrylicEnabled(True)
        # 初始化窗口
        self.initWindow()
        
        # 初始化导航
        self.initNavigation()
        
        
        # 设置主题监听器
        self.themeListener = SystemThemeListener(self)
        
    def initNavigation(self):
        self.addSubInterface(self.homeInterface, FIF.HOME, self.tr('主页'))
        self.addSubInterface(self.jiyuInterface, FIF.CAMERA, self.tr('极域助手'))
        self.navigationInterface.addSeparator()
        self.addSubInterface(self.launcherInterface, FIF.PLAY, self.tr('启动器'))

        
        self.addSubInterface(
            self.aboutInterface, FIF.INFO, self.tr('关于'), NavigationItemPosition.BOTTOM)
        
    def setCustomFont(self):
        """设置自定义字体"""
        font_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'font.ttf')
        font_id = QFontDatabase.addApplicationFont(font_path)
        
        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            custom_font = QFont(font_family, 10)
            QApplication.setFont(custom_font)
            print(f"成功加载自定义字体: {font_family}")
        else:
            print("警告: 无法加载自定义字体，使用系统默认字体")
    
    def initWindow(self):
        self.setWindowTitle('Information Technology Lesson Toolkit V1.0') 
        self.setWindowIcon(QIcon('icon.ico'))
        self.setMinimumSize(800, 600)