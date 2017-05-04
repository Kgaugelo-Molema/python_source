# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ToolboxExample.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ToolBox(object):
    def setupUi(self, ToolBox):
        ToolBox.setObjectName("ToolBox")
        ToolBox.resize(605, 467)
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 605, 413))
        self.page.setObjectName("page")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(30, 0, 75, 23))
        self.pushButton.setObjectName("pushButton")
        ToolBox.addItem(self.page, "")
        self.page1 = QtWidgets.QWidget()
        self.page1.setGeometry(QtCore.QRect(0, 0, 605, 413))
        self.page1.setObjectName("page1")
        self.pushButton_2 = QtWidgets.QPushButton(self.page1)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 0, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        ToolBox.addItem(self.page1, "")

        self.retranslateUi(ToolBox)
        ToolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(ToolBox)

    def retranslateUi(self, ToolBox):
        _translate = QtCore.QCoreApplication.translate
        ToolBox.setWindowTitle(_translate("ToolBox", "ToolBox"))
        self.pushButton.setText(_translate("ToolBox", "PushButton"))
        ToolBox.setItemText(ToolBox.indexOf(self.page), _translate("ToolBox", "Page 1"))
        self.pushButton_2.setText(_translate("ToolBox", "PushButton"))
        ToolBox.setItemText(ToolBox.indexOf(self.page1), _translate("ToolBox", "Page 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ToolBox = QtWidgets.QToolBox()
    ui = Ui_ToolBox()
    ui.setupUi(ToolBox)
    ToolBox.show()
    sys.exit(app.exec_())

