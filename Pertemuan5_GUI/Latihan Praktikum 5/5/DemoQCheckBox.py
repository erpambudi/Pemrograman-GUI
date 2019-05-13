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
		self.setWindowTitle(' ')
		
		self.titleCheck = QCheckBox()
		self.titleCheck.setText('Show Title')
	
		hbox1 = QHBoxLayout()
		hbox1.addWidget(self.titleCheck)
		
		layout = QVBoxLayout()
		layout.addLayout(hbox1)
		self.setLayout(layout)
		
		self.titleCheck.clicked.connect(self.setTitle)
		
	def setTitle(self):
		if self.titleCheck.isChecked(): self.setWindowTitle('Contoh QCheckBox')
		else: self.setWindowTitle(' ')
			
if __name__ == '__main__':
	a = QApplication(sys.argv)
	
	form = MainForm()
	form.show()
	
	a.exec_()
