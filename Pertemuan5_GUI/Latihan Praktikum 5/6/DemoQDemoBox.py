import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainForm(QWidget):
	
	def __init__(self):
		super().__init__()
		self.setupUi()
	
	def setupUi(self):
		self.resize(300, 100)
		self.move(300, 300)
		self.setWindowTitle('Latihan QComboBox')
		
		self.combo1 = QComboBox()
		self.combo1.addItem('--Pilih Makanan--')
		self.combo1.addItem('Mendoan')
		self.combo1.addItem('Cireng')
		self.combo1.addItem('Gethuk')
		self.combo1.addItem('Tahu Bulat')
		self.combo1.addItem('Ketan Susu')
		
		self.combo2 = QComboBox()
		self.combo2.addItem('--Pilih Minuman--')
		self.combo2.addItem('Es Cincau')
		self.combo2.addItem('Milkshake')
		self.combo2.addItem('Chatime')
		self.combo2.addItem('Thaitea')
		self.combo2.addItem('Kopi Hitam')
			
		self.getTextButton = QPushButton('Pilihan Anda')
		
		layout = QVBoxLayout()
		layout.addWidget(self.combo1)
		layout.addWidget(self.combo2)
		layout.addWidget(self.getTextButton)
		layout.addStretch()
		self.setLayout(layout)
		self.getTextButton.clicked.connect(self.getTextButtonClick)
	
	def getTextButtonClick(self):
		QMessageBox.information(self, 'Informasi',
		'Anda memilih: ' + self.combo1.currentText()+ ' & ' + self.combo2.currentText())

if __name__ == '__main__':
	a = QApplication(sys.argv)
	form = MainForm()
	form.show()
	a.exec_()