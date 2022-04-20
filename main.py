import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class Login(QDialog):
	def __init__(self):
		super(Login,self).__init__()
		loadUi("login.ui",self)
		self.loginbutton.clicked.connect(self.loginFunction)
		self.loginPassWord.setEchoMode(QtWidgets.QLineEdit.Password)
		
	def loginFunction(self):
		username=self.loginUserName.text()
		password=self.loginPassWord.text()
		phonepage=PhoneModelPage();
		widget.addWidget(phonepage)
		widget.setCurrentIndex(widget.currentIndex() + 1)
		
		
class PhoneModelPage(QDialog):
	def __init__(self):
		super(PhoneModelPage, self).__init__()
		loadUi("PhoneModelPage.ui", self)
		

app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(470)
widget.setFixedWidth(604)
widget.show()
app.exec_()
