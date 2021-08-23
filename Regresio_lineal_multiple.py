# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 18:26:01 2021

@author: hp
"""
#regresion lineal multiple
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv("50_Startups.csv")
X = dataset.iloc[:, :-1].values # index localitation, values es para solo valores
y = dataset.iloc[:, 4].values

#Codificar datos categóricos
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])

onehotencoder = OneHotEncoder(categorical_features=[3])
X = onehotencoder.fit_transform(X).toarray()
#Evitar trampa de variables dummy multicolinealidad
X = X[:,1:]
#dividir el dataset en conjunto de entranamiento y testing
from sklearn.cross_validation import train_test_split # función que nos permite dividir dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
#ajustar el modelo de regresión lineal multiple con el conjunto de entrenamiento
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(X_train, y_train)

#predicción de los resultados en el conjunto de testing
y_pred = regression.predict(X_test)

#construir el modelo optimo utilizando eliminación hacia atrás
import statsmodels.formula.api as sm #columna de 1 toma el valor de los coeficientes
#numpy manejo de estructura de datos
X = np.append(arr = np.ones((50,1)).astype(int), values = X, axis=1) #axis columna, para medir el p valor de los coeficientes
SL = 0.05

X_opt = X[:,[0,1,2,3,4,5]]#solo dejaremos las variables estadísticamente significativo
regression_OLS = sm.OLS(endog=y,exog= X_opt).fit()
regression_OLS.summary()

#elimino la de p mayor, es decir, x2
X_opt = X[:,[0,1,3,4,5]]#solo dejaremos las variables estadísticamente significativo
regression_OLS = sm.OLS(endog=y,exog= X_opt).fit()
regression_OLS.summary()
#eliminamos ahora x1
X_opt = X[:,[0,3,4,5]]#solo dejaremos las variables estadísticamente significativo
regression_OLS = sm.OLS(endog=y,exog= X_opt).fit()
regression_OLS.summary()
#eliinamos x2 que es en realidad el 4
X_opt = X[:,[0,3,5]]#solo dejaremos las variables estadísticamente significativo
regression_OLS = sm.OLS(endog=y,exog= X_opt).fit()
regression_OLS.summary()

#Ahora eliminamos la 5
X_opt = X[:,[0,3]]#solo dejaremos las variables estadísticamente significativo
regression_OLS = sm.OLS(endog=y,exog= X_opt).fit()
regression_OLS.summary()
#el mejor predictor es utilizar el gasto de marketing, la única que quedó

#Eliminación de variables de manera automátizada utilizando solamente p valores
"""import statsmodels.formula.api as sm
def backwardElimination(x, sl):    
    numVars = len(x[0])    
    for i in range(0, numVars):        
        regressor_OLS = sm.OLS(y, x.tolist()).fit()        
        maxVar = max(regressor_OLS.pvalues).astype(float)        
        if maxVar > sl:            
            for j in range(0, numVars - i):                
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):                    
                    x = np.delete(x, j, 1)    
    regressor_OLS.summary()    
    return x 
 
SL = 0.05
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
X_Modeled = backwardElimination(X_opt, SL)"""
#Eliminación de variables utilizando p-valor y R cuadrado justado
"""import statsmodels.formula.api as sm
def backwardElimination(x, SL):    
    numVars = len(x[0])    
    temp = np.zeros((50,6)).astype(int)    
    for i in range(0, numVars):        
        regressor_OLS = sm.OLS(y, x.tolist()).fit()        
        maxVar = max(regressor_OLS.pvalues).astype(float)        
        adjR_before = regressor_OLS.rsquared_adj.astype(float)        
        if maxVar > SL:            
            for j in range(0, numVars - i):                
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):                    
                    temp[:,j] = x[:, j]                    
                    x = np.delete(x, j, 1)                    
                    tmp_regressor = sm.OLS(y, x.tolist()).fit()                    
                    adjR_after = tmp_regressor.rsquared_adj.astype(float)                    
                    if (adjR_before >= adjR_after):                        
                        x_rollback = np.hstack((x, temp[:,[0,j]]))                        
                        x_rollback = np.delete(x_rollback, j, 1)     
                        print (regressor_OLS.summary())                        
                        return x_rollback                    
                    else:                        
                        continue    
    regressor_OLS.summary()    
    return x 
 
SL = 0.05
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
X_Modeled = backwardElimination(X_opt, SL)"""
