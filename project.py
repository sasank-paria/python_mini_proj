import sys
import textwrap

import self
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
        self.news_button_homepage.clicked.connect(self.gotonews)
        self.graph_button.clicked.connect(self.gotograph)

        #covid vaccine stats
        import requests
        import lxml
        from bs4 import BeautifulSoup

        url = " https://www.mohfw.gov.in/"
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9"
        }

        response = requests.get(url, headers=header)

        soup = BeautifulSoup(response.content, "lxml")
        # print(soup.prettify())

        price = soup.find(class_="coviddata").get_text()
        self.label_35.setText(price)





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

    def gotonews(self):
        n=news()
        widget.addWidget(n)
        widget.setCurrentIndex(widget.currentIndex() + 1)



    def gotohospital(self):

        h=hospital_finder()
        widget.addWidget(h)
        widget.setCurrentIndex(widget.currentIndex() + 1)


    def gotoslotfinder(self):
        import Vaccine_Availability_Checker

    def gotograph(self):
        # iska code ui ka saath connect ho gya main project me

        import json

        import pandas
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
        # with open("coviddata.json","w") as file:
        #     json.dump(response1,file)

        # print(response1)
        p1 = response1['response'][0]['country']
        p2 = response1['response'][0]['population']
        p3 = response1['response'][0]['cases']['active']
        p4 = response1['response'][0]['cases']['critical']
        p5 = response1['response'][0]['cases']['recovered']
        p6 = response1['response'][0]['cases']['total']
        p7 = response1['response'][0]['deaths']['total']
        p8 = response1['response'][0]['day']
        p9 = response1['response'][0]['time']

        # self.l1.setText(p1)
        # self.l2.setText(p2)
        # self.l3.setText(p3)
        # self.l4.setText(p4)
        # self.l5.setText(p5)
        # self.l6.setText(p6)
        # self.l7.setText(p7)
        # self.l8.setText(p8)
        # self.l9.setText(p9)

        data = pandas.Series(response1)
        # print(data)

        import matplotlib.pyplot as plt
        import numpy as np

        # y = np.array([p7, p5, p4, p3])
        # mylabels = ["deaths", "recovered", "critical", "active"]
        #
        # plt.pie(y, labels = mylabels)
        #
        # plt.show()
        #

        x = np.array(["deaths", "recovered", "critical", "active"])
        y = np.array([p7, p5, p4, p3])

        plt.bar(x, y)
        plt.show()




    def gotomedicine(self):

        m=medicine_search()
        widget.addWidget(m)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class hospital_finder(QMainWindow):
    def __init__(self):
        super(hospital_finder,self).__init__()
        uic.loadUi("hospital_finder.ui",self)
        self.home_hf.clicked.connect(self.gotohome)
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
        import json
        import textwrap

        import requests

        url = "https://trueway-places.p.rapidapi.com/FindPlacesNearby"

        querystring = {"location": "19.076090,72.877426", "type": "hospital", "radius": "9000", "language": "en"}

        headers = {
            "X-RapidAPI-Host": "trueway-places.p.rapidapi.com",
            "X-RapidAPI-Key": "1f62d360a0mshab4da6de118667bp13703cjsn05c591a9a491"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        response1 = response.json()
        try:
            #this should be printed ob labels of ui page
            l1_1 = response1['results'][0]['name']

            l1_2 = response1['results'][0]['address']
            l1_3 = response1['results'][0]['phone_number']
           # l1_4 = response1['results'][0]['distance']

            self.la_2.setText(l1_1)
            self.la_3.setText(textwrap.fill(l1_2))
            self.la_4.setText(l1_3)
            #self.la_5.setText(l1_4)
        except:
            print("error in api")

#variables should be rename further....
        try:
            l2_1 = response1['results'][1]['name']
            l2_2 = response1['results'][1]['address']
            l2_3 = response1['results'][1]['phone_number']
          #  l2_4 = response1['results'][1]['distance']
            self.la_10.setText(l2_1)
            self.la_11.setText(textwrap.fill(l2_2))
            self.la_12.setText(l2_3)
           # self.la_13.setText(l2_4)
        except:
            print("error in api")

        try:
            l3_1 = response1['results'][2]['name']
            l3_2 = response1['results'][2]['address']
            l3_3 = response1['results'][2]['phone_number']
           # l3_4 = response1['results'][2]['distance']
            self.la_18.setText(l3_1)
            self.la_19.setText(textwrap.fill(l3_2))
            self.la_20.setText(l3_3)
           # self.la_21.setText(l3_4)
        except:
            print("error in api")

        try:
            l4_1 = response1['results'][3]['name']
            l4_2 = response1['results'][3]['address']
            l4_3 = response1['results'][3]['phone_number']
          #  l4_4 = response1['results'][3]['distance']
            self.la_26.setText(l4_1)
            self.la_27.setText(textwrap.fill(l4_2))
            self.la_28.setText(l4_3)
          #  self.la_29.setText(l4_4)
        except:
            print("error in api")

        try:
            l5_1 = response1['results'][4]['name']
            l5_2 = response1['results'][4]['address']
            l5_3 = response1['results'][4]['phone_number']
         #   l5_4 = response1['results'][4]['distance']
            self.la_34.setText(l5_1)
            self.la_35.setText(textwrap.fill(l5_2))
            self.la_36.setText(l5_3)
         #   self.la_37.setText(l5_4)
        except:
            print("error in api")

        try:
            l6_1 = response1['results'][5]['name']
            l6_2 = response1['results'][5]['address']
            l6_3 = response1['results'][5]['phone_number']
          #  l6_4 = response1['results'][5]['distance']
            self.la_42.setText(l6_1)
            self.la_43.setText(textwrap.fill(l6_2))
            self.la_44.setText(l6_3)
          #  self.la_45.setText(l6_4)
        except:
            print("error in api")

        try:
            l7_1 = response1['results'][6]['name']
            l7_2 = response1['results'][6]['address']
            l7_3 = response1['results'][6]['phone_number']
      #      l7_4 = response1['results'][6]['distance']

            self.la_6.setText(l7_1)
            self.la_7.setText(textwrap.fill(l7_2))
            self.la_8.setText(l7_3)
        #    self.la_9.setText(l7_4)
        except:
            print("error in api")

        try:
            l8_1 = response1['results'][7]['name']
            l8_2 = response1['results'][7]['address']
            l8_3 = response1['results'][7]['phone_number']
        #    l8_4 = response1['results'][7]['distance']
            self.la_14.setText(l8_1)
            self.la_15.setText(textwrap.fill(l8_2))
            self.la_16.setText(l8_3)
        #    self.la_17.setText(l8_4)
        except:
            print("error in api")

        try:
            l9_1 = response1['results'][8]['name']
            l9_2 = response1['results'][8]['address']
            l9_3 = response1['results'][8]['phone_number']
         #   l9_4 = response1['results'][8]['distance']
            self.la_22.setText(l9_1)
            self.la_23.setText(textwrap.fill(l9_2))
            self.la_24.setText(l9_3)
          #  self.la_25.setText(l9_4)
        except:
            print("error in api")

        try:
            l10_1 = response1['results'][9]['name']
            l10_2 = response1['results'][9]['address']
            l10_3 = response1['results'][9]['phone_number']
         #   l10_4 = response1['results'][9]['distance']
            self.la_30.setText(l10_1)
            self.la_31.setText(textwrap.fill(l10_2))
            self.la_32.setText(l10_3)
          #  self.la_33.setText(l10_4)
        except:
            print("error in api")

        try:
            l11_1 = response1['results'][10]['name']
            l11_2 = response1['results'][10]['address']
            l11_3 = response1['results'][10]['phone_number']
        #    l11_4 = response1['results'][10]['distance']
            self.la_38.setText(l11_1)
            self.la_39.setText(textwrap.fill(l11_2))
            self.la_40.setText(l11_3)
          #  self.la_41.setText(l11_4)
        except:
            print("error in api")

        try:
            l12_1 = response1['results'][11]['name']
            l12_2 = response1['results'][11]['address']
            l12_3 = response1['results'][11]['phone_number']
       #     l12_4 = response1['results'][11]['distance']

            self.la_46.setText(l12_1)
            self.la_47.setText(textwrap.fill(l12_2))
            self.la_48.setText(l12_3)
         #   self.la_49.setText(l12_4)
        except:
            print("error in api")






















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

        '''label7_1 = response1['results'][6]["title"]
        label7_2 = response1['results'][6]["link"]
        label7_3 = response1['results'][6]["description"]'''

        self.l1_10.setText(label1_1)
        self.l2_9.setText(f"<a href=\"{label1_2}\">{label1_2}</a>")
        self.l1_8.setText(label1_3)

        self.label1_18.setText(label2_1)
        self.label1_17.setText(f"<a href=\"{label2_2}\">{label2_2}</a>")
        self.label1_16.setText(label2_3)

        self.label1_7.setText(label3_1)
        self.label1_6.setText(f"<a href=\"{label3_2}\">{label3_2}</a>")
        self.label1_5.setText(label3_3)

        self.label1_15.setText(label4_1)
        self.label1_14.setText(f"<a href=\"{label4_2}\">{label4_2}</a>")
        self.label1_13.setText(label4_3)

        self.l3.setText(label5_1)
        self.l2.setText(f"<a href=\"{label5_2}\">{label5_2}</a>")
        self.l1.setText(label5_3)

        self.label1_12.setText(label6_1)
        self.label1_11.setText(f"<a href=\"{label6_2}\">{label6_2}</a>")
        self.label1_2.setText(label6_3)











class news(QMainWindow):
    def __init__(self):
        super(news,self).__init__()
        uic.loadUi("news.ui",self)
        self.home_news_button.clicked.connect(self.gotohome)

    #display of news api on ui

        import requests
        import json
        url = "https://bing-news-search1.p.rapidapi.com/news"

        querystring = {"count": "12", "category": "Health", "mkt": "en-GB", "safeSearch": "Off", "textFormat": "Raw"}

        headers = {
            "X-BingApis-SDK": "true",
            "X-RapidAPI-Host": "bing-news-search1.p.rapidapi.com",
            "X-RapidAPI-Key": "1f62d360a0mshab4da6de118667bp13703cjsn05c591a9a491"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        response1 = response.json()

        # with open("news.json","w") as file:
        # 	json.dump(response1,file)

        # print(response1)

        p2 = response1['value'][0]['name']
        p3 = response1['value'][0]['url']

        p4 = response1['value'][1]['name']
        p5 = response1['value'][1]['url']

        p6 = response1['value'][2]['name']
        p7 = response1['value'][2]['url']

        p8 = response1['value'][3]['name']
        p9 = response1['value'][3]['url']

        p10 = response1['value'][4]['name']
        p11 = response1['value'][4]['url']

        p12 = response1['value'][5]['name']
        p13 = response1['value'][5]['url']

        p14 = response1['value'][6]['name']
        p15 = response1['value'][6]['url']

        p16 = response1['value'][7]['name']
        p17 = response1['value'][7]['url']

        p18 = response1['value'][8]['name']
        p19 = response1['value'][8]['url']

        p20 = response1['value'][9]['name']
        p21 = response1['value'][9]['url']

        p22 = response1['value'][10]['name']
        p23 = response1['value'][10]['url']

        p24 = response1['value'][11]['name']
        p25 = response1['value'][11]['url']



        self.l1_2.setText(p2)
        self.label_5.setText(f"<a href=\"{p3}\">{p3}</a>")

        self.l3_2.setText(p4)
        self.l4.setText(f"<a href=\"{p5}\">{p5}</a>")

        self.l5.setText(p6)
        self.l6.setText(f"<a href=\"{p7}\">{p7}</a>")

        self.l7.setText(p8)
        self.l8.setText(f"<a href=\"{p9}\">{p9}</a>")

        self.l9.setText(p10)
        self.l10.setText(f"<a href=\"{p11}\">{p11}</a>")

        self.l11.setText(p12)
        self.l12.setText(f"<a href=\"{p13}\">{p13}</a>")

        self.l13.setText(p14)
        self.l14.setText(f"<a href=\"{p15}\">{p15}</a>")

        self.l15.setText(p16)
        self.l16.setText(f"<a href=\"{p17}\">{p17}</a>")

        self.l17.setText(p18)
        self.l18.setText(f"<a href=\"{p19}\">{p19}</a>")

        self.l19.setText(p20)
        self.l20.setText(f"<a href=\"{p21}\">{p21}</a>")

        self.l21.setText(p22)
        self.l22.setText(f"<a href=\"{p23}\">{p23}</a>")

        self.l23.setText(p24)
        self.l24.setText(f"<a href=\"{p25}\">{p25}</a>")




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