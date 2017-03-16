from PyQt5 import QtSql, QtGui, QtWidgets
from datetime import datetime
import sqlite3

def getDB():
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('citylibrary.db')
    return db

#Create the library application database
def createDB():
    print('Creating DB')
    db = getDB()
    if not db.open():
        QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
                                   QtGui.qApp.tr("Unable to establish a database connection.\n"
                                                 "This example needs SQLite support. Please read "
                                                 "the Qt SQL driver documentation for information "
                                                 "how to build it.\n\n"
                                                 "Click Cancel to exit."),
                                   QtGui.QMessageBox.Cancel)
        return False
    query = QtSql.QSqlQuery()
    createLibraryDB(query)
    return True

def createLibraryDB(query):
    #Create Inventory table
    query.exec_("drop table inventory")
    query.exec_("create table inventory(id int primary key, "
                "type varchar(10), datepurchased datetime)")

    #Create Book table
    query.exec_("drop table book")
    query.exec_("create table book(title varchar(100), "
                "isbn varchar(50), author varchar(100), "
                "yearpublished varchar(4), quantity varchar(4), inventoryid int)")

    #Create Computer table
    query.exec_("drop table computer")
    query.exec_("create table computer(manufacturer varchar(100), "
                "quantity varchar(4), inventoryid int)")

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    createDB()

