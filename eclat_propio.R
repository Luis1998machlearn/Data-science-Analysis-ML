# eclat

#preprocesamiento de datos
install.packages("arules")
library(arules)
install.packages("arulesViz")
library(arulesViz)
dataset = read.csv("Market_Basket_Optimisation.csv", header = FALSE) #header es porque no tiene encabezado

dataset = read.transactions("Market_Basket_Optimisation.csv",
                            sep = ",", rm.duplicates = TRUE)
summary(dataset)

itemFrequencyPlot(dataset, topN = 10)

# entrenar algoritmo eclat con el dataet
rules = eclat(data = dataset,
                parameter = list(support =0.004, minlen = 2))

#viualización de resultado
inspect(sort(rules, by = 'support')[1:10])


