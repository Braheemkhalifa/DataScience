import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 


#importing Data: 

DataSet = pd.read_csv('Salary_Data.csv')
x = DataSet.iloc[:,:-1].values
y = DataSet.iloc[:,-1].values


#Splitting DataSet into Training Set and Test:

from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=1/3 ,random_state=0)

"""
#Feature Scalling

from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test) 
"""


#Fitting Simple linear Regression in Training set

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)


#Predicted the test set of result 
y_pred = regressor.predict(x_test)


#Visualizing The Training Set Result:￼
plt.scatter(x_train,y_train,color='Blue')
plt.plot(x_train,regressor.predict(x_train),color='yellow')
plt.title('Salary vs Experience (Training Data)')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.show()
 
#Visualizing The Test Set Result:￼
plt.scatter(x_test,y_test,color='Blue')
plt.plot(x_train,regressor.predict(x_train),color='yellow')
plt.title('Salary vs Experience (Test Data)')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.show()
  
 
 
 
 
 
 
 
 
 