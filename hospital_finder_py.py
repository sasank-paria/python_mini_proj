import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap
#-------------------------------------------------------------------------------------------------------------------------

class hospital_finder(QDialog):
    def __init__(self):
        super(hospital_finder,self).__init__()
        uic.loadUi("hospital_finder.ui",self)
        self.hospital_nearme_home_button.clicked.connect(self.gotohome)

    def gotohome(self):
        from homepage_py import homepage
        h=homepage()
        widget.close()




#screen output
app = QApplication(sys.argv)
welcome=hospital_finder()
widget=QStackedWidget()

widget.addWidget(welcome)
widget.setFixedHeight(1041)
widget.setFixedWidth(1380)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("exiting")