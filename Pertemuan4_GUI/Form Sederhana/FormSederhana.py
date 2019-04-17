from PyQt5.QtWidgets import QWidget, QLabel

class FormSederhana(QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi()

	def setupUi(self):
		self.resize(500, 200)
		self.move(400, 400)
		self.setWindowTitle('Form Sederhana') #memberi title di form
		
		self.label = QLabel('Menampilkan Tulisan berupa label') #memberi label
		self.label.move(100, 40)
		self.label.setParent(self)
