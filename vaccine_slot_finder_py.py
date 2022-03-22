import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap
#-------------------------------------------------------------------------------------------------------------------------

class vaccine_slot_finder(QDialog):
    def __init__(self):
        super(vaccine_slot_finder,self).__init__()
        uic.loadUi("vaccine_slot_finder.ui",self)
        self.vaccine_slot_home_button.clicked.connect(self.gotohome)

    def gotohome(self):
        from homepage_py import homepage
        h=homepage()
        widget.close()

#screen output
app = QApplication(sys.argv)
welcome=vaccine_slot_finder()
widget=QStackedWidget()

widget.addWidget(welcome)
widget.setFixedHeight(841)
widget.setFixedWidth(900)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("exiting")