import os
import shutil


def ruta(principal, secundario):
    print(os.path.join(principal, secundario))
    return os.path.join(principal, secundario)


class CreateFolder:
    nombre_carpeta = 'sentencias_propias'
    ruta_carpeta = ruta(os.getcwd(), nombre_carpeta)

    def __init__(self):
        # Verifica si el directorio existe
        if os.path.exists(self.ruta_carpeta):
            # Si existe, elimina el directorio
            try:
                shutil.rmtree(self.ruta_carpeta)
                print(f"Directorio '{self.nombre_carpeta}' eliminado.")
            except OSError as e:
                print(f"Error al eliminar el directorio '{self.nombre_carpeta}': {e}")
        # Crea el directorio
        try:
            os.makedirs(self.ruta_carpeta)
            print(f"Directorio '{self.nombre_carpeta}' creado.")
        except OSError as e:
            print(f"Error al crear el directorio '{self.nombre_carpeta}': {e}")


    def consultas(self, nombre, consulta, datos):
        if datos:
            ruta_fichero = ruta(self.ruta_carpeta, nombre+'.txt')
            with open(ruta_fichero,'w') as f:
                #f.write("La consulta es : \n")
                #f.write(consulta)
                #f.write("La datos son : \n")
                f.write('\n'.join(map(str, datos)))



