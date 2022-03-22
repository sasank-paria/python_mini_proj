import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap
#-------------------------------------------------------------------------------------------------------------------------

class homepage(QMainWindow):
    def __init__(self):
        super(homepage,self).__init__()
        uic.loadUi("homepage.ui",self)
        self.get_vaccinated.clicked.connect(self.gotoslotfinder)
        self.hospital_finder.clicked.connect(self.gotohospital)
        self.medicine_search.clicked.connect(self.gotomedicine)

    def gotohospital(self):
        from hospital_finder_py import hospital_finder
        h=hospital_finder()
        widget.close()

    def gotoslotfinder(self):
            from vaccine_slot_finder_py import vaccine_slot_finder
            v=vaccine_slot_finder()
            widget.close()

    def gotomedicine(self):
        from medicine_search import medicine_search
        m=medicine_search()
        widget.close()




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
