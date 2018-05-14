#Polynominal Linear Regression

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 


#importing Data: 

DataSet = pd.read_csv('Position_Salaries.csv')
x = DataSet.iloc[:,1:2].values
y = DataSet.iloc[:,-1].values



#Fitting Simple linear Regression in Training set

from sklearn.linear_model import LinearRegression
linear_regressor = LinearRegression()
linear_regressor.fit(x,y) 


#Fitting Polynominal linear Regression in Training set

from sklearn.preprocessing import PolynomialFeatures
poly_regressor = PolynomialFeatures(degree=4)
x_poly = poly_regressor.fit_transform(x)


linear_regressor2 = LinearRegression()
linear_regressor2.fit(x_poly,y)


#Visualizing  The Linear Regression :￼

plt.scatter(x,y,color='Blue')
plt.plot(x,linear_regressor.predict(x),color='yellow')
plt.title('Linear Regression')
plt.xlabel('Levels')
plt.ylabel('Salary')
plt.show()


#Visualizing  The  Polynominal Linear Regression :￼
x_grid = np.arange(min(x),max(x),0.1)
x_grid = x_grid.reshape((len(x_grid),1))

plt.scatter(x,y,color='Blue')
plt.plot(x_grid,linear_regressor2.predict(poly_regressor.fit_transform(x_grid)),color='yellow')
plt.title('Polynominal Linear Regression with grid to make carve better')
plt.xlabel('Levels')
plt.ylabel('Salary')
plt.show()



#predict the linear regression 

linear_regressor.predict(6.5)


#predict the Polynominal linear regression 

linear_regressor2.predict(poly_regressor.fit_transform(6.5))





