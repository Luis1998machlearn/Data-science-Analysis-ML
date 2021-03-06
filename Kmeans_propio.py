# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 22:56:09 2021

@author: hp
"""
#K-means
# Cómo importar las librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar el data set
dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:,[3,4]].values  

#métodod del codo para averiuar número óptimo de cluster
from sklearn.cluster import KMeans
wcss = []
for i in range (1, 11):
    kmeans = KMeans(n_clusters = i, init = "k-means++", max_iter= 300, n_init = 10, random_state = 0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11), wcss)
plt.title("método del codo")
plt.xlabel("numero de clusters")
plt.ylabel("wcss(k)")
plt.show()

#aplicar el método de k-means para segmentar el dataset
kmeans = KMeans(n_clusters = 5, init = "k-means++", max_iter=300, n_init = 10, random_state = 0)
y_kmeans = kmeans.fit_predict(X)

#gráfico de clusters
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 100, c = "red", label = "cauto")
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 100, c = "blue", label = "estandar")
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 100, c = "green", label = "objetivo")
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = "cyan", label = "descuidados")
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = "magenta", label = "conservadores")
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s = 300, c = "yellow", label = "Baricentros")
plt.title("cluster de clientes")
plt.xlabel("Ingresos anuales en $")
plt.ylabel("puntuación en gastos (1-100)")
plt.legend()
plt.show()