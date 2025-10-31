import random 
texto = input("Escribe: " )

llave = ''.join(str(random.randint(0,1)) for _ in texto)

def xor(texto, llave):
  return ''.join(chr(ord(texto[i]) ^ ord(llave[i])) for i in range (len(texto)))

cifrado = xor(texto, llave)
descrifrado = xor(cifrado, llave)

print("Texto plano:", texto, " | Llave:", llave)
print("Texto encriptado:", cifrado)
print("Texto encriptado:", descrifrado)