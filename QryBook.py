from QryBase import *
import sqlite3


class QrBookData(QrBase):
    def __init__(self):
        QrBase.__init__(self)

    #Add book to DB
    def Add(self, title, isbn, author, year, qty):
        result = False
        print('Adding book to DB')
        invID = self.genInventoryID()
        if invID > 0:
            sqlScript = "insert into book(title, isbn, author, yearpublished, quantity, inventoryid) values('{0}', '{1}', '{2}', '{3}', '{4}', {5})".format(title, isbn, author, year, qty, str(invID))
            if self.cursor.execute(sqlScript):
                self.sqlLiteDB.commit()
                result = True
        return result

    #Update book data
    def Update(invID, title, isbn, author, year, qty):
        print('Updating book data')
        sqlLiteDB = sqlite3.connect('citylibrary.db')
        cursor = sqlLiteDB.cursor()
        sqlScript = "update book set title = {0}, isbn = {1}, author = {2}, yearpublished = {3}, quantity = {4} where inventoryid = {5}".format(title, isbn, author, year, qty, str(invID))
        if cursor.execute(sqlScript):
            sqlLiteDB.commit()
            return True


