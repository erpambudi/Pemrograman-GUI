import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainForm(QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi()
	
	def setupUi(self):
		self.resize(400, 150)
		self.move(300, 300)
		self.setWindowTitle('Tugas QRadioButton')
		
		self.label1 = QLabel()
		self.label1.setText('Bilangan pertama\t')
		self.phoneEdit1 = QLineEdit()
		hbox1 = QHBoxLayout()
		hbox1.addWidget(self.label1)
		hbox1.addWidget(self.phoneEdit1)
		
		self.label2 = QLabel()
		self.label2.setText('Bilangan kedua\t')
		self.phoneEdit2 = QLineEdit()
		hbox2 = QHBoxLayout()
		hbox2.addWidget(self.label2)
		hbox2.addWidget(self.phoneEdit2)
		
		self.tambah = QRadioButton()
		self.tambah.setText('&Tambah')
		self.tambah.setChecked(True)
		self.kurang = QRadioButton()
		self.kurang.setText('&Kurang')
		self.kali = QRadioButton()
		self.kali.setText('&Kali')
		self.bagi = QRadioButton()
		self.bagi.setText('&Bagi')
		hbox3 = QHBoxLayout()
		hbox3.addWidget(self.tambah)
		hbox3.addWidget(self.kurang)
		hbox3.addWidget(self.kali)
		hbox3.addWidget(self.bagi)
		
		self.resultLabel = QLabel()
		self.resultLabel.setText('<b> Hasil Penjumlahan : </b>')
		self.hitungButton = QPushButton('Hitung')
		vbox = QVBoxLayout()
		vbox.addWidget(self.resultLabel)
		vbox.addWidget(self.hitungButton)
		
		layout = QVBoxLayout()
		layout.addLayout(hbox1)
		layout.addLayout(hbox2)
		layout.addLayout(hbox3)
		horizontalLine1 = QFrame()
		horizontalLine1.setFrameShape(QFrame.HLine)
		horizontalLine1.setFrameShadow(QFrame.Sunken)
		layout.addWidget(horizontalLine1)
		layout.addLayout(vbox)
		layout.addStretch()
		self.setLayout(layout)
		
		self.hitungButton.clicked.connect(self.checkButtonClick)
	
	def checkButtonClick(self):
		if self.tambah.isChecked():
			jumlah = self.phoneEdit1.text() + self.phoneEdit2.text()
			self.resultLabel.setText('<b>Hasil Penjumlahan : </b>'+ jumlah)
		elif self.kurang.isChecked():
			self.resultLabel.setText('<b>Hasil Pengurangan : </b>')
		elif self.kali.isChecked():
			self.resultLabel.setText('<b>Hasil Perkalian : </b>')
		elif self.bagi.isChecked():
			self.resultLabel.setText('<b>Hasil Pembagian : </b>')
		
if __name__ == '__main__':
	a = QApplication(sys.argv)
	form = MainForm()
	form.show()
	a.exec_()
