#Connecto SQL
import mysql.connector


class ConnectMysql:

    host = None
    password = None
    user = None
    database = None
    mydb = None

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
    def connect(self):
        self.mydb = mysql.connector.connect(host=self.host,user=self.user,password=self.password, database=self.database)
    def execute(self, sql):
        mycursor = self.mydb.cursor()
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

