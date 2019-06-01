import sys

from designNama import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainForm(QWidget):
	def __init__ (self,parent = None):
		QDialog.__init__(self,parent)
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		self.ui.halo.clicked.connect(self.haloClicked)
	
	def haloClicked(self):
		QMessageBox.information(self,' Demo QtDesigner', ' Hallo %s , apa kabar?' %self.ui.namaTxt.text())

if __name__ =='__main__':
	a = QApplication(sys.argv)
	form = MainForm()
	form.show()
	a.exec_()