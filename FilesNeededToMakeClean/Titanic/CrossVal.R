library(dplyr)
library(randomForest)
library(caret)

dataTrain = read.delim2('D:/Programowanie/R_Projects/Titanic/Trainc.csv', sep = ',', header = T, dec = ".", na.strings = "NA",stringsAsFactors=FALSE )
dataTest = read.delim2('D:/Programowanie/R_Projects/Titanic/Testc.csv', sep = ',', header = T, dec = ".", na.strings = "NA",stringsAsFactors=FALSE )

View(dataTrain)
y = dataTrain[,c('Survived')]


C1 = y
C2 = y
class(C1)
class(C2)

indexes = 1:nrow(dataTrain)

C1 = data.frame(indexes,y)

C1$indexes = NULL
df$x <- NULL
C2 = data.frame(indexes, y)





View(indexes)
