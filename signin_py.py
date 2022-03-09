import sys
from PyQt5 import uic
from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap

class signin(QDialog):
    def __init__(self):
        super(signin,self).__init__()
        uic.loadUi("signin.ui",self)




#screen output
app = QApplication(sys.argv)
welcome=signin()
widget=QStackedWidget()

widget.addWidget(welcome)
widget.setFixedHeight(768)
widget.setFixedWidth(425)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("exiting")