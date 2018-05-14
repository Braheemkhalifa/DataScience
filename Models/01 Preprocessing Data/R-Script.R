
DS= read.csv('Data.csv')
DS$Age=ifelse(is.na(DS$Age),ave(DS$Age,FUN = function(x) mean(x,na.rm = TRUE)),DS$Age)
DS$Salary=ifelse(is.na(DS$Salary),ave(DS$Salary,FUN = function(x) mean(x,na.rm = TRUE)),DS$Salary)

DS$Country=factor(DS$Country,levels = c('Spain','France','Germany'),labels = c(1,2,3))
DS$Purchased=factor(DS$Purchased,levels = c('No','Yes'),labels = c(0,1))


set.seed(123)
split = sample.split(DS$Purchased,SplitRatio = 0.8)

training_set = subset(DS,split==TRUE)
test_set = subset(DS,split==FALSE)

# 
# training_set[,2:3]=scale(training_set[,2:3])
# test_set[,2:3]=scale(test_set[,2:3])