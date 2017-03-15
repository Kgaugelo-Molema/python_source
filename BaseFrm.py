from PyQt5 import QtCore, QtWidgets
from MyDialog import Ui_Dialog
import QryBook

#The base class for all inventory windows
class Base_Frm(object):
    #The ItemType string parameter specifies which inventory data is being manipulated
    def setupUi(self, Form, ItemType):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(110, 20, 200, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 160, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.addBook(self.pushButton))
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

        self.retranslateUi(Form, ItemType)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form, ItemType):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", ItemType + " Details"))
        self.pushButton.setText(_translate("Form", "Save"))
        self.label.setText(_translate("Form", ItemType + " Title"))
        if (ItemType != "Book"):
            self.label.setVisible(False)
            self.lineEdit.setVisible(False)
        self.label_2.setText(_translate("Form", "ISBN"))
        if (ItemType == "Media") or (ItemType == "Stationery"):
            self.label_2.setText(_translate("Form", "Type"))
        if (ItemType == "Computer"):
            self.label_2.setText(_translate("Form", "Manufacturer"))
        self.label_3.setText(_translate("Form", "Author"))
        if (ItemType == "Media"):
            self.label_3.setText(_translate("Form", "Size(MB)"))
        if (ItemType == "Stationery"):
            self.label_3.setText(_translate("Form", "Supplier"))
        if (ItemType == "Computer"):
            self.label_3.setVisible(False)
            self.lineEdit_3.setVisible(False)
        self.label_4.setText(_translate("Form", "Year Published"))
        if (ItemType == "Media"):
            self.label_4.setText(_translate("Form", "Source"))
        if (ItemType != "Book") and (ItemType != "Media"):
            self.label_4.setVisible(False)
            self.lineEdit_4.setVisible(False)
        self.label_5.setText(_translate("Form", "Quantity"))
        if (ItemType == "Media"):
            self.label_5.setVisible(False)
            self.lineEdit_5.setVisible(False)

    #This method invokes the dialog box the appears after the Save button is clicked
    def ShowDlg(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.exec_()

    #This method executes the SQL insert statements for the Inventory and Book tables
    def addBook(self, b):
        if QryBook.Add(self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(), self.lineEdit_5.text()):
            self.ShowDlg()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Base_Frm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

