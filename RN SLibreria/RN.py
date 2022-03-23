from cmath import sqrt
import math
from tkinter import W
import numpy as np
import random as rand
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import csv

X = []
Y = []

# Lectura del dataset
def leerDataset():
    tempX = []
    tempY = []
    tempXY = []

    with open('datasetP1.csv', newline='') as File:  
        reader = csv.reader(File)
        auxLit = []
        listaDatos = []
        listaDatosY = []
        listaDatosX = []
        for row in reader:
            for datos in row:
                auxLit.append(datos)

            # Añadimos las columnas del dataset en una lista individual
            # listaDatos.append(int(auxLit[0]))
            #Estraer todos los datos de Y
            listaDatosY.append(float(auxLit[1]))
            # Adicion del BIAS en los datos de las X y extraccion
            listaDatosX.append([1, int(auxLit[0])])
            auxLit = [] 
            listaDatos = []

    print("listaDatos X", listaDatosX)
    print("listaDatos Y", listaDatosY)

    # Se meten los datos en un array para el manejo de los floats
    # tempX = np.array(listaDatos, dtype=float)
    # tempY = np.array(listaDatosY, dtype=float)

    # Se juntan los arreglos de X y Y
    tempXY = [listaDatosX, listaDatosY]

    # Y se retorna la lista unida
    return tempXY

def datos():
    global X
    global Y
    XY = leerDataset()
    X = XY[0]
    Y = XY[1]

    print("X: ", X)
    print("Y: ", Y)

    # Transpuesta de X
    X = np.array(X).transpose()
    Y = np.array(Y)

# def ponderacion(w):
#     print(float(w[0]))
#     wk = np.array([(float(w[0]), float(w[1]), float(w[2]))])
#     print(wk)
#     return wk

def calculos(ns, wk):
    # Asignacion de X y Y con array
    datos()
    errorK = []
    k = 0
    generaciones = []
    # n = ns
    # wk = ponderacion(ws)
    # 0.854,0.327,0.558,0.456,0.541,0.78

    # Se ejecutara hasta que el maximo error sea menor a 0.1
    while(True):
        k += 1

        # Multiplicacion de la wk con la X y se obtiene uk
        uk = np.dot(wk,X)

        # yck = np.array([0 if uk[0][i] < 0 else 1  for i in range(len(uk[0]))])

        # Funsion de activacion -> Igualacion de Uk para la Y calculada
        yck = uk

        # error calculado es igual a la resta de la Y con la Y calculada
        ek = Y - yck

        # Obtener el error maximo con base a ek
        errorMax = max(ek)

        # Hacer transpuesta para ek
        ek = ek.transpose()

        # Obtener multiplicacion de X con la ek y el resultado multiplicar con ns
        tempDotX = np.dot(X, ek) * ns

        # Suma de wk mas la temporal de X para obtener la ultima W
        wt = wk + tempDotX

        raiz = 0

        #Obtener raiz de ek
        for i in range(len(ek)):
            raiz += ek[i]**2

        wk = wt
        print(errorMax)
        errorK.append((math.sqrt(raiz)))
        # Numero de veces que se itero el While
        generaciones.append(k)

        if  errorMax < 0.1:
            print('Calculando Y: ',yck)
            print('==== GENERACIONES ====')
            print(k)
            return errorK, generaciones, wk
        
def iteraciones(n1, wk):
    ns = ["N1"]
    wks = []
    errores = []
    generaciones = []
    for i in range(1):
        print("----Numero ",i+1 ,"----")
        n1 = float(n1)
        datos = calculos(n1, wk)
        errores.append(datos[0])
        generaciones.append(datos[1])
        wks.append(datos[2])
        
    # print("Errores: ", errores)
    # print("Num Errores: ", numErrores)

    figure2 = plt.figure(figsize=(20, 8))

    ax = plt.subplot(1,2,1)

    ax.set_title('Grafica')
    for x in range(len(errores)):
        ax.plot(generaciones[x], errores[x], marker='o',label=f'N = {x+1}')

    ax.legend()


    ax2 = plt.subplot(1,2,2)
    ax2.axis('tight')
    ax2.axis('off')

    table = [['η','Ultimos pesos de W']]
    # print(wks[0][0])
        
    for y in range(len(ns)):   
        tableTemp = []
        tableTemp.append(ns[0])
        tableTemp.append(wks[y])
        
        table.append(tableTemp)

    table = ax2.table(cellText = table, loc = 'center', cellLoc = 'center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(0.5,1)

    plt.tight_layout()

    plt.show()

# entrada = 0.000001
# entrada1 = [0.451, 0.457]
# leerDataset()
# iteraciones(entrada, entrada1)
