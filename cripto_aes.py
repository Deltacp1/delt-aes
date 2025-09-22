import sys
import os
import hashlib
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

ITERATIONS = 100000
KEY_SIZE = 32  # 256 bits
SALT_SIZE = 16
IV_SIZE = 16

def get_key(password: str, salt: bytes) -> bytes:
    """Deriva a chave a partir da senha e do salt usando PBKDF2."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_SIZE,
        salt=salt,
        iterations=ITERATIONS,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def cifrar(entrada, saida, chave):
    with open(entrada, "rb") as f:
        conteudo = f.read()

    salt = os.urandom(SALT_SIZE)
    iv = os.urandom(IV_SIZE)
    key = get_key(chave, salt)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Padding PKCS7 manual (CBC precisa de múltiplos de 16)
    padding_len = 16 - (len(conteudo) % 16)
    conteudo += bytes([padding_len]) * padding_len

    dados_cifrados = encryptor.update(conteudo) + encryptor.finalize()

    with open(saida, "wb") as f:
        f.write(salt + iv + dados_cifrados)

def decifrar(entrada, saida, chave):
    with open(entrada, "rb") as f:
        conteudo = f.read()

    salt = conteudo[:SALT_SIZE]
    iv = conteudo[SALT_SIZE:SALT_SIZE + IV_SIZE]
    dados_cifrados = conteudo[SALT_SIZE + IV_SIZE:]

    key = get_key(chave, salt)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    dados = decryptor.update(dados_cifrados) + decryptor.finalize()

    # Remove padding
    padding_len = dados[-1]
    dados = dados[:-padding_len]

    with open(saida, "wb") as f:
        f.write(dados)

def main():
    if len(sys.argv) != 5:
        print("Uso: python cripto_aes.py <cifrar|decifrar> <entrada> <saida> <chave>")
        sys.exit(1)

    operacao, entrada, saida, chave = sys.argv[1:]

    try:
        if operacao == "cifrar":
            cifrar(entrada, saida, chave)
        elif operacao == "decifrar":
            decifrar(entrada, saida, chave)
        else:
            raise ValueError("Operação inválida. Use 'cifrar' ou 'decifrar'.")
    except Exception as e:
        print("Erro:", str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()
