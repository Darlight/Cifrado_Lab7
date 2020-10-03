"""
Universidad del Valle de Guatemala
CC3078 - Cifrado de informacion
2/10/2020
Grupo #4
nolib_ElGamal.py
Descripcion: Algoritmo ElGamal sin ninguna libreria. 
Link del codigo: https://www.geeksforgeeks.org/elgamal-encryption-algorithm/
"""
import random  
from math import pow
  
a = random.randint(2, 10) 
# gran comun dicisor
def gcd(a, b): 
    if a < b: 
        return gcd(b, a) 
    elif a % b == 0: 
        return b; 
    else: 
        return gcd(b, a % b) 
  
# generador de numeros grandes
def gen_key(q): 
  
    key = random.randint(pow(10, 20), q) 
    while gcd(q, key) != 1: 
        key = random.randint(pow(10, 20), q) 
  
    return key 
  
# exponente modular
def power(a, b, c): 
    x = 1
    y = a 
  
    while b > 0: 
        if b % 2 == 0: 
            x = (x * y) % c; 
        y = (y * y) % c 
        b = int(b / 2) 
  
    return x % c 
  
# Encriptacion asimetrica
def encrypt(msg, q, h, g): 
  
    en_msg = [] 
  
    k = gen_key(q)# llave privada del que envia el mensaje cifrado
    s = power(h, k, q) #
    p = power(g, k, q) #
      
    for i in range(0, len(msg)): 
        en_msg.append(msg[i]) 
  
    print("g^k used : ", p) 
    print("g^ak used : ", s) 
    for i in range(0, len(en_msg)): 
        en_msg[i] = s * ord(en_msg[i]) 
  
    return en_msg, p 
  
def decrypt(en_msg, p, key, q): 
  
    dr_msg = [] 
    h = power(p, key, q) 
    for i in range(0, len(en_msg)): 
        dr_msg.append(chr(int(en_msg[i]/h))) 
          
    return dr_msg 

#---- Main ----
msg = 'encryption'
print("Original Message :", msg) 
  
q = random.randint(pow(10, 20), pow(10, 50)) # numero grande
g = random.randint(2, q) #numero usado dentro del numero grande
  
key = gen_key(q)# Llave privada para el receptor 
h = power(g, key, q)
print("g used : ", g) 
print("g^a used : ", h) 
  
en_msg, p = encrypt(msg, q, h, g) # mensaje encriptado
dr_msg = decrypt(en_msg, p, key, q) #mensaje desencriptado
dmsg = ''.join(dr_msg) 
print("Decrypted Message :", dmsg); 