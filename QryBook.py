from QryBase import *


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
    def Update(self, invID, title, isbn, author, year, qty):
        result = False
        print('Updating book data')
        sqlScript = "update book set title = '{0}', isbn = '{1}', author = '{2}', yearpublished = '{3}', quantity = '{4}' where inventoryid = {5}".format(title, isbn, author, year, qty, str(invID))
        if self.cursor.execute(sqlScript):
            self.sqlLiteDB.commit()
            result = True
        return result

    #Delete book data
    def Delete(self, invID):
        result = False
        print('Deleting book data')
        sqlScript = "delete from book where inventoryid = {0}".format(str(invID))
        if self.cursor.execute(sqlScript):
            self.sqlLiteDB.commit()
            result = True
        return result


