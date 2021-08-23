# Importar el dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[, 2:3]

# Dividir los datos en conjunto de entrenamiento y conjunto de test
# install.packages("caTools")
# library(caTools)
# set.seed(123)
# split = sample.split(dataset$Purchased, SplitRatio = 0.8)
# training_set = subset(dataset, split == TRUE)
# testing_set = subset(dataset, split == FALSE)

# Escalado de valores
# training_set[,2:3] = scale(training_set[,2:3])
# testing_set[,2:3] = scale(testing_set[,2:3])

# ajustar modelo de regresion lineal con el conjunto de datos
lin_reg = lm(formula = Salary ~ .,
             data = dataset)


# ajustar el modelo de regresión polinómica con el conjunto de datos
dataset$Level2 = dataset$Level^2
dataset$Level3 = dataset$Level^3
dataset$Level4 = dataset$Level^4
poly_reg = lm(formula = Salary ~ .,
              data = dataset)
#visualizacion modelo lineal
library(ggplot2)
ggplot() +
  geom_point(aes(x=dataset$Level, y= dataset$Salary),
             color = "red") +
  geom_line(aes(x= dataset$Level,y=predict(lin_reg, newdata = dataset)),
            color = "blue") +
  ggtitle("prediccion lineal del sueldo en funcion del nivel del empleado") +
  xlab("nivel del empleado") +
  ylab("sueldo en $")
#visualización de modelo polinomico
ggplot() +
  geom_point(aes(x=dataset$Level, y= dataset$Salary),
             color = "red") +
  geom_line(aes(x= dataset$Level,y=predict(poly_reg, newdata = dataset)),
            color = "blue") +
  ggtitle("prediccion polinomico del sueldo en funcion del nivel del empleado") +
  xlab("nivel del empleado") +
  ylab("sueldo en $")
#prediccion de nuevos resultados con regresion lineal
y_pred = predict(lin_reg, newdata = data.frame(Level= 6.5))#hay que crear un dataframe en R para una nueva prediccion
#prediccion de nuevos resultados con regresion polinomica
y_pred_poli = predict(poly_reg, newdata = data.frame(Level= 6.5,
                                                     Level2 = 6.5^2,
                                                     Level3 = 6.5^3,
                                                     Level4 = 6.5^4))
