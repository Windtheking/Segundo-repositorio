from random import randint
from operaciones import suma,resta,multiplicacion,dividir
import time
print("programa para operaciones matematicas")

a = float(input("valor 1: "))
b = float(input("valor 2: "))

suma(a,b)
resta(a,b)
multiplicacion(a,b)
dividir(a,b)

input("precione enter para continuar")

time.sleep(5)

print("gracias por usar nuestros servicios, hasta pronto")

time.sleep(1.5)

stat = randint(1,20)
if stat == 1:
    print("you got a 1, -5 modifier")
else:
    print("go fuck yourself")