import sqlite3
import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget

import registration_img_qrc
# --------------------------------------------------------------------------------------------------------------------------

class registration(QDialog):
    def __init__(self):
        super(registration, self).__init__()
        uic.loadUi("registration.ui", self)
        self.reg_password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.reg_confirmedpassword_field.setEchoMode(QtWidgets.QLineEdit.Password)

        self.signup_button.clicked.connect(self.signup_backend)
        self.reg_signin_button.clicked.connect(self.login_page_open)

    def login_page_open(self):
        from signin_py import signin
        login1 = signin()

    def signup_backend(self):
        user = self.reg_user_name_field.text()
        password = self.reg_password_field.text()
        confirmpassword = self.reg_confirmedpassword_field.text()
        emailid = self.reg_emailid_field.text()
        mobile = self.reg_mobileno_field.text()
        resaddress = self.reg_resaddress_field.toPlainText()
        pincode = self.reg_pincode_field.text()

        if len(user) == 0 or len(password) == 0 or len(confirmpassword) == 0:
             self.register_error_msg_text_field.setText("please enter username and password fields!")

        elif password != confirmpassword:
            self.register_error_msg_text_field.setText("passwords are not matching!")
        else:
            pass
            conn = sqlite3.connect("python_mini_proj.db")
            cur = conn.cursor()

            reg_data = [user, password, confirmpassword, emailid, mobile, resaddress, pincode]
            cur.execute(
                'INSERT INTO signup_page (username, password ,confirmed_password,email,mobileno,res_address,pincode) VALUES (?,?,?,?,?,?,?)',
                reg_data)

            conn.commit()
            conn.close()

            self.register_error_msg_text_field.setText("registered successfully!")


# screen output
app = QApplication(sys.argv)
welcome = registration()
widget = QStackedWidget()

widget.addWidget(welcome)
# widget.setFixedHeight(810)
# widget.setFixedWidth(1024)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("exiting")
