import pandas as pd
import numpy as np
from os import system
import matplotlib.pyplot as plt

df = pd.read_excel(r'C:\Users\ADSI\Music\Datos\XX\Ventas.xlsx', sheet_name='Datos')

serie = pd.Series(df.to_numpy().tolist())
def graficar():
    lisGra = []
    t1,t2,t3,t4,t5,t6,t7,t8 = [],[],[],[],[],[],[],[]

    for j in range(0, len(serie)):

        if serie[j][0] == 'SAO_53':
            t1.append(serie[j][5] * serie[j][6])
        elif serie[j][0] == 'SAO_57':
            t2.append(serie[j][5] * serie[j][6])
        elif serie[j][0] == 'SAO_58':
            t3.append(serie[j][5] * serie[j][6])
        elif serie[j][0] == 'SAO_92':
            t4.append(serie[j][5] * serie[j][6])
        elif serie[j][0] == 'SAO_93':
            t5.append(serie[j][5] * serie[j][6])
        elif serie[j][0] == 'SAOVia_40':
            t6.append(serie[j][5] * serie[j][6])
        elif serie[j][0] == 'SAOVia_43':
            t7.append(serie[j][5] * serie[j][6])
        elif serie[j][0] == 'SAOVia_48':
            t8.append(serie[j][5] * serie[j][6])

    lisGra.append(sum(t1))
    lisGra.append(sum(t2))
    lisGra.append(sum(t3))
    lisGra.append(sum(t4))
    lisGra.append(sum(t5))
    lisGra.append(sum(t6))
    lisGra.append(sum(t7))
    lisGra.append(sum(t8))

    serieY = ['SAO_53','SAO_57','SAO_58','SAO_92',
            'SAO_93','SAOVia_40','SAOVia_43','SAOVia_48']

    fig, ax = plt.subplots()
    ax.bar(serieY,lisGra)
    plt.show()
