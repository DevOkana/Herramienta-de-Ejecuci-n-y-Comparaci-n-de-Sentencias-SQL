from decimal import Decimal
import os
import datetime
import re

def comparar_tuplas(archivo2,tupla2,archivo1,tupla1):
    print("    *---- Proxima Evaluación ---------")
    # Convertir las tuplas en listas para poder modificarlas
    tupla1_lista = list(tupla1)
    tupla2_lista = list(tupla2)

    # Iterar sobre los elementos de la primera tupla
    for elem1 in tupla1:
        # Si el elemento de la primera tupla está en la segunda tupla
        if elem1 in tupla2_lista:
            # Eliminar el elemento coincidente de ambas listas
            tupla2_lista.remove(elem1)
            tupla1_lista.remove(elem1)

    # Convertir las listas restantes en cadenas para formar un patrón regex
    patron_regex1 = '|'.join(map(str, tupla1_lista))
    patron_regex2 = '|'.join(map(str, tupla2_lista))

    # Contadores de coincidencias
    contador_coincidencias1 = 0
    contador_coincidencias2 = 0


    # Buscar coincidencias usando expresiones regulares
    for elem2 in tupla2_lista:
        if re.search(patron_regex1, str(elem2)):
            contador_coincidencias1 += 1
            #tupla2_lista.remove(elem2)
            #tupla1_lista.remove(elem2)
            

    for elem1 in tupla1_lista:
        if re.search(patron_regex2, str(elem1)):
            contador_coincidencias2 += 1
            #tupla1_lista.remove(elem1)
            #tupla1_lista.remove(elem1)
            

    # Sumar los contadores de coincidencias
    total_coincidencias = contador_coincidencias1 + contador_coincidencias2

    # Imprimir las listas restantes y el número total de coincidencias
    if total_coincidencias > 0:
        print("Coincidencias encontradas: {}, EVALUAR MANUALMENTE".format(total_coincidencias))
    if tupla2_lista:
        print(f"Archivo salida: {os.path.relpath(archivo2)} columna restante: ", tupla2_lista)
    if tupla1_lista:
        print(f"Archivo a comparar:{os.path.relpath(archivo1)} columna restantes: ", tupla1_lista)
    

    # Si las listas están vacías, todas las coincidencias fueron encontradas y las tuplas son iguales
    return not (tupla1_lista or tupla2_lista)


def comparar_archivos(archivo1, archivo2, depurar=False):
    encontrado = False
    with open(archivo1, 'r', encoding='utf-8') as f1, open(archivo2, 'r', encoding='utf-8') as f2:
        print("-----------------------------------------------------------------")
        print(f"Evaluando {archivo1}")
        for linea1 in f1:            
            if linea1.strip() == "La consulta es :":
                for _ in range(2):
                    next(f1)  # Empezar desde la cuarta línea
                continue
            tupla1 = eval(linea1)
            if depurar:
                print(f"-------------- Nueva Línea ------------")
                print(tupla1)  # Solo para depuración, puedes eliminar esta línea
            for elemento_a_buscar in tupla1:
                encontrado_en_linea = False
                mas_columna = [False,""]
                for linea2 in f2:
                    if linea2.strip() == "La consulta es :":
                        for _ in range(2):
                            next(f2)  # Empezar desde la cuarta línea
                        continue
                    tupla2 = eval(linea2)
                    
                    if len(tupla2) == len(tupla1):
                        if elemento_a_buscar in tupla2:
                            encontrado_en_linea = True
                            if depurar:
                                print(f"Encontrado {elemento_a_buscar} en {os.path.relpath(archivo2)}")
                            break
                    elif len(tupla2) > len(tupla1):
                        if elemento_a_buscar in tupla2:
                            encontrado_en_linea = True
                            mas_columna = [True,archivo2]
                            
                            if depurar:
                                print(f" * - Encontrado {elemento_a_buscar} en {os.path.relpath(archivo2)} pero hay una columna demás en {os.path.relpath(archivo2)}")
                            break                            
                    elif len(tupla2) < len(tupla1):
                        encontrado_en_linea = True
                        mas_columna = [True,archivo1]
                        
                        if depurar:
                            print(f" * - Encontrado {elemento_a_buscar} en {os.path.relpath(archivo2)} pero hay una columna demás en {os.path.relpath(archivo1)}")
                        break

                if not encontrado_en_linea:
                    comparar_tuplas(archivo2,tupla2,archivo1,tupla1)
                    print(f"No encontrado {elemento_a_buscar} en {os.path.relpath(archivo2)}.")
                    encontrado = True
                tupla2 = []
                f2.seek(0)  # Reiniciar la lectura de archivo2 al inicio
            tupla1 = []
            # Reiniciar el puntero de archivo2
            f2.seek(0)
        if not encontrado:
            if mas_columna[0]:
                print(f"Todos los elementos del {os.path.relpath(archivo1)} se encuentran en {os.path.relpath(archivo2)} pero tienen una columna demás en {os.path.relpath(mas_columna[1])}")

            else:
                 print(f"Todos los elementos del {os.path.relpath(archivo1)} se encuentran en {os.path.relpath(archivo2)}.")




def listarArchivos(comparar, generadas):
    archivos_comparar = [os.path.join(comparar, archivo) for archivo in os.listdir(comparar) if os.path.isfile(os.path.join(comparar, archivo))]
    archivos_generadas = [os.path.join(generadas, archivo) for archivo in os.listdir(generadas) if os.path.isfile(os.path.join(generadas, archivo))]

    return archivos_generadas, archivos_comparar


