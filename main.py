import os
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

# 添加项目根目录到系统路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 设置Qt属性 - 必须在QApplication创建之前
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

app = QApplication(sys.argv)

try:
    from view.pages.main_window import MainWindow
except ImportError as e:
    print(f"导入错误: {e}")
    sys.exit(1)



w = MainWindow()
w.show()

app.exec_()