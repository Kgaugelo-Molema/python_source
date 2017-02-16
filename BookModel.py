from PyQt5 import QtSql, QtCore
import SQLiteLayer

class BookModel(object):
    def GetModel(self):
        db = SQLiteLayer.getDB()
        model = QtSql.QSqlTableModel()
        model.setTable('book')
        model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        model.select()
        model.setHeaderData(0, QtCore.Qt.Horizontal, "title")
        model.setHeaderData(1, QtCore.Qt.Horizontal, "isbn")
        model.setHeaderData(2, QtCore.Qt.Horizontal, "author")
        model.setHeaderData(3, QtCore.Qt.Horizontal, "year")
        model.setHeaderData(4, QtCore.Qt.Horizontal, "qty")
        model.setHeaderData(5, QtCore.Qt.Horizontal, "invID")
        return model