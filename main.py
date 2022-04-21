import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

from DataBase import DataBase

storeIndex = 0
accessoriesIndex = 0
specsIndex = 0
screenIndex = 0
phoneIndex = 1
loginIndex = 0
trackerIndex = 1
phoneNameModel = ""

storeBool = False
accessoriesBool = False
specsBool = False
screenBool = False


class Login(QDialog):
	def __init__(self):
		super(Login, self).__init__()
		loadUi("login.ui", self)
		self.loginbutton.clicked.connect(self.loginFunction)
		self.loginPassWord.setEchoMode(QtWidgets.QLineEdit.Password)

	def loginFunction(self):
		# make sure to do a if statement checking if user & pass are good if not try again
		username = self.loginUserName.text()
		password = self.loginPassWord.text()
		actual_password = db.exec_single_value(f"select Password from PhoneFinder where UserName = '{username}'")
		# print(actual_password)
		if password == actual_password:
			phonepage = PhoneModelPage()
			widget.addWidget(phonepage)
			widget.setCurrentIndex(widget.currentIndex() + 1)


class PhoneModelPage(QDialog):
	def __init__(self):
		super(PhoneModelPage, self).__init__()
		loadUi("PhoneModelPage.ui", self)
		self.phoneFinderStores.clicked.connect(self.storeFunction)
		self.phoneFinderAccess.clicked.connect(self.accessFunction)
		self.phoneFinderSpecs.clicked.connect(self.specsFunction)
		self.phoneFinderScreen.clicked.connect(self.screenFunction)
		self.phoneFindButton.clicked.connect(self.findPhoneFunction)

	def findPhoneFunction(self):
		global phoneNameModel
		phoneName = self.phoneNameText.text()
		getPhoneModel, getManufacture = db.exec_single_row(2, f"select ModelNumber, Manufacturer from PhoneModel where PhoneName = '{phoneName}'")
		# getPhoneModel, getManufacture = db.exec_single_row(f"select ModelNumber, Manufacturer from PhoneModel where substring(PhoneName, 0, {len(phoneName)}) = '{phoneName}'")
		if getPhoneModel is not None and getManufacture is not None:
			phoneNameModel = getPhoneModel
			self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(getPhoneModel))
			self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(getManufacture))

	def storeFunction(self):
		global storeBool
		global storeIndex
		global trackerIndex
		if storeBool == False:
			storeIndex = trackerIndex + 1
			trackerIndex += 1
			storeBool = True
		storepage = StorePage()
		widget.addWidget(storepage)
		widget.setCurrentIndex(storeIndex)

	def accessFunction(self):
		global accessoriesBool
		global trackerIndex
		global accessoriesIndex
		if accessoriesBool == False:
			accessoriesIndex = trackerIndex + 1
			trackerIndex += 1
			accessoriesBool = True

		accesspage = AccessoriesPage()
		widget.addWidget(accesspage)
		widget.setCurrentIndex(accessoriesIndex)

	def specsFunction(self):
		global specsBool
		global trackerIndex
		global specsBool
		localSpecBool = specsBool
		if specsBool == False:
			specsIndex = trackerIndex + 1
			trackerIndex += 1
			specsBool = True

		specspage = SpecsPage()
		widget.addWidget(specspage)
		widget.setCurrentIndex(specsIndex)

	def screenFunction(self):
		global screenBool
		global screenIndex
		global trackerIndex
		if screenBool == False:
			screenIndex = trackerIndex + 1
			trackerIndex += 1
			screenBool = True
		screenpage = ScreenPage()
		widget.addWidget(screenpage)
		widget.setCurrentIndex(screenIndex)


class StorePage(QDialog):
	def __init__(self):
		super(StorePage, self).__init__()
		loadUi("Stores.ui", self)
		self.tableWidget.setColumnWidth(0, 250)
		self.tableWidget.setColumnWidth(1, 250)
		self.tableWidget.setColumnWidth(2, 400)
		self.tableWidget.setColumnWidth(3, 300)
		self.tableWidget.setColumnWidth(4, 250)
		self.tableWidget.setColumnWidth(5, 250)
		self.storeBackButton.clicked.connect(self.backButton)

	def backButton(self):
		global phoneIndex
		widget.setCurrentIndex(phoneIndex)


class AccessoriesPage(QDialog):
	def __init__(self):
		super(AccessoriesPage, self).__init__()
		loadUi("Accessories.ui", self)
		self.accessoriesBackButton.clicked.connect(self.backButton)

	def backButton(self):
		global phoneIndex
		widget.setCurrentIndex(phoneIndex)


class SpecsPage(QDialog):
	def __init__(self):
		super(SpecsPage, self).__init__()
		loadUi("Specs.ui", self)
		self.specsBackButton.clicked.connect(self.backButton)

	def backButton(self):
		global phoneIndex
		widget.setCurrentIndex(phoneIndex)


class ScreenPage(QDialog):
	def __init__(self):
		super(ScreenPage, self).__init__()
		loadUi("Screen.ui", self)
		self.screenBackButton.clicked.connect(self.backButton)

	def backButton(self):
		global phoneIndex
		widget.setCurrentIndex(phoneIndex)


db = DataBase(host='/tmp', port=8888, db_name='PhoneFinderDB')
db.start()
db.exec_file('CreateTables.sql')
db.exec_file('InsertTestData.sql')
app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1000)
widget.setFixedHeight(800)
widget.show()
app.exec_()
db.stop()
