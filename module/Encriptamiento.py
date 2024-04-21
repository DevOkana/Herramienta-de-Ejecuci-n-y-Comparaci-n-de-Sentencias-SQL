from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
import base64
import random
import string

def generar_contrasena(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def generar_clave(password):
    # Codificar la contraseña como bytes
    password_bytes = password.encode('utf-8')

    # Generar una sal aleatoria
    sal = os.urandom(16)

    # Configurar el algoritmo PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # Tamaño de la clave en bytes
        salt=sal,
        iterations=100000,  # Número de iteraciones (ajustable según sea necesario)
        backend=default_backend()
    )

    # Derivar la clave
    clave = kdf.derive(password_bytes)

    # Devolver la clave codificada en base64
    return base64.urlsafe_b64encode(clave)


def cifrar(texto, clave):
    f = Fernet(clave)
    return f.encrypt(texto.encode())


def descifrar(texto_cifrado, clave):
    f = Fernet(clave)
    return f.decrypt(texto_cifrado).decode()


def encriptar(password, texto):
    # Generar una clave usando una contraseña
    clave = generar_clave(password)
    # Cifrar el texto
    return cifrar(texto, clave)



