##Apriori

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

# entrenar algoritmo Apriori con el dataet
rules = apriori(data = dataset,
                parameter = list(support =0.004, confidence = 0.2))

#viualización de resultado
inspect(sort(rules, by = 'lift')[1:10])
plot(rules, method = "graph", engine = "htmlwidget")

              
