from decimal import Decimal
import os
import datetime


def comparar_archivos(archivo1, archivo2, depurar=False):
    encontrado = False
    with open(archivo1, 'r') as f1, open(archivo2, 'r') as f2:
        for linea1 in f1:
            if linea1 == "La consulta es :":
                linea1 = f1.readlines()[3:]  # Empezar desde la cuarta línea
            tupla1 = eval(linea1)
            if depurar:
                print(f"-------------- Nueva Línea ------------")
                print(tupla1)  # Solo para depuración, puedes eliminar esta línea
            for x in range(len(tupla1)):
                elemento_a_buscar = tupla1[x]
                if depurar:
                    print(f"--------------Linea número {x}------------")
                encontrado_en_linea = False
                for linea2 in f2:
                    if linea2 == "La consulta es :":
                        linea2 = f2.readlines()[3:]  # Empezar desde la cuarta línea
                    tupla2 = eval(linea2)
                    if elemento_a_buscar in tupla2:
                        encontrado_en_linea = True
                        if depurar:
                            print(f"Encontrado {elemento_a_buscar} de la posición {tupla1.index(elemento_a_buscar)} del archivo {os.path.relpath(archivo1)} ")
                            print(f"Encontrado {elemento_a_buscar} en la posición {tupla2.index(elemento_a_buscar)} del archivo {os.path.relpath(archivo2)} ")
                        break
                if not encontrado_en_linea:
                    print(f"No encontrado {elemento_a_buscar} en {os.path.relpath(archivo2)}. Fallo en la línea {x} posición {tupla2.index(tupla2[x])} valor {tupla2[x]} de {os.path.relpath(archivo1)}, se esperaba {tupla1[x]}")
                    encontrado = True
                f2.seek(0)  # Reiniciar la lectura de archivo2 al inicio
            tupla1 = []  # Reiniciar tupla1
            tupla2 = []  # Reiniciar tupla2
    if not encontrado:
        print(f"Todos los elementos del {os.path.relpath(archivo1)} se encuentran en {os.path.relpath(archivo2)}.")
    f1.close()
    f2.close()

def listarArchivos(comparar, generadas):
    archivos_comparar = [os.path.join(comparar, archivo) for archivo in os.listdir(comparar) if os.path.isfile(os.path.join(comparar, archivo))]
    archivos_generadas = [os.path.join(generadas, archivo) for archivo in os.listdir(generadas) if os.path.isfile(os.path.join(generadas, archivo))]

    return archivos_generadas, archivos_comparar


