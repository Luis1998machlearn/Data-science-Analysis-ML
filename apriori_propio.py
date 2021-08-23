# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 11:34:59 2021

@author: hp
"""
#apriori
#librerias necesarias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importar dataset
dataset = pd.read_csv("Market_Basket_Optimisation.csv", header = None)
transactions = [] #hacindo una lista de pthon vacía
for i in range(0, 7501):#bucle para recorrer cada una de las transacciones
    transactions.append([str(dataset.values[i, j]) for j in range(0,20)]) #para hacer uan lista con los elemntrs y conforman un nuevo objeto de las transacciones
    
#entrenar el algoritmo de apriori
from apyori import apriori
rules = apriori(transactions, min_support = 0.003 , min_confidence = 0.2, 
                min_lift = 3 , min_length = 2)
#visualizacion de los resultado
results = list(rules)
results[2]