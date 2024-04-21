
# Herramienta de Ejecución y Comparación de Sentencias SQL

Esta herramienta es una utilidad de línea de comandos que permite ejecutar sentencias SQL almacenadas en un archivo `.sql` en una base de datos MySQL, y comparar las salidas de las sentencias ejecutadas con los resultados esperados.

## Características

- Ejecución de sentencias SQL almacenadas en un archivo `.sql` en una base de datos MySQL.
- Comparación de las salidas de las sentencias ejecutadas con los resultados esperados.
- Opción para mostrar las sentencias de la base de datos por consola.
- Opción para mostrar la salida de las sentencias por consola.
- Opción para mostrar las sentencias en el archivo de salida.
- Opción para cifrar las sentencias almacenadas en los archivos de salida.

## Requisitos

- Python 3.6 o superior
- MySQL Server
- Bibliotecas Python: 
    - `mysql-connector-python` -> Conectar con la base de datos
    - `sqlparse` -> Reconocer sentencias SQL
    - `cryptography` -> Para encriptar las salidas de las sentencias
    
## Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/tu_usuario/herramienta-sentencias-sql.git
```

2. Accede al directorio del proyecto:

```bash
cd herramienta-sentencias-sql
```

3. Instala las dependencias:

```bash
pip install -r requirenments.txt
```

4. Configura el acceso a la base de datos dentro de la ruta `config/config.py`:
```python
host = "localhost" # Cambiar por la dirección IP donde está el servidor
username = "root" # Cambiar por el usuario de la base de datos
root_password = "12345678" # Cambiar por la contraseña del usuario
database = "Cadena_hotelera" # Base de datos por defecto a utilizar
```
## Uso

Ejecuta el script `main.py` para utilizar la herramienta. Asegúrate de tener un archivo `.sql` con las sentencias que deseas ejecutar en la base de datos MySQL.

```bash
python main.py
```

## Módulos

- `Comparar.py`: Se recorre todos los archivos de `sentencias_comparar` y `sentencia_generadas`.
   - Función `comparar_archivos`:
     - El primer parámetro `archivo1` son los archivos a comprobar.
     - El segundo parámetro `archivo2` son los archivos base con los que se va a comparar.
     - El parámetro `depurar` es para buscar errores entre los datos y la línea de cada fichero y salida.
     
   ```python 
   def comparar_archivos(archivo1, archivo2, depurar=False)
   ```
   
   - Función `listarArchivos`:
     - El primer parámetro `comparar` será la ruta donde están los archivos base a comparar.
     - El segundo parámetro `generadas` será la ruta donde se han generado las nuevas salidas para comparar.
    
    ```python
    def listarArchivos(comparar, generadas):
    ```
   
- `CompareExit`: Encargado de generar los archivos donde serán guardadas la salida y la carpeta que los contendrá.
  
- `Encriptamiento`: Para encriptar las sentencias que serán guardadas en el archivo de salida. Generará las contraseñas en caso de no querer poner una de manera automática.  

- `ScriptSQL`: Contendrá todo lo relacionado con la base de datos y la conexión con ella.
   - `ConnectMysql`: Contendrá la conexión con la base de datos. Los datos para conectarse con ella estarán en `config/config.py`. 
   - `ExtractScriptSQL`: Leerá las sentencias del archivo. La ruta se especificará, se eliminarán los comentarios en `--` y los `#`, también se eliminará `DELIMITER` de las funciones porque `mysql.connector` es incompatible con ella. Esto se hace de manera automática.

## Menú

Se pedirán una serie de parámetros para completar el correcto funcionamiento:

1. La ruta donde se encuentra el script. Por defecto es:
   ```python 
   ruta(os.getcwd(),"Caso_Practico_2024_BBDD.sql")
   ```

2. Se pedirá si deseas mirar la consulta y los datos de salida en consola con la entrada (S/N).

3. Deberás escoger si quieres introducir las sentencias en la ruta del archivo de salida. Ejemplo de salida:
   ```SQL 
    -- La consulta es :
    select * from nombre_tabla
    -- La datos son :
    (columna1, columna2, columna3)
   ```

4. En caso de escoger sí, por temas de seguridad y para evitar problemas de que se pueda enviar la salida con la sentencia, se encriptarán las sentencias con una contraseña que se pedirá por pantalla. Por defecto, se encriptará. Si se escoge 'A/a', se generará una contraseña aleatoria. Si escoges introducir la contraseña, deberá tener más de 8 caracteres.

5. Cuando termine de recrear todas las salidas, pedirá si deseas comprobar las salidas generadas con las salidas a comparar, que han sido las que previamente se han generado por las sentencias de otras personas para ver si las salidas son iguales.


## Términos y Condiciones

1. **Responsabilidad del Usuario**: El usuario asume la responsabilidad total de la utilización de este código. Se advierte que este código puede contener información sensible relacionada con casos prácticos específicos. Por lo tanto, el usuario debe leer detenidamente las instrucciones y los menús proporcionados, y se le insta a no compartir las sentencias SQL con terceros. Si el usuario decide compartir el código, se le recomienda encarecidamente revisar la salida generada para garantizar la seguridad y la integridad de los datos. 

2. **Plagio y Uso Inapropiado**: El autor de este código no se hace responsable del plagio u otros usos inapropiados que puedan surgir del uso de este código. Se prohíbe estrictamente el plagio, la distribución no autorizada o cualquier otro uso inapropiado del código y sus resultados. 

3. **Seguridad de los Datos**: Se hace hincapié en la importancia de la seguridad de los datos. En caso de compartir el código con otros usuarios, se recomienda encarecidamente no incluir las sentencias SQL que puedan contener datos sensibles. El autor no se hace responsable de cualquier divulgación no autorizada de datos sensibles que pueda surgir del uso de este código.

4. **Contraseñas y Encriptación**: En caso de optar por encriptar las sentencias SQL, se debe tener en cuenta que el proceso de encriptación se realiza con el fin de garantizar la seguridad de los datos. Se recomienda encarecidamente utilizar contraseñas seguras y mantenerlas confidenciales. El autor no se hace responsable de la pérdida o divulgación de contraseñas utilizadas en el proceso de encriptación.

5. **Aceptación de los Términos**: El uso de este código implica la aceptación de los términos y condiciones establecidos anteriormente. Cualquier violación de estos términos puede dar lugar a acciones legales y responsabilidades civiles.


## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas contribuir a este proyecto, por favor, abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE).