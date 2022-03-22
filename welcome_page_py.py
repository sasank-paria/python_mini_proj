import sys
from PyQt5 import uic
from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap
import images_qrc
#--------------------------------------------------------------------------------------------------------------------



class welcome_page(QDialog):
    def __init__(self):
        super(welcome_page,self).__init__()
        uic.loadUi("welcome_page.ui",self)
        self.welcome_page_signin_button.clicked.connect(self.gotologin)
        self.welcome_page_register_button.clicked.connect(self.gotoregister)

    def gotologin(self):
        from signin_py import signin
        login=signin()
        widget.close()

    def gotoregister(self):
        from  registration_py import registration
        register=registration()
        widget.close()




#screen output
app = QApplication(sys.argv)

welcome=welcome_page()
widget=QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(735)
widget.setFixedWidth(1124)
widget.show()

sys.exit(app.exec_())
