#arbol de decision para regresi髇
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


# Escalado de valores #cuando se usan distancias euclideas
# training_set[,2:3] = scale(training_set[,2:3])
# testing_set[,2:3] = scale(testing_set[,2:3])

# Ajustar Modelo de Regresi贸n con el Conjunto de Datos
library(rpart)
regression = rpart(formula = Salary ~ .,
                   data = dataset,
                   control = rpart.control(minsplit = 1))



# Predicci贸n de nuevos resultados con Regresi贸n de arboles de decision
y_pred = predict(regression, newdata = data.frame(Level = 6.5))



# Visualizaci贸n del modelo de regresion arbol de decisi髇
# install.packages("ggplot2")
library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)#generar datos intermedios de 0,1 a 0,1 para que se vea m醩 fluido el gr醘ico
ggplot() +
  geom_point(aes(x = dataset$Level , y = dataset$Salary),
             color = "red") +
  geom_line(aes(x = x_grid, y = predict(regression, 
                                        newdata = data.frame(Level = x_grid))),
            color = "blue") +
  ggtitle("Predicci贸n (Modelo de Regresi贸n de arbol de decision)") +
  xlab("Nivel del empleado") +
  ylab("Sueldo (en $)")