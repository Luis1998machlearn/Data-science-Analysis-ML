# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 11:17:37 2021

@author: hp
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("Data.csv")
X = dataset.iloc[:, :-1].values # index localitation, values es para solo valores
y = dataset.iloc[:, 3].values #esta es la coumna de predicción
### para limpieza o tratameinto de nan
#1- si no conosco un dato, elimino toda la fila y paso a tener menos, pero es muy peligroso.
#2- idea más común, reemplazar por la media
#tratamiento de NAs
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values="NaN",strategy="mean",axis=0) #por columna 0 y fila 1, y nan son las que se queiren cambiar
imputer = imputer.fit(X[:,1:3])#para tomar la columna 2 y 3, esto es para definir cuáles cambiar
X[:, 1:3] = imputer.transform(X[:, 1:3]) # sobreescribir los valores desconocidos, transform devuelve y sustituye la información de los valores desconocidos 
X
# codificar datos categóricos
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
X
X
onehotencoder = OneHotEncoder(categorical_features=[0])
X = onehotencoder.fit_transform(X).toarray()# hot encoder es para datos dummy, porque francia 1 no significa nada que USA sea 2.
X
labelencoder_y = LabelEncoder()
y =labelencoder_y.fit_transform(y)
y
#dividir el dataset en conjunto de entranamiento y testing
from sklearn.cross_validation import train_test_split # función que nos permite dividir dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)# se utiliza un 80% para entrenamiento
 ## si el rango de valores es mucho más grande, puede ser un problema, por ejemplo, edad vrs salario.
 #escalar es la solución, poner el mayor como 1 y el menor como 0, y de ahí en escalar.
 #Standarización= x-mean/desviación standar (campana de gauss, muchos valores cercano de 0, entorno a la media, todo lo cercano al valor medio de la columna es mas cercano a 0)
 # normalización es; x-min/max-min(menor se convierte en 0 y el mayor en 1), el resto escalado de forma lineal
  #escalado de variables
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test) ##esto es para estandarzación
# la dummy se escala o no?? ambas están bien, la y? si es clasificación no y predicción sí



