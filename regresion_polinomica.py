# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 16:01:34 2021

@author: hp
"""
#regresion polinómica
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar el data set
dataset = pd.read_csv("Position_Salaries.csv")
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

#no se necesita dividir el dataset porque no tendría sentido, son muy pocos.
#no hay que escalar, porque queremos más bien ver la relaciónes no lineales con polinomial

#ajustar la regresion lineal com dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

#ajustar la regresion polinómica con el dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)#qué pasaría si le agrego grado 3 0 4?, se mejora con 3, y se mejora más con grado 4
X_poly = poly_reg.fit_transform(X)#transformación polinómica.
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

#visualización de los resultados del modelo lineal
plt.scatter(X, y, color="red")
plt.plot(X, lin_reg.predict(X), color="blue")#predecir valores para el conjunto de datos x
plt.title("modelo de regresion lineal")
plt.xlabel("posicion del empleado")
plt.ylabel("sueldo en $")
plt.show()
#visualización de los resultados del modelo POLINOMICO
X_grid = np.arange(min(X), max(X), 0.1) #para hacer puntos intermedios y que no se vea como rectas, si no con suavidad
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y, color="red")
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color="blue")#predecir valores para el conjunto de datos x_poly solo al modelo de predicción.
plt.title("modelo de regresion polinómica")
plt.xlabel("posicion del empleado")
plt.ylabel("sueldo en $")
plt.show()

#prediccion de nuestros modelos
lin_reg.predict(6.5)


lin_reg_2.predict(poly_reg.fit_transform(6.5))#meter un valor para ver cómo está el modelo.
