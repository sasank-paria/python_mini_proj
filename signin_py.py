import sys
from PyQt5 import uic
from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap
import sqlite3
#------------------------------------------------------------------------------------------------------------------


class signin(QDialog):
    def __init__(self):
        super(signin,self).__init__()
        uic.loadUi("signin.ui",self)
        self.signin_password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_button.clicked.connect(self.login_backend)

    def login_backend(self):
        username = self.signin_username_field.text()
        password = self.signin_password_field.text()

        if len(username)==0 or len(password)==0:
            self.messagefield.setText("enter valid data!")
        #
        # else:
        #     conn = sqlite3.connect("shop_data.db")
        #     cur = conn.cursor()
        #     query = 'SELECT password FROM login_info WHERE username =\''+username+"\'"
        #     cur.execute(query)
        #     result_pass = cur.fetchone()[0]
        #     if result_pass == password:
        #         print("Successfully logged in.")
        #         self.error.setText("")
        #     else:
        #         self.error.setText("Invalid username or password")












#screen output
app = QApplication(sys.argv)
welcome=signin()
widget=QStackedWidget()

widget.addWidget(welcome)
widget.setFixedHeight(692)
widget.setFixedWidth(713)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("exiting")