import BookModel
from PyQt5.QtWidgets import *
from PyQt5 import QtGui

def createView(title, model):
    view = QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view

def addrow():
    print(model.rowCount())
    ret=model.insertRows(model.rowCount(), 1)
    print(ret)

def findrow(i):
    delrow=i.row()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    bookModel = BookModel.BookModel()
    model = bookModel.GetModel()
    delrow=-1
    view1 = createView("Table Model (View 1)", model)
    view1.clicked.connect(findrow)
    dlg=QDialog()
    layout = QVBoxLayout()
    layout.addWidget(view1)
    button = QPushButton("Add a row")
    button.clicked.connect(addrow)
    layout.addWidget(button)
    btn1 = QPushButton("del a row")
    btn1.clicked.connect(lambda: model.removeRow(view1.currentIndex().row()))
    layout.addWidget(btn1)
    dlg.setLayout(layout)
    dlg.setWindowTitle("Database Demo")
    dlg.show()
    sys.exit(app.exec_())