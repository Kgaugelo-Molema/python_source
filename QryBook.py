from datetime import datetime
import sqlite3

#Add book to DB
def Add(title, isbn, author, year, qty):
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

#Update book data
def Update(invID, title, isbn, author, year, qty):
    print('Updating book data')
    sqlLiteDB = sqlite3.connect('citylibrary.db')
    cursor = sqlLiteDB.cursor()
    sqlScript = "update book set title = {0}, isbn = {1}, author = {2}, yearpublished = {3}, quantity = {4} where inventoryid = {5}".format(title, isbn, author, year, qty, str(invID))
    if cursor.execute(sqlScript):
        sqlLiteDB.commit()
        return True


