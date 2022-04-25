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



def set_first_row(tableWidget, row):
	i = 0
	for item in row:
		tableWidget.setItem(0, i, QtWidgets.QTableWidgetItem(str(item)))
		i += 1


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
		self.tableWidget.setColumnWidth(0, 150)
		self.tableWidget.setColumnWidth(1, 195)
		self.phoneFinderStores.clicked.connect(self.storeFunction)
		self.phoneFinderAccess.clicked.connect(self.accessFunction)
		self.phoneFinderSpecs.clicked.connect(self.specsFunction)
		self.phoneFinderScreen.clicked.connect(self.screenFunction)
		self.phoneFindButton.clicked.connect(self.findPhoneFunction)
		self.phoneSignOut.clicked.connect(self.SignOutFunction)

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
		global storepage
		global phoneNameModel
		if storeBool == False:
			storeIndex = trackerIndex + 1
			trackerIndex += 1
			storeBool = True
			storepage = StorePage()
			widget.addWidget(storepage)
		
		widget.setCurrentIndex(storeIndex)
		tablerow = 0
		storepage.storeTableWidget.setRowCount(0)
		storepage.storeTableWidget.setRowCount(10)
		for row in db.exec(f"SELECT Store.StoreNameID, StoreName, Address, City, State, Price FROM Store, SoldAt WHERE SoldAt.SoldAtModelNumber = '{phoneNameModel}' AND SoldAt.storeNameID = Store.storeNameID"):
			storepage.storeTableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
			storepage.storeTableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
			storepage.storeTableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
			storepage.storeTableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
			storepage.storeTableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
			storepage.storeTableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
			tablerow+=1
			
			

	def accessFunction(self):
		global accessoriesBool
		global trackerIndex
		global accessoriesIndex
		global accesspage
		if not accessoriesBool:
			accessoriesIndex = trackerIndex + 1
			trackerIndex += 1
			accessoriesBool = True
			accesspage = AccessoriesPage()
			widget.addWidget(accesspage)
		widget.setCurrentIndex(accessoriesIndex)
		row = db.exec_single_row(2, f"select HasCase, ScreenProtector from Accessories where ModelNumber = '{phoneNameModel}'")
		set_first_row(accesspage.accesstableWidget, row)

	def specsFunction(self):
		global specsBool
		global trackerIndex
		global specsIndex
		global specspage
		localSpecBool = specsBool
		if specsBool == False:
			specsIndex = trackerIndex + 1
			trackerIndex += 1
			specsBool = True
			specspage = SpecsPage()
			widget.addWidget(specspage)
		widget.setCurrentIndex(specsIndex)
		row = db.exec_single_row(6, f"select Storage, Dimensions, BatteryLife, Weight, Color, Cpu from Specs where ModelNumber = '{phoneNameModel}'")
		set_first_row(specspage.tableWidget, row)

	def screenFunction(self):
		global screenBool
		global screenIndex
		global trackerIndex
		global screenpage
		if screenBool == False:
			screenIndex = trackerIndex + 1
			trackerIndex += 1
			screenBool = True
			screenpage = ScreenPage()
			widget.addWidget(screenpage)
		widget.setCurrentIndex(screenIndex)
		global phoneNameModel
		row = db.exec_single_row(3, f"select ScreenType, Resolution, AspectRatio from ScreenType where ModelNumber = '{phoneNameModel}'")
		set_first_row(screenpage.screentableWidget, (phoneNameModel, *row))
		
	def SignOutFunction(self):
		widget.setCurrentIndex(0)


class StorePage(QDialog):
	def __init__(self):
		super(StorePage, self).__init__()
		loadUi("Stores.ui", self)
		self.storeTableWidget.setColumnWidth(0, 100)
		self.storeTableWidget.setColumnWidth(1, 100)
		self.storeTableWidget.setColumnWidth(2, 235)
		self.storeTableWidget.setColumnWidth(3, 150)
		self.storeTableWidget.setColumnWidth(4, 150)
		self.storeTableWidget.setColumnWidth(5, 87)
		self.storeBackButton.clicked.connect(self.backButton)

	def backButton(self):
		global phoneIndex
		widget.setCurrentIndex(phoneIndex)


class AccessoriesPage(QDialog):
	def __init__(self):
		super(AccessoriesPage, self).__init__()
		loadUi("Accessories.ui", self)
		self.accesstableWidget.setColumnWidth(0, 265)
		self.accesstableWidget.setColumnWidth(1, 260)
		self.accessoriesBackButton.clicked.connect(self.backButton)

	def backButton(self):
		global phoneIndex
		widget.setCurrentIndex(phoneIndex)


class SpecsPage(QDialog):
	def __init__(self):
		super(SpecsPage, self).__init__()
		loadUi("Specs.ui", self)
		self.tableWidget.setColumnWidth(0, 100)
		self.tableWidget.setColumnWidth(1, 150)
		self.tableWidget.setColumnWidth(2, 100)
		self.tableWidget.setColumnWidth(3, 150)
		self.tableWidget.setColumnWidth(4, 150)
		self.tableWidget.setColumnWidth(5, 178)
		self.specsBackButton.clicked.connect(self.backButton)

	def backButton(self):
		global phoneIndex
		widget.setCurrentIndex(phoneIndex)


class ScreenPage(QDialog):
	def __init__(self):
		super(ScreenPage, self).__init__()
		loadUi("Screen.ui", self)
		self.screentableWidget.setColumnWidth(0, 150)
		self.screentableWidget.setColumnWidth(1, 150)
		self.screentableWidget.setColumnWidth(2, 250)
		self.screentableWidget.setColumnWidth(3, 185)
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
