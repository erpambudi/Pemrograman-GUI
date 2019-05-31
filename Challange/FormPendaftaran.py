import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class FormPendaftaran(QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi()
	
	def setupUi(self):
		self.resize(350, 200)
		self.move(300, 300)
		self.setWindowTitle('Form Pendaftaran')
		
		self.label1 = QLabel()
		self.label1.setText('<b> Pendaftaran Calon Anggota Avengers </b>')
		
		self.label2 = QLabel()
		self.label2.setText('Nama')
		self.textNama = QLineEdit()
		
		self.label3 = QLabel()
		self.label3.setText('Jenis Kelamin')
		self.cekKelamin1 = QRadioButton()
		self.cekKelamin1.setText('&Laki-Laki')
		self.cekKelamin1.setChecked(True)
		self.cekKelamin2 = QRadioButton()
		self.cekKelamin2.setText('&Perempuan')
		
		self.label4 = QLabel()
		self.label4.setText('Tanggal Lahir')
		self.dateEdit = QDateEdit()
		self.dateEdit.setDisplayFormat('dd/MM/yyyy')
		self.dateEdit.setDate(QDate.currentDate())
		
		self.label5 = QLabel()
		self.label5.setText('Hobi')
		self.combo1 = QComboBox()
		self.combo1.addItem('Basket')
		self.combo1.addItem('Sepak bola')
		self.combo1.addItem('Voli')
		self.combo1.addItem('Catur')
		self.combo1.addItem('Lainnya')
		
		self.label6 = QLabel()
		self.label6.setText('Alamat')
		self.AlamatEdit = QTextEdit()
		
		self.SubmitButton = QPushButton('&Submit')
		self.CancelButton = QPushButton('&Cancel')
		
		layout = QGridLayout()
		layout.addWidget(self.label1, 0, 1, 1, 2)
		layout.addWidget(self.label2, 1, 0)
		layout.addWidget(self.textNama, 1, 1, 1, 2)
		layout.addWidget(self.label3, 2, 0)
		layout.addWidget(self.cekKelamin1, 2, 1,)
		layout.addWidget(self.cekKelamin2, 3, 1,)
		layout.addWidget(self.label4, 4, 0,)
		layout.addWidget(self.dateEdit, 4, 1, 1, 2)
		layout.addWidget(self.label5, 5, 0,)
		layout.addWidget(self.combo1, 5, 1, 1, 2)
		layout.addWidget(self.label6, 6, 0,)
		layout.addWidget(self.AlamatEdit, 6, 1, 1, 2)
		layout.addWidget(self.SubmitButton, 7, 1)
		layout.addWidget(self.CancelButton, 7, 2)
		self.setLayout(layout)
		
		self.SubmitButton.clicked.connect(self.submit)
		self.CancelButton.clicked.connect(self.cancel)
		
	def submit(self):
		nama = str(self.textNama.text())
		ttl = str(self.dateEdit.date().toString())
		hobi = str(self.combo1.currentText())
		alamat = str(self.AlamatEdit.toPlainText())
		
		if self.cekKelamin1.isChecked():
			QMessageBox.information(self, 'Pendaftaran Berhasil',
			'Nama : ' + nama + '\n' +
			'Jenis Kelamin : Laki-Laki\n' +
			'Tanggal Lahir : ' + ttl+ '\n'+
			'Hobi : '+hobi +'\n'+
			'Alamat : '+alamat+'\n') 
		else:
			QMessageBox.information(self, 'Pendaftaran Berhasil',
			'Nama : ' + nama + '\n' +
			'Jenis Kelamin : Perempuan\n' +
			'Tanggal Lahir : ' + ttl + '\n'+
			'Hobi : '+hobi +'\n'+
			'Alamat : '+alamat+'\n')
		
	def cancel(self):
		self.close()
	
	