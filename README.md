# delt-aes

## Criptografia AES-256-CBC em Python

Este projeto implementa um programa simples de criptografia e descriptografia de arquivos utilizando o algoritmo **AES-256** no modo **CBC**, com derivação de chave via **PBKDF2**.

O programa pode ser executado diretamente no terminal, permitindo **cifrar** e **decifrar** qualquer arquivo informado.

---

## 🚀 Pré-requisitos

- **Python 3.8+**
- Biblioteca [`cryptography`](https://pypi.org/project/cryptography/)

Instale a dependência com:

```bash
pip install cryptography
```
---

## Instale o código

Clone este repositório ou baixe o arquivo delt-aes
```bash
git clone https://github.com/deltacp1/delt-aes/
cd cripto_aes
```
## Modo de utilizar

```bash
python cripto_aes.py <operacao> <arquivo_e> <arquivo_s> <key>
```
- operação -> escolhida entre decifrar ou cifrar
- arquivo_e -> o caminho do arquivo que vai ser processado
- arquivo_s -> o caminho pro arquivo da saida
- key -> senha para derivar chave AES

##Exemplo de utilização para cifrar

```bash
python cripto_aes.py cifrar exemplo.txt mens.enc secret_key
```
##Exemplo de utilização para cifrar

```bash
python cripto_aes.py decifrar mens.enc exemplo_decif.txt secret_key
```







