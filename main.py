
from module.scriptSQL import ConnectMysql
import config.config as config

con = ConnectMysql(config.host,config.username,config.root_password,config.database)
con.connect()
con.execute("SELECT * FROM hoteles")