import sys
import textwrap

from PyQt5 import uic
from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap
import images_qrc
import sqlite3
import images_qrc
import registration_img_qrc
import homepageimageqrc
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


        #covid data cases display

        import json

        import requests

        url = "https://covid-193.p.rapidapi.com/statistics"

        querystring = {"country": "India"}

        headers = {
            "X-RapidAPI-Host": "covid-193.p.rapidapi.com",
            "X-RapidAPI-Key": "1f62d360a0mshab4da6de118667bp13703cjsn05c591a9a491"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        response1 = response.json()
        #
        # with open("coviddata.json", "w") as file:
        #     json.dump(response1, file)
        #
        # print(response1)
        p1 = str(response1['response'][0]['country'])
        p2 = str(response1['response'][0]['population'])
        p3 = str(response1['response'][0]['cases']['active'])
        p4 = str(response1['response'][0]['cases']['critical'])
        p5 = str(response1['response'][0]['cases']['recovered'])
        p6 = str(response1['response'][0]['cases']['total'])
        p7 = str(response1['response'][0]['deaths']['total'])
        p8 = str(response1['response'][0]['day'])
        p9 = str(response1['response'][0]['time'])

        self.l1.setText(p1)
        self.l2.setText(p2)
        self.l3.setText(p3)
        self.l4.setText(p4)
        self.l5.setText(p5)
        self.l6.setText(p6)
        self.l7.setText(p7)
        self.l8.setText(p8)
        self.l9.setText(p9)


    def gotohospital(self):

        h=hospital_finder()
        widget.addWidget(h)
        widget.setCurrentIndex(widget.currentIndex() + 1)


    def gotoslotfinder(self):
        import Vaccine_Availability_Checker






    def gotomedicine(self):

        m=medicine_search()
        widget.addWidget(m)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class hospital_finder(QDialog):
    def __init__(self):
        super(hospital_finder,self).__init__()
        uic.loadUi("hospital_finder.ui",self)
        self.hospital_nearme_home_button.clicked.connect(self.gotohome)
        self.hospital_find_button.clicked.connect(self.hospitalfind)


    def gotohome(self):

        h=homepage()
        widget.addWidget(h)
        widget.setCurrentIndex(widget.currentIndex() + 1)



    def hospitalfind(self):
        #display area details with pincode
        import json

        import requests
        pincode=self.pincode_textbar.text()
        url = "https://pincode.p.rapidapi.com/"

        payload = {
            "searchBy": "pincode",
            "value": f"{pincode}"
        }
        headers = {
            "content-type": "application/json",
            "Content-Type": "application/json",
            "X-RapidAPI-Host": "pincode.p.rapidapi.com",
            "X-RapidAPI-Key": "1f62d360a0mshab4da6de118667bp13703cjsn05c591a9a491"
        }

        response = requests.request("POST", url, json=payload, headers=headers)

        response1 = response.json()

#display this on the ui page of hospital finder
        pin = response1[0]['pin']
        region = response1[0]['region']
        taluka = response1[0]['taluk']
        district = response1[0]['district']
        state = response1[0]['circle']

        #will show the nearbuy hospitals
        import json

        import requests

        url = "https://trueway-places.p.rapidapi.com/FindPlacesNearby"

        querystring = {"location": "19.076090,72.877426", "type": "hospital", "radius": "9000", "language": "en"}

        headers = {
            "X-RapidAPI-Host": "trueway-places.p.rapidapi.com",
            "X-RapidAPI-Key": "1f62d360a0mshab4da6de118667bp13703cjsn05c591a9a491"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        response1 = response.json()
#this should be printed ob labels of ui page
        l1_1 = response1['results'][0]['name']
        l1_2 = response1['results'][0]['address']
        l1_3 = response1['results'][0]['phone_number']
        l1_4 = response1['results'][0]['distance']

#variables should be rename further....
        l2_1 = response1['results'][1]['name']
        l2_2 = response1['results'][1]['address']
        l1_3 = response1['results'][1]['phone_number']
        l1_4 = response1['results'][1]['distance']

        l1_1 = response1['results'][2]['name']
        l1_2 = response1['results'][2]['address']
        l1_3 = response1['results'][2]['phone_number']
        l1_4 = response1['results'][2]['distance']

        l1_1 = response1['results'][3]['name']
        l1_2 = response1['results'][3]['address']
        l1_3 = response1['results'][3]['phone_number']
        l1_4 = response1['results'][3]['distance']

        l1_1 = response1['results'][4]['name']
        l1_2 = response1['results'][4]['address']
        l1_3 = response1['results'][4]['phone_number']
        l1_4 = response1['results'][4]['distance']

        l1_1 = response1['results'][5]['name']
        l1_2 = response1['results'][5]['address']
        l1_3 = response1['results'][5]['phone_number']
        l1_4 = response1['results'][5]['distance']

        l1_1 = response1['results'][6]['name']
        l1_2 = response1['results'][6]['address']
        l1_3 = response1['results'][6]['phone_number']
        l1_4 = response1['results'][6]['distance']

        l1_1 = response1['results'][7]['name']
        l1_2 = response1['results'][7]['address']
        l1_3 = response1['results'][7]['phone_number']
        l1_4 = response1['results'][7]['distance']

        l1_1 = response1['results'][8]['name']
        l1_2 = response1['results'][8]['address']
        l1_3 = response1['results'][8]['phone_number']
        l1_4 = response1['results'][8]['distance']

        l1_1 = response1['results'][9]['name']
        l1_2 = response1['results'][9]['address']
        l1_3 = response1['results'][9]['phone_number']
        l1_4 = response1['results'][9]['distance']

        l1_1 = response1['results'][10]['name']
        l1_2 = response1['results'][10]['address']
        l1_3 = response1['results'][10]['phone_number']
        l1_4 = response1['results'][10]['distance']

        l1_1 = response1['results'][11]['name']
        l1_2 = response1['results'][11]['address']
        l1_3 = response1['results'][11]['phone_number']
        l1_4 = response1['results'][11]['distance']

        self.labelkanaam.setText(textwrap.fill(l2_1))


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

        # with open("news.json", "w") as outfile:
        #     json.dump(response1, outfile)

        #this labels to be printed on the ui page of medicine search
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


        self.l1.setText(label1_1)
        self.l2.setText(f"<a href=\"{label1_2}\">{label1_2}</a>")
        self.l3.setText(label1_3)






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