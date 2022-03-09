import sys
from PyQt5 import uic
from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap

class welcome_page(QDialog):
    def __init__(self):
        super(welcome_page,self).__init__()
        uic.loadUi("welcome_page.ui",self)




#screen output
app = QApplication(sys.argv)
welcome=welcome_page()
widget=QStackedWidget()

widget.addWidget(welcome)
widget.setFixedHeight(735)
widget.setFixedWidth(1124)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("exiting")