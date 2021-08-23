# Importar el dataset
dataset = read.csv("50_Startups.csv")
#dataset = dataset[, 2:3]
# Codificar las variables categÃ³ricas
dataset$State = factor(dataset$State,
                         levels = c("New York", "California", "Florida"),
                         labels = c(1, 2, 3))

# Dividir los datos en conjunto de entrenamiento y conjunto de test
# install.packages("caTools")
library(caTools)
set.seed(123)
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)

# Escalado de valores
# training_set[,2:3] = scale(training_set[,2:3])
# testing_set[,2:3] = scale(testing_set[,2:3])

#en R hace automático lo de vairbales dummy.
#Ajustar el modelo de regresion lineal multiple con el conjunto de entrenamiento
regression = lm(formula = Profit ~ .,
                data = training_set) #en lugar de escribri todas las variables independientes, se pone . y ~ es en funcion de


#probar el modelo, predecir los resulados con el conjunto de test

y_pred = predict(regression, newdata = testing_set)

#construir un modelo óptimo con la eliminación hacia atrás
SL = 0.05
regression = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State,
                data = dataset)
summary(regression)
#eliminando state 2
regression = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend ,
                data = dataset)
summary(regression)
#eliminando administration
regression = lm(formula = Profit ~ R.D.Spend + Marketing.Spend ,
                data = dataset)
summary(regression)

#install.packages("https://cran.r-project.org/src/contrib/Archive/ElemStatLearn/ElemStatLearn_2015.6.26.2.tar.gz",repos=NULL, type="source")
#Automatizar la eliminacion de variables
"""backwardElimination <- function(x, sl) {
  numVars = length(x)
  for (i in c(1:numVars)){
    regressor = lm(formula = Profit ~ ., data = x)
    maxVar = max(coef(summary(regressor))[c(2:numVars), "Pr(>|t|)"])
    if (maxVar > sl){
      j = which(coef(summary(regressor))[c(2:numVars), "Pr(>|t|)"] == maxVar)
      x = x[, -j]
    }
    numVars = numVars - 1
  }
  return(summary(regressor))
}

SL = 0.05
dataset = dataset[, c(1,2,3,4,5)]
backwardElimination(training_set, SL"""