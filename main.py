
from module.scriptSQL import ConnectMysql,ExtactScriptSQL
import config.config as config


con = ConnectMysql(config.host,config.username,config.root_password,config.database)
con.connect()
ruta_archivo = 'C:/Users/figue/Downloads/Caso_Practico_2024_BBDD.sql'
sentencias = ExtactScriptSQL.leer_sentencias_sql(ruta_archivo)
for idx, sentencia in enumerate(sentencias, start=1):
    print(f"Sentencia {idx}:")
    print(sentencia)
    print("--------------------")