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
        self.initUI()
        self.__initWidget()

    def initUI(self):
        """初始化用户界面"""
        # 设置对象名称 - 这是关键！
        self.setObjectName('homeInterface')
        
        # 创建主布局
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)
        
        # 添加标题
        title = QLabel('主页', self)
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: #333;
            padding: 20px;
        """)
        layout.addWidget(title)
        
        # 添加欢迎卡片
        card = PushSettingCard(
            text='启动器',
            icon=FluentIcon.PLAY,
            title="转到启动器",
            content='前往ITLTookit的启动器界面以更好的摸鱼'
        )
        layout.addWidget(card)
        
        # 添加一些示例内容
        infoLabel = QLabel('你知道吗？Itltookit原作者推的动漫角色已突破100+！', self)
        infoLabel.setWordWrap(True)
        infoLabel.setStyleSheet("""
            font-size: 14px;
            color: #666;
            padding: 15px;
            background-color: #f0f8ff;
            border-radius: 8px;
            border: 1px solid #d1e7ff;
        """)
        layout.addWidget(infoLabel)
        
        # 添加弹性空间
        layout.addStretch()

    def __initWidget(self):
        """初始化组件属性"""
        # 确保对象名称已设置
        if not self.objectName():
            self.setObjectName('homeInterface')