from PyQt5.QtWidgets import (QWidget, QPushButton, QToolTip)
from PyQt5.QtGui import QFont

class ToolTip(QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi()

	def setupUi(self):
		self.resize(400, 300)
		self.move(300, 300)
		self.setWindowTitle('Latihan Menampilkan Tooltip')
		QToolTip.setFont(QFont('SansSerif',12))
		self.setToolTip('ini adalah <i>Tooltip</i> untuk <b>form</b>')
		
		self.button = QPushButton('Other Form')
		self.button.move(160, 100)
		self.button.setParent(self)
		self.button.setToolTip('''<font color=red>Tombol untuk membuka</font>
		<b>Form Lain</b>''')
		
		self.button.clicked.connect(self.buttonClick)
		self.button = QPushButton('Keluar')
		self.button.move(160, 150)
		self.button.setParent(self)
		self.button.setToolTip('''<font color=blue>Tombol untuk</font>
		<b>Keluar</b>''')
		self.button.clicked.connect(self.buttonClick)

	def buttonClick(self):
		self.close()
