#Multiple Linear Regression

DS= read.csv('50_Startups.csv')

#Encoing Categorical Variables
DS$State=factor(DS$State,levels = c('New York','California','Florida')
                  ,labels = c(1,2,3))

#Split Data 

set.seed(123)
split = sample.split(DS$Profit,SplitRatio = 0.8)
training_set = subset(DS,split==TRUE)
test_set = subset(DS,split==FALSE)

#Fitting Simple linear Regression in Training set
regressor = lm(formula = Profit ~. ,data = training_set)

#Predicted the test set of result 
y_pred = predict(regressor, newdata = test_set)

#builing the optimal model using backar elimination 

regressor = lm(formula = Profit ~R.D.Spend +Administration+Marketing.Spend+State,data = DS)
summary(regressor)

regressor = lm(formula = Profit ~R.D.Spend +Administration+Marketing.Spend,data = DS)
summary(regressor)

regressor = lm(formula = Profit ~R.D.Spend+Marketing.Spend,data = DS)
summary(regressor)

regressor = lm(formula = Profit ~R.D.Spend,data = DS)
summary(regressor)