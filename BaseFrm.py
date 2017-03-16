from PyQt5 import QtCore, QtWidgets
from MyDialog import Ui_Dialog
from QryBook import *

#The base class for all inventory windows
class Base_Frm(object):
    #The ItemType string parameter specifies which inventory data is being manipulated
    def setupUi(self, Form, ItemType, ExecType):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.itemType = ItemType
        self.execType = ExecType
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(110, 20, 200, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 160, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.execFormOperations(self.pushButton))
        #self.pushButton.clicked.connect(self.ShowDlg)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 15, 80, 31))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 45, 200, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 80, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 73, 200, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(11, 68, 80, 31))
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(110, 102, 200, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 97, 80, 31))
        self.label_4.setObjectName("label_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(110, 131, 200, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 126, 80, 31))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", self.itemType + " Details"))
        self.pushButton.setText(_translate("Form", "Save"))
        self.label.setText(_translate("Form", self.itemType + " Title"))
        if (self.itemType != "Book"):
            self.label.setVisible(False)
            self.lineEdit.setVisible(False)
        self.label_2.setText(_translate("Form", "ISBN"))
        if (self.itemType == "Media") or (self.itemType == "Stationery"):
            self.label_2.setText(_translate("Form", "Type"))
        if (self.itemType == "Computer"):
            self.label_2.setText(_translate("Form", "Manufacturer"))
        self.label_3.setText(_translate("Form", "Author"))
        if (self.itemType == "Media"):
            self.label_3.setText(_translate("Form", "Size(MB)"))
        if (self.itemType == "Stationery"):
            self.label_3.setText(_translate("Form", "Supplier"))
        if (self.itemType == "Computer"):
            self.label_3.setVisible(False)
            self.lineEdit_3.setVisible(False)
        self.label_4.setText(_translate("Form", "Year Published"))
        if (self.itemType == "Media"):
            self.label_4.setText(_translate("Form", "Source"))
        if (self.itemType != "Book") and (self.itemType != "Media"):
            self.label_4.setVisible(False)
            self.lineEdit_4.setVisible(False)
        self.label_5.setText(_translate("Form", "Quantity"))
        if (self.itemType == "Media"):
            self.label_5.setVisible(False)
            self.lineEdit_5.setVisible(False)

    #This method invokes the dialog box the appears after the Save button is clicked
    def ShowDlg(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.exec_()

    #This method executes the SQL insert statements for the Inventory and Book tables
    def execFormOperations(self, b):
        result = False
        if self.execType == "Add":
            if self.itemType == "Book":
                if self.execBookOperations():
                    result = True
        if result:
            self.ShowDlg()

    def execBookOperations(self):
        result = False
        if self.execType == "Add":
            qry = QrBookData()
            if qry.Add(self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(),self.lineEdit_5.text()):
                result = True
        return result


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Base_Frm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

