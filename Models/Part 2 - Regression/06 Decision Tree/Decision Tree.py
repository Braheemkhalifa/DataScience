#Polynominal Decision Tree 

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 


#importing Data: 

DataSet = pd.read_csv('Position_Salaries.csv')
x = DataSet.iloc[:,1:2].values
y = DataSet.iloc[:,-1].values



#Fitting Decision Tree  Model :

from sklearn.tree import DecisionTreeRegressor 
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(x,y)


#predict Decision Tree  

y_pred = regressor.predict(6.5)


#Visualizing  The   Decision Tree  :￼

plt.scatter(x,y,color='Blue')
plt.plot(x,regressor.predict(x),color='yellow')
plt.title('Decision Tree')
plt.xlabel('Levels')
plt.ylabel('Salary')
plt.show()


#Visualizing  Decision Tree :(for higher resolution)
x_grid = np.arange(min(x),max(x),0.01)
x_grid = x_grid.reshape((len(x_grid),1))
plt.scatter(x,y,color='Blue')
plt.plot(x_grid,regressor.predict(x_grid),color='yellow')
plt.title('Decision Tree')
plt.xlabel('Levels')
plt.ylabel('Salary')
plt.show()



