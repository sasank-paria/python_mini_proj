import sys
from PyQt5 import uic
from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap
import images_qrc
import sqlite3
import images_qrc
import registration_img_qrc
#--------------------------------------------------------------------------------------------------------------------



class welcome_page(QDialog):
    def __init__(self):
        super(welcome_page,self).__init__()
        uic.loadUi("welcome_page.ui",self)
        self.welcome_page_signin_button.clicked.connect(self.gotologin)
        self.welcome_page_register_button.clicked.connect(self.gotoregister)

    def gotologin(self):

        login=signin()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoregister(self):

        register=registration()
        widget.addWidget(register)
        widget.setCurrentIndex(widget.currentIndex() + 1)



class signin(QDialog):
    def __init__(self):
        super(signin,self).__init__()
        uic.loadUi("signin.ui",self)
        self.signin_password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_button.clicked.connect(self.login_backend)
        self.click_here_toregister.clicked.connect(self.goregister)

    def goregister(self):

        r=registration()
        widget.addWidget(r)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def login_backend(self):

        username = self.signin_username_field.text()
        password = self.signin_password_field.text()

        if len(username)==0 or len(password)==0:
            self.messagefield.setText("enter valid data!")

        else:
            conn = sqlite3.connect("python_mini_proj.db")
            cur = conn.cursor()
            query = 'SELECT password FROM signup_page WHERE username =\''+username+"\'"
            #query='SELECT username password FROM signup_page '
            cur.execute(query)
            pass_ = cur.fetchone()[0]
            if pass_ == password:

               home=homepage()
               widget.addWidget(home)
               widget.setCurrentIndex(widget.currentIndex() + 1)
            else:
                self.messagefield.setText("Invalid username or password")




class registration(QDialog):
    def __init__(self):
        super(registration,self).__init__()
        uic.loadUi("registration.ui",self)
        self.reg_password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.reg_confirmedpassword_field.setEchoMode(QtWidgets.QLineEdit.Password)

        self.signup_button.clicked.connect(self.signup_backend)
        self.reg_signin_button.clicked.connect(self.login_page_open)

    def login_page_open(self):

        r=signin()
        widget.addWidget(r)
        widget.setCurrentIndex(widget.currentIndex() + 1)



    def signup_backend(self):
        user = self.reg_user_name_field.text()
        password = self.reg_password_field.text()
        confirmpassword = self.reg_confirmedpassword_field.text()
        emailid=self.reg_emailid_field.text()
        mobile=self.reg_mobileno_field.text()
        resaddress=self.reg_resaddress_field.toPlainText()
        pincode=self.reg_pincode_field.text()

        if len(user)==0 or len(password)==0 or len(confirmpassword)==0:
            self.register_error_msg_text_field.setText("please enter username and password fields!")

        elif password!=confirmpassword:
            self.register_error_msg_text_field.setText("passwords are not matching!")
        else:

            conn = sqlite3.connect("python_mini_proj.db")
            cur = conn.cursor()

            reg_data = [user, password , confirmpassword,emailid,mobile,resaddress,pincode]
            cur.execute('INSERT INTO signup_page (username, password ,confirmed_password,email,mobileno,res_address,pincode) VALUES (?,?,?,?,?,?,?)', reg_data)

            conn.commit()
            conn.close()

            self.register_error_msg_text_field.setText("registered successfully!")





class homepage(QMainWindow):
    def __init__(self):
        super(homepage,self).__init__()
        uic.loadUi("homepage.ui",self)
        self.get_vaccinated.clicked.connect(self.gotoslotfinder)
        self.hospital_finder.clicked.connect(self.gotohospital)
        self.medicine_search.clicked.connect(self.gotomedicine)

    def gotohospital(self):

        h=hospital_finder()
        widget.addWidget(h)
        widget.setCurrentIndex(widget.currentIndex() + 1)


    def gotoslotfinder(self):

            v=vaccine_slot_finder()
            widget.addWidget(v)
            widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotomedicine(self):

        m=medicine_search()
        widget.addWidget(m)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class hospital_finder(QDialog):
    def __init__(self):
        super(hospital_finder,self).__init__()
        uic.loadUi("hospital_finder.ui",self)
        self.hospital_nearme_home_button.clicked.connect(self.gotohome)

    def gotohome(self):

        h=homepage()
        widget.addWidget(h)
        widget.setCurrentIndex(widget.currentIndex() + 1)




class medicine_search(QDialog):
    def __init__(self):
        super(medicine_search,self).__init__()
        uic.loadUi("medicine_search.ui",self)
        self.medicine_home_button.clicked.connect(self.gotohome)
        self.medicine_search_button.clicked.connect(self.medicine)

    def gotohome(self):

        h=homepage()
        widget.addWidget(h)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def medicine(self):
        import requests
        import json
        query = self.search_midicine_textbar.text()
        url = f"https://google-search3.p.rapidapi.com/api/v1/search/q={query} +buy online +netmeds+pharmeasy+1mg"

        headers = {
            "X-User-Agent": "desktop",
            "X-Proxy-Location": "EU",
            "X-RapidAPI-Host": "google-search3.p.rapidapi.com",
            "X-RapidAPI-Key": "1f62d360a0mshab4da6de118667bp13703cjsn05c591a9a491"
        }

        response = requests.request("GET", url, headers=headers)

        response1 = response.json()

        with open("news.json", "w") as outfile:
            json.dump(response1, outfile)

        label1_1 = response1['results'][0]["title"]
        label1_2 = response1['results'][0]["link"]
        label1_3 = response1['results'][0]["description"]

        label2_1 = response1['results'][1]["title"]
        label2_2 = response1['results'][1]["link"]
        label2_3 = response1['results'][1]["description"]

        label3_1 = response1['results'][2]["title"]
        label3_2 = response1['results'][2]["link"]
        label3_3 = response1['results'][2]["description"]

        label4_1 = response1['results'][3]["title"]
        label4_2 = response1['results'][3]["link"]
        label4_3 = response1['results'][3]["description"]

        label5_1 = response1['results'][4]["title"]
        label5_2 = response1['results'][4]["link"]
        label5_3 = response1['results'][4]["description"]

        label6_1 = response1['results'][5]["title"]
        label6_2 = response1['results'][5]["link"]
        label6_3 = response1['results'][5]["description"]

        label7_1 = response1['results'][6]["title"]
        label7_2 = response1['results'][6]["link"]
        label7_3 = response1['results'][6]["description"]

        label8_1 = response1['results'][7]["title"]
        label8_2 = response1['results'][7]["link"]
        label8_3 = response1['results'][7]["description"]

        self.label.setText(label1_1)
        self.label_3.setText(label1_2)
        self.label_5.setText(label1_3)






class vaccine_slot_finder(QDialog):
    def __init__(self):
        super(vaccine_slot_finder,self).__init__()
        uic.loadUi("vaccine_slot_finder.ui",self)
        self.vaccine_slot_home_button.clicked.connect(self.gotohome)

    def gotohome(self):

        h=homepage()
        widget.addWidget(h)
        widget.setCurrentIndex(widget.currentIndex() + 1)













#screen output
app = QApplication(sys.argv)

welcome=welcome_page()
widget=QtWidgets.QStackedWidget()
widget.addWidget(welcome)
# widget.setFixedHeight(735)
# widget.setFixedWidth(1124)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("exiting")