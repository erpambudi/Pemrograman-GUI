# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DesignNama.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 341)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 100, 421, 20))
        self.label.setObjectName("label")
        self.namaTxt = QtWidgets.QLineEdit(Form)
        self.namaTxt.setGeometry(QtCore.QRect(100, 130, 471, 21))
        self.namaTxt.setObjectName("namaTxt")
        self.halo = QtWidgets.QPushButton(Form)
        self.halo.setGeometry(QtCore.QRect(160, 170, 75, 23))
        self.halo.setObjectName("halo")
        self.exit = QtWidgets.QPushButton(Form)
        self.exit.setGeometry(QtCore.QRect(490, 290, 75, 23))
        self.exit.setObjectName("exit")
        self.clear = QtWidgets.QPushButton(Form)
        self.clear.setGeometry(QtCore.QRect(240, 170, 75, 23))
        self.clear.setObjectName("clear")

        self.retranslateUi(Form)
        self.exit.clicked.connect(Form.close)
        self.clear.clicked.connect(self.namaTxt.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Masukan Nama Anda : </span></p></body></html>"))
        self.halo.setText(_translate("Form", "Halo"))
        self.exit.setText(_translate("Form", "Exit"))
        self.clear.setText(_translate("Form", "Clear"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
