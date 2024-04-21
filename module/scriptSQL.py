#Connecto SQL
import mysql.connector
import re
import sqlparse


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
        try:
            self.mydb = mysql.connector.connect(host=self.host,user=self.user,password=self.password, database=self.database)
        except mysql.connector.errors.ProgrammingError as _:
            self.mydb = mysql.connector.connect(host=self.host, user=self.user, password=self.password)
            mycursor = self.mydb.cursor()
            mycursor.execute(f"CREATE DATABASE {self.database}")

    def execute(self, sql):
        mycursor = self.mydb.cursor()
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult

class ExtractScriptSQL:
    def leer_sentencias_sql(ruta_achivo):
        # Lista para almacenar las sentencias SQL
        sentencias_sql = []

        # Abre el archivo .sql en modo lectura
        with open(ruta_achivo, 'r') as file:
            # Lee todo el contenido del archivo
            try:
                sql_content = file.read()
                sql_content = re.sub(r'(--.*)', '', sql_content)

                # Elimina comentarios de varias líneas
                sql_content = re.sub(r'(/\*.*?\*/)', '', sql_content, flags=re.DOTALL)
                # Elimina líneas que contienen solo "--------------------"
                sql_content = re.sub(r'-{20,}', '', sql_content)
                sql_content = re.sub(r'(--.*)', '', sql_content)
                sql_content = re.sub(r'DELIMITER\s*//', '', sql_content, flags=re.IGNORECASE)
                sql_content = re.sub(r'\s*//\s*DELIMITER\s*;', '', sql_content)
                # Divide el contenido en líneas
                lines = sql_content.split('\n')

                # Filtra las líneas vacías y las que contienen solo comentarios
                lines = [line.strip() for line in lines if line.strip() and not line.strip().startswith('#')]

                # Reconstruye el contenido sin las líneas eliminadas
                sql_content = '\n'.join(lines)
                # Divide el contenido en sentencias SQL
                parsed_sql = sqlparse.split(sql_content)
                # Recorre cada sentencia SQL parseada
                for sql_statement in parsed_sql:
                    # Agrega la sentencia a la lista
                    sentencias_sql.append(sql_statement.strip())
                file.close()
                return sentencias_sql
            except OSError as a:
                print(a.errno)
        return False