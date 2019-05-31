import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from FormPendaftaran import *

class MainForm(QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi()
	
	def setupUi(self):
		self.resize(300, 100)
		self.move(300, 300)
		self.setWindowTitle('Kuis Pemrograman GUI')
		
		self.label1 = QLabel()
		self.label1.setText('Username')
		self.textUser = QLineEdit()
		
		self.label2 = QLabel()
		self.label2.setText('Password')
		self.textPswd = QLineEdit()
		
		self.loginButton = QPushButton('&Login')
		self.clearButton = QPushButton('&Clear')
		
		layout = QGridLayout()
		layout.addWidget(self.label1, 0, 0)
		layout.addWidget(self.textUser, 0, 1, 1, 2)
		layout.addWidget(self.label2, 1, 0)
		layout.addWidget(self.textPswd, 1, 1, 1, 2)
		layout.addWidget(self.loginButton, 2, 1)
		layout.addWidget(self.clearButton, 2, 2)
		self.setLayout(layout)
		
		self.loginButton.clicked.connect(self.masuk)
		self.clearButton.clicked.connect(self.hapus)
		
	def masuk(self):
		user = self.textUser.text()
		pw = self.textPswd.text()
		
		if not user or not pw :
			QMessageBox.information(self,'Perhatian','Username atau password tidak boleh kosong')
		else:
			if user == '17104032' and pw =='erpam':
				self.form = FormPendaftaran()
				self.form.show()
				self.close()
			else:
				QMessageBox.information(self,'Perhatian','Username atau password Salah') 
	
	def hapus(self):
		self.textUser.clear()
		self.textPswd.clear()

if __name__ == '__main__':
	a = QApplication(sys.argv)
	form = MainForm()
	form.show()
	a.exec_()