import pandas as pd
import numpy as np
import xlsxwriter as xl
dataset = pd.read_excel(r'C:\Users\Santy\Desktop\ADSO 13\Trabajos visual estudio\tRABAJOS PANDAS\adso13.xlsx', 
                        engine ='openpyxl', header = 0, usecols = "B,D")


datos = pd.DataFrame(dataset)
lis = dataset.to_numpy().tolist()
deduccion = []
lis.append(["samuel", 456982])
print(lis)
print("esta variable es tipo: ", type(lis))

"""print(dataset)
print(type(dataset))
for linea in dataset:
    for columna in linea:
        print(dataset)
        
print(lis)"""
        
"""print(dataset)
print(type(dataset))
for linea in dataset:
    for columna in linea:
        print(linea,columna)"""

#bdexp = body exp
bdexp = pd.ExcelWriter(r'\Users\Santy\Desktop\ADSO 13\Trabajos visual estudio\tRABAJOS PANDAS\adso13r.xlsx', engine ='xlsxwriter')

dataset.to_excel(bdexp, sheet_name="resultad")
bdexp._save()
