from datetime import datetime
import sqlite3


class QrBase(object):
    def __init__(self):
        self.sqlLiteDB = sqlite3.connect('citylibrary.db')
        self.cursor = self.sqlLiteDB.cursor()

    def genInventoryID(self):
        result = -1
        self.cursor.execute('select max(id) from inventory')
        row = self.cursor.fetchone()
        invID = 0;
        if row[0] != None:
            invID = row[0]
        invID += 1
        datestr = datetime.now().strftime("%d %B %Y")
        sqlScript = "insert into inventory(id, type, datepurchased) values({0}, 'Book', '{1}')".format(str(invID), datestr)
        if self.cursor.execute(sqlScript):
            self.sqlLiteDB.commit()
            result = invID
        return result

