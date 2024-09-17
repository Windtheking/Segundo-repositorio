import pandas as pd
import numpy as np
import xlsxwriter as xl
from os import system
import time
import matplotlib.pyplot as plt
import grafica2 as gra


dataset = pd.read_excel(r'C:\Users\Santy\Desktop\ADSO 13\Trabajos visual estudio\Ventas.xlsx', 
                        engine ='openpyxl', 
                        header = 0)
serie = pd.Series(dataset.to_numpy().tolist())
temp = 0

#lis = dataset.to_numpy().tolist()
def operacion_simple():
    print('${:,.1f}'.format(serie[4][5]*serie[4][6]))

def operacion_practica():
    #para recorrer la serie y multiplicar valores 
    #y sumar las mutiplicaciones
    for Z in range(len(serie)):
        if serie[Z][0]=='SAOVia_48':
            temp += serie[Z][5]*serie[Z][6]
    print('${:,.1f}'.format(temp))

#lo mismo de arriba pero mas simple y en el total total
def total_tiendas():
    temp = 0
    for Z in range(len(serie)):
        temp += serie[Z][5]*serie[Z][6]
    print('${:,.1f}'.format(temp))
def filtro():
    temp = 0
    #para poder ejecutar la multiplicacion total y suma usar el input tienda 
    Tiendas = ["1. SAO_53",
               "2. SAO_57",
               "3. SAO_58",
               "4. SAO_92",
               "5. SAO_93",
               "6. SAOVia_40",
               "7. SAOVia_43",
               "8. SAOVia_48",
               ]
    print(Tiendas)
    tienda = str(input('\n ingrese nombre de la tienda: '))
    for Z in range(len(serie)):
        if serie[Z][0]== tienda:
            temp += serie[Z][5]*serie[Z][6]
    print('el valor de ingresos en la tienda escogida es: ' + '${:,.1f}'.format(temp))    


def menu():
    
    print('1) Ingreso General')
    print('2) Filtro de tienda e Ingreso Especifico')
    print('3) graficar los valores')
    print('4) Fin del programa')
    
    op = int(input("\nIngrese su opción del menu: "))
    match op:
        case 1:
            print("\n El ingreso general de las tiendas olimpica fue")
            total_tiendas()
            print("¿esea seguir? N/Y:")
            respuesta = input()
            match respuesta:
                case "N":
                    print("proceso terminado, muchas gracias por usar nuestros servicios")
                    time.sleep(1.5)
                    system("cls")
                    quit
                case "Y":
                    system("cls")
                    menu()
        case 2:
            print("\n usted ha escogido el filtro especifico de tiendas")
            print("\nescoja su tienda, no olvide escribir el nombre ")
            print("igual a como aparece en la lista")
            filtro()
            print("¿esea seguir? N/Y:")
            respuesta1 = input()
            match respuesta1:
                case "N":
                    print("proceso terminado, muchas gracias por usar nuestros servicios")
                    time.sleep(1.5)
                    system("cls")
                    quit
                case "Y":
                    system("cls")
                    menu()        
        case 3:
            system("cls")
            gra.graficar()
            menu()
        case 4:
            print("proceso terminado, muchas gracias por usar nuestros servicios")
            time.sleep(1.5)
            system("cls")
            quit
menu()
