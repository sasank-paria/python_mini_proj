import sys
from PyQt5 import uic
from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap

class homepage(QMainWindow):
    def __init__(self):
        super(homepage,self).__init__()
        uic.loadUi("homepage.ui",self)




#screen output
app = QApplication(sys.argv)
welcome=homepage()
widget=QStackedWidget()

widget.addWidget(welcome)
widget.setFixedHeight(759)
widget.setFixedWidth(1374)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("exiting")