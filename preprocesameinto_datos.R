# plantilla para el preprocesamiento de datos
#importar el dataset
dataset = read.csv('Data.csv')
#dataset = dataset[,2:3]
#tratamiento de los valores NA
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age,FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)#$ es para ver cuales on las columnas dentro del dataframe

# si dentro de datastet en la columna año es nan, condición es verdadero,
#se pone después de la primer coma, y falso en el segundo, si es verdadero se 
#sustituye por la media, tomando todos los valores de la columna menos los nan.
dataset$Salary = ifelse(is.na(dataset$Salary),
                     ave(dataset$Salary,FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Salary)
View(dataset)
#codificar las variables categóricas
dataset$Country = factor(dataset$Country,
                         levels = c("France","Spain","Germany"),
                         labels = c(1, 2, 3))
dataset$Purchased = factor(dataset$Purchased,
                         levels = c("No","Yes"),
                         labels = c(0, 1))

#dividir los datos en conjuntos de entrenamiento y test

install.packages("caTools")
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)# se toma un 80% para entrenamiento
training_set = subset(dataset, split ==TRUE)
testing_set = subset(dataset, split == FALSE) # del split creado, tomar ese vector y solamente el False
#escalando valores
training_set[,2:3] = scale(training_set[,2:3])
testing_set[,2:3] = scale(testing_set[,2:3])
