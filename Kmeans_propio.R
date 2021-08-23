# clustering K means

dataset = read.csv("Mall_Customers.csv")
X = dataset[,4:5]

#método del codo
set.seed(6)
wcss = vector()
for (i in 1:10){
  wcss[i] <- sum(kmeans(X, i)$withinss)
  
}
plot(1:10, wcss, type = 'b', main = "método del codo",
     xlab = "número de clusters", ylab = "WCSS")

#aplicar el algoritmo de k-means con k optimo
set.seed(29)
kmeans <- kmeans(X, 5, iter.max = 300, nstart = 10)

#visualización de clusters
library(cluster)
clusplot(X, 
         kmeans$cluster,
         lines = 0,
         shade = TRUE,
         color = TRUE,
         labels = 1, 
         plotchar = FALSE,
         span = TRUE,
         main = "clustering de clientes",
         xlab = "ingreoss anuales",
         ylab = "puntuación (1-100")