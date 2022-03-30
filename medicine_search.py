import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap
#-------------------------------------------------------------------------------------------------------------------------

class medicine_search(QDialog):
    def __init__(self):
        super(medicine_search,self).__init__()
        uic.loadUi("medicine_search.ui",self)
        self.medicine_home_button.clicked.connect(self.gotohome)

    def gotohome(self):
        from homepage_py import homepage
        h=homepage()
        widget.close()


#screen output
app = QApplication(sys.argv)
welcome=medicine_search()
widget=QStackedWidget()

widget.addWidget(welcome)
widget.setFixedHeight(841)
widget.setFixedWidth(900)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("exiting")