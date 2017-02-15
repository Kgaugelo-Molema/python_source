from PyQt5 import QtSql, QtGui, QtWidgets
import sqlite3


def createDB():
    print('Creating DB')
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('citylibrary.db')
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
    #Inventory
    query.exec_("create table inventory(id int primary key, "
                "type varchar(10), datepurchased datetime)")
    # query.exec_("insert into sportsmen values(102, 'Christiano', 'Ronaldo')")
    # query.exec_("insert into sportsmen values(103, 'Ussain', 'Bolt')")
    # query.exec_("insert into sportsmen values(104, 'Sachin', 'Tendulkar')")
    # query.exec_("insert into sportsmen values(105, 'Saina', 'Nehwal')")

    # Book
    query.exec_("create table book(title varchar(100), "
                "isbn varchar(50), author varchar(100), "
                "yearpublished int, quantity int, inventoryid int)")

def addBook(title, isbn, author, year, qty):
    print('Adding book to DB')
    sqlLiteDB = sqlite3.connect('citylibrary.db')
    cursor = sqlLiteDB.cursor()
    cursor.execute('select max(id) from inventory')
    row = cursor.fetchone()
    invID = row[0]
    if invID == 0:
        invID == 1
    invID += 1
    sqlScript = "insert into inventory(id, type, datepurchased) values({0}, 'Book', '15 Feb 2017')".format(str(invID))
    if cursor.execute(sqlScript):
        sqlLiteDB.commit()
    return True

if __name__ == '__main__':
    import sys

app = QtWidgets.QApplication(sys.argv)
createDB()
addBook("MyBook", "1234-5678-1234-6789", "KKK", 2000, 5)
