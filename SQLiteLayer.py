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

#Add book to DB
def DBAddBook(title, isbn, author, year, qty):
    print('Adding book to DB')
    sqlLiteDB = sqlite3.connect('citylibrary.db')
    cursor = sqlLiteDB.cursor()
    cursor.execute('select max(id) from inventory')
    row = cursor.fetchone()
    invID = 0;
    if row[0] != None:
        invID = row[0]
    invID += 1
    datestr = datetime.now().strftime("%d %B %Y")
    sqlScript = "insert into inventory(id, type, datepurchased) values({0}, 'Book', '{1}')".format(str(invID), datestr)
    if cursor.execute(sqlScript):
        sqlScript = "insert into book(title, isbn, author, yearpublished, quantity, inventoryid) values('{0}', '{1}', '{2}', '{3}', '{4}', {5})".format(title, isbn, author, year, qty, str(invID))
        if cursor.execute(sqlScript):
            sqlLiteDB.commit()
            return True


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    createDB()

