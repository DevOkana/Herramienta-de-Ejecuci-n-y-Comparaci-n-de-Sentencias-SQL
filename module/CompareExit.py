import os
import shutil
from module import Encriptamiento



def ruta(principal, secundario):
    print(os.path.join(principal, secundario))
    return os.path.join(principal, secundario)


class CreateFolder:
    
    nombre_carpeta = 'sentencias_generadas'
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


    def consultas(self, nombre, consulta, datos,cifrar,password,m_sentencias_archivo,sentencias):

        if datos:
            ruta_fichero = ruta(self.ruta_carpeta, nombre+"_APARTADO_"+ str(sentencias)+'.txt')
           
            with open(ruta_fichero,'w',encoding='utf-8') as f:
                if m_sentencias_archivo:
                    if cifrar:
                        sentencia = str(Encriptamiento.encriptar(password,consulta.replace('\n', ' ')))
                    else:
                        sentencia = consulta.replace('\n', ' ')
                    f.write("La consulta es : \n")
                    f.write(sentencia)
                    f.write("\n La datos son : \n")
                f.write('\n'.join(map(str, datos)))
                f.close()


