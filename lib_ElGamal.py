"""
Universidad del Valle de Guatemala
CC3078 - Cifrado de informacion
2/10/2020
Grupo #4
lib_ElGamal.py
Descripcion: Algoritmo ElGamal con libreria. 
link del codigo: https://pythonhosted.org/pycrypto/Crypto.PublicKey.ElGamal-module.html
"""
from Crypto import Random
from Crypto.Random import random
from Crypto.PublicKey import ElGamal
from Crypto.Util.number import GCD
from Crypto.Hash import SHA

message = "Hello"
key = ElGamal.generate(1024, Random.new().read)
h = SHA.new(message).digest()
while 1:
    k = random.StrongRandom().randint(1,key.p-1)
    if GCD(k,key.p-1)==1: break
sig = key.sign(h,k)

if key.verify(h,sig):
    print("OK")
else:
    print("Incorrect signature")
