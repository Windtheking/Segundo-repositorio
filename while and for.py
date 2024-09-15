"""#def opera(num):
    #res = num * 2
    #print (res)
#opera(3)    

#valores = [3,9,8]
#res = map(lambda x: x*x, valores)
#print(list(res))

#valores = [5000, 3500 , 8350 , 9000 , 1000]
#res = list(map(lambda x: x*0.19, valores))
#print(res)

#res = [j * j for j in valores]
#res
#print(res)

#def operaciones (tipo,a,b):
    #return{"suma": lambda x: (a + b) - x,
     #      "resta": lambda x: (a - b) + x ,
    #       "mult": lambda x: (a * b) * x,
    #       "div": lambda x: (a / b) / x}.get(tipo, lambda: None)
print(operaciones("div", 8 , 8)())"""

"""import time
for j in range(5):
    print("jose" , j)
    time.sleep(2)"""


"""pais = "Colombia tierra querida"

for j in range(len(pais)):
    #print(pais[1], end = "")
    print(len(pais))"""

lista = [1,2,8,3,4]
for J in range(len(lista)):
    if (J <= len(lista)):
        print(lista[J], end= "-")
    else:
        lista[J]