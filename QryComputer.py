from QryBase import *


class QrComputer(QrBase):
    def __init__(self):
        QrBase.__init__(self)

    #Add computer to DB
    def Add(self, manufacturer, qty):
        result = False
        print('Adding computer to DB')
        invID = self.genInventoryID()
        if invID > 0:
            sqlScript = "insert into computer(manufacturer, quantity, inventoryid) values('{0}', '{1}', {2})".format(manufacturer, qty, str(invID))
            if self.cursor.execute(sqlScript):
                self.sqlLiteDB.commit()
                result = True
        return result

    #Update computer data
    def Update(self, invID, manufacturer, qty):
        result = False
        print('Updating computer data')
        sqlScript = "update computer set manufacturer = '{0}', manufacturer = '{1}' where inventoryid = {2}".format(manufacturer, qty, str(invID))
        if self.cursor.execute(sqlScript):
            self.sqlLiteDB.commit()
            result = True
        return result

    #Delete computer data
    def Delete(self, invID):
        result = False
        print('Deleting computer data')
        sqlScript = "delete from computer where inventoryid = {0}".format(str(invID))
        if self.cursor.execute(sqlScript):
            self.sqlLiteDB.commit()
            result = True
        return result


