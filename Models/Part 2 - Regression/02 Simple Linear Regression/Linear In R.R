#Simple Linear Regression 


#Import Data
DS= read.csv('Salary_Data.csv')

#Split Data 
#install.package('catools')
set.seed(123)
split = sample.split(DS$Salary,SplitRatio = 2/3)
training_set = subset(DS,split==TRUE)
test_set = subset(DS,split==FALSE)

#Fitting Simple linear Regression in Training set
regressor = lm(formula = Salary ~ YearsExperience ,data = training_set)

#Predicted the test set of result 
y_pred = predict(regressor, newdata = test_set)


#visualizing the training set result
#install.pacages('ggplot2')

ggplot() +
geom_point( aes(x=training_set$YearsExperience,y=training_set$Salary),color='blue') +
geom_line(   aes(x=training_set$YearsExperience,y=predict(regressor, newdata = training_set)), 
      color='green') +
ggtitle('Salary vs Experience ( training data)') + 
  xlab('Years of Experience') + ylab('Salary')

#visualizing the training set result

ggplot() +
  geom_point( aes(x=test_set$YearsExperience,y=test_set$Salary),color='blue') +
  geom_line(   aes(x=training_set$YearsExperience,y=predict(regressor, newdata = training_set)), 
               color='green') +
  ggtitle('Salary vs Experience ( training data)') + 
  xlab('Years of Experience') + ylab('Salary')

