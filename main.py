from module.Comparar import listarArchivos, comparar_archivos
from module.Encriptamiento import *
from module.ScriptSQL import ConnectMysql, ExtractScriptSQL
import config.config as config
from module.CompareExit import CreateFolder, ruta

def init(mostrar_sentencias, mostrar_salida, mostrar_sentencias_archivo, cifrar, password, ruta_archivo):
    con = ConnectMysql(config.host, config.username, config.root_password, config.database)
    salida = CreateFolder()
    con.connect()
    try:
        sentencias = ExtractScriptSQL.leer_sentencias_sql(ruta_archivo)

        sentencias_con = 3

        if sentencias:
            for idx, sentencia in enumerate(sentencias, start=1):
                if mostrar_sentencias:
                    print(f"---------Sentencia {idx}:---------")
                    print(sentencia)
                datos = con.execute(sentencia)
                if idx > 9:
                    sentencias_con += 1
                if mostrar_salida:
                    if datos:
                        print("---------DATOS---------")
                        print(datos)
                salida.consultas(f"Sentencia_{idx}", sentencia, datos, cifrar, password, mostrar_sentencias_archivo,sentencias_con)
        else:
            print("---------No hay sentencias--------")
    except FileNotFoundError as e:
        print(e)


if __name__ == "__main__":
    ruta_archivo = ruta(os.getcwd(),"Caso_Practico_2024_BBDD.sql")
    
    print("Ruta por defecto:", ruta_archivo)

    ruta_personalizada = input(
        "Introduce la ruta del archivo .sql para la base de datos o deja en blanco para usar la ruta por defecto:\n")
    if ruta_personalizada:
        ruta_archivo = ruta_personalizada

    m_sentencias = input("¿Mostrar las sentencias de la base de datos por consola? (S/N): ").upper()
    while m_sentencias not in ["S", "N"]:
        m_sentencias = input(
            "Entrada no válida. Por favor, ingresa 'S' para mostrar las sentencias o 'N' para no mostrarlas: ").upper()

    e_sentencias = input("¿Mostrar la salida de las sentencias por consola (S/N)?: ").upper()
    while e_sentencias not in ["S", "N"]:
        e_sentencias = input(
            "Entrada no válida. Por favor, ingresa 'S' para mostrar las sentencias o 'N' para no mostrarlas: ").upper()

    print("IMPORTANTE: En caso de escoger que S debe tener cuidado, ya que las sentencias estarán grabadas en el fichero de salida")

    m_sentencias_archivo = input("¿Mostrar la sentencias en el archivo de salida (S/N)?: ").upper()
    cifrar = False
    password = ""
    while m_sentencias_archivo not in ["S", "N"]:
        m_sentencias_archivo = input(
            "Entrada no válida. Por favor, ingresa 'S' para mostrar las sentencias o 'N' para no mostrarlas: ").upper()

    if m_sentencias_archivo == "S":
        mostrar_sentencias_archivo = True

        print("Se almacenarán las sentencias en los ficheros de salida por seguridad y para evitar filtraciones.")
        print("IMPORTANTE: En caso de que olvides cifrarlas y pases la carpeta a un compañero, las sentencias se cifrarán por defecto.")
        entrada = input("Si no deseas cifrarlas, presiona 'N/n', deja en blanco para poner contraseña o A para contraseña automatica: ")
        if entrada.upper() == "N":
            cifrar = False
        elif entrada.upper() == "A":
            cifrar = True
            password = generar_contrasena()
            print(f"Contraseña Generada: {password}")
        else:
            cifrar = True
            while len(password) <= 8:
                password = input("Debes introducir una contraseña de más de 8 caracteres: ")
    else:
        mostrar_sentencias_archivo = False
   
    # Llamar a la función init con los parámetros adecuados
    init(m_sentencias == "S", e_sentencias == "S", mostrar_sentencias_archivo, cifrar, password, ruta_archivo)
    entrada = input("Se ha terminado de general, ¿Quieres comparar los resultados con los base(S/N)?:")
    while entrada.upper() not in ["S", "N"]:
        entrada = input()
    if(entrada.upper() == "S"):
        comp, gen = listarArchivos(ruta(os.getcwd(), "sentencias_comparar"),
                                   ruta(os.getcwd(), "sentencias_generadas"))
        """
            Iterar entre los carpetas el primer parametro son son 
            los archivos base a comparar, los gen son los generados actualmente por el script
        """
        for x in range(len(comp)):    
            try:

                comparar_archivos(gen[x],comp[x])
            except IndexError as e:
                print(f"Hay columnas de más en las tablas generadas ERROR: {e}")
    else:
        exit()