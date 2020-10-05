"""
Universidad del Valle de Guatemala
CC3078 - Cifrado de informacion
2/10/2020
Grupo #4
lib_ElGamal.py
Descripcion: Algoritmo ElGamal con libreria. 
Codigo obtenido de: https://pypi.org/project/elgamal/#description
"""
from elgamal.elgamal import Elgamal 

# Mensaje a cifrar
m = b'Hola mundo'
print("Mensaje a cifrar:",m)

# Se generar las llaves
# pb = llave publica
# pv = llave privada
# En este caso ambas llaves son de 128 bits
pb, pv = Elgamal.newkeys(128)
print("\nNumero primo: ", pb.p)
print("\nGenerador: ", pb.g)
print("\nLlave publica: ", pb)
print("\nLlave privada: ", pv)

# Se cifra el mensaje utilizando la llave publica
ct = Elgamal.encrypt(m, pb)
print("\nTexto cifrado: ", ct)

# Se descifra el mensaje cifrado utilizando la llave privada
dd = Elgamal.decrypt(ct, pv)
print("\nTexto descifrado: ", dd)
