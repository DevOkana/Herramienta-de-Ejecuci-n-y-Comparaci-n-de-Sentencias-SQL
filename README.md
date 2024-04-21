
# Herramienta de Ejecución y Comparación de Sentencias SQL

Esta herramienta es una utilidad de línea de comandos que permite ejecutar sentencias SQL almacenadas en un archivo .sql en una base de datos MySQL, y comparar las salidas de las sentencias ejecutadas con los resultados esperados.

## Características

- Ejecución de sentencias SQL almacenadas en un archivo .sql en una base de datos MySQL.
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

## Uso

Ejecuta el script `main.py` para utilizar la herramienta. Asegúrate de tener un archivo `.sql` con las sentencias que deseas ejecutar en la base de datos MySQL.

```bash
python main.py
```

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas contribuir a este proyecto, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE).

--- 
