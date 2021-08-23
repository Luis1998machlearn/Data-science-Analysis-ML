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

# Ajustar Modelo de SVR con el Conjunto de Datos
install.packages("e1071")
library(e1071)
regression = svm(formula= Salary ~ .,
                 data = dataset,
                 type = "eps-regression",
                 kernel = "radial")

# Predicci贸n de nuevos resultados con Regresi贸n SVR
y_pred = predict(regression, newdata = data.frame(Level = 6.5))



# Visualizaci贸n del modelo de regresi贸n SVR
# install.packages("ggplot2")
library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)#generar datos intermedios de 0,1 a 0,1 para que se vea m醩 fluido el gr醘ico
ggplot() +
  geom_point(aes(x = dataset$Level , y = dataset$Salary),
             color = "red") +
  geom_line(aes(x = dataset$Level, y = predict(regression, 
                                        newdata = data.frame(Level = dataset$Level))),
            color = "blue") +
  ggtitle("Predicci贸n (Modelo de Regresi贸n SVR)") +
  xlab("Nivel del empleado") +
  ylab("Sueldo (en $)") #valores at韕icos menospreciados por el modelo