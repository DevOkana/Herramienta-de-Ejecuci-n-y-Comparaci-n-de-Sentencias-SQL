import mysql.connector

from module.scriptSQL import ConnectMysql,ExtractScriptSQL
import config.config as config
from module.CompareExit import CreateFolder


con = ConnectMysql(config.host,config.username,config.root_password,config.database)
salida = CreateFolder()
con.connect()
ruta_archivo = 'C:/Users/figue/Downloads/Caso_Practico_2024_BBDD.sql'
sentencias = ExtractScriptSQL.leer_sentencias_sql(ruta_archivo)

for idx, sentencia in enumerate(sentencias, start=1):
    print("Sentencia {}: {}".format(idx, sentencia))
    datos = con.execute(sentencia)


    salida.consultas(f"Sentencia_{idx}", sentencia, datos)
    print("------------------")





