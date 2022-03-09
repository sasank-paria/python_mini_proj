import sys
from PyQt5 import uic
from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap

class registration(QDialog):
    def __init__(self):
        super(registration,self).__init__()
        uic.loadUi("registration.ui",self)




#screen output
app = QApplication(sys.argv)
welcome=registration()
widget=QStackedWidget()

widget.addWidget(welcome)
widget.setFixedHeight(810)
widget.setFixedWidth(1024)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("exiting")