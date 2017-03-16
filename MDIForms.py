import sys

from PyQt5.QtWidgets import *
from BaseFrm import Base_Frm

class MainWindow(QMainWindow):
    count = 0

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        #The menu bar object on the main window
        bar = self.menuBar()
        file = bar.addMenu("File")
        ##########Menu bar items##########
        new = file.addMenu("New")
        #----File|New menu actions----#
        #Book#
        actionBook = QAction(self)
        actionBook.setObjectName("actionBook")
        actionBook.setText("Book")
        actionBook.setToolTip("Add")
        new.addAction(actionBook)
        #Media##
        actionMedia = QAction(self)
        actionMedia.setObjectName("actionMedia")
        actionMedia.setText("Media")
        actionMedia.setToolTip("Add")
        new.addAction(actionMedia)
        #Stationery#
        actionStationery = QAction(self)
        actionStationery.setObjectName("actionStationery")
        actionStationery.setText("Stationery")
        actionStationery.setToolTip("Add")
        new.addAction(actionStationery)
        #Computer#
        actionComputer = QAction(self)
        actionComputer.setObjectName("actionComputer")
        actionComputer.setText("Computer")
        actionComputer.setToolTip("Add")
        new.addAction(actionComputer)
        #--------------------------------------#
        update = file.addMenu("Update")
        #----File|Update menu actions----#
        #Book#
        actionBookEdit = QAction(self)
        actionBookEdit.setObjectName("actionBookEdit")
        actionBookEdit.setText("BookEdit")
        actionBookEdit.setToolTip("Edit")
        update.addAction(actionBookEdit)
        #Media##
        actionMediaEdit = QAction(self)
        actionMediaEdit.setObjectName("actionMediaEdit")
        actionMediaEdit.setText("MediaEdit")
        actionMediaEdit.setToolTip("Edit")
        update.addAction(actionMediaEdit)
        #Stationery#
        actionStationeryEdit = QAction(self)
        actionStationeryEdit.setObjectName("actionStationeryEdit")
        actionStationeryEdit.setText("StationeryEdit")
        actionStationeryEdit.setToolTip("Edit")
        update.addAction(actionStationeryEdit)
        #Computer#
        actionComputerEdit = QAction(self)
        actionComputerEdit.setObjectName("actionComputerEdit")
        actionComputerEdit.setText("ComputerEdit")
        actionComputerEdit.setToolTip("Edit")
        update.addAction(actionComputerEdit)
        #--------------------------------------#
        delete = file.addMenu("Delete")
        delete.addAction("Book")
        delete.addAction("Media")
        delete.addAction("Stationery")
        delete.addAction("Computer")
        exit = file.addAction("Exit")
        view = bar.addMenu("View")
        view.addAction("Cascade")
        view.addAction("Tiled")
        file.triggered[QAction].connect(self.windowaction)
        self.setWindowTitle("Tshwane Library Inventory")

    def windowaction(self, q):
        print("triggered")
        if q.text() == "New":
            self.showDlg()
        if q.text() == "cascade":
            self.mdi.cascadeSubWindows()
        if q.text() == "Tiled":
            self.mdi.tileSubWindows()
        if (q.text() == "Book") or (q.text() == "Media") or (q.text() == "Stationery") or (q.text() == "Computer"):
            self.showForm(q.text(), QAction(q).parent().toolTip())


    #This method invokes all the inventory item maintenance windows
    def showForm(self, ItemType, ExecType):
        MainWindow.count = MainWindow.count + 1
        Form = QWidget()
        ui = Base_Frm()
        ui.setupUi(Form, ItemType, ExecType)
        self.mdi.addSubWindow(Form)
        Form.show()

def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
