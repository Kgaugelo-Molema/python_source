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
        new = file.addMenu("New")
        #Menu bar items
        #new.addAction("Book")
        new.addAction("Media")
        new.addAction("Stationery")
        new.addAction("Computer")
        #File|New menu actions
        actionBook = QAction(self)
        actionBook.setObjectName("actionBook")
        actionBook.setText("Book")
        actionBook.setToolTip("Add")
        new.addAction(actionBook)

        update = file.addMenu("Update")
        update.addAction("Media")
        update.addAction("Stationery")
        update.addAction("Computer")
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
