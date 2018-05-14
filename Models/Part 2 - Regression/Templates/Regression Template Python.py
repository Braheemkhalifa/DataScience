#Polynominal Linear Regression

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 


#importing Data: 

DataSet = pd.read_csv('Position_Salaries.csv')
x = DataSet.iloc[:,1:2].values
y = DataSet.iloc[:,-1].values




"""

#Feature Scalling

from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test) 
"""

'''
#Splitting DataSet into Training Set and Test:

from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=1/5,random_state=0)
'''


#Fitting Regression Model in Training set
#regressor 




#predict the regression 

y_pred = regressor.predict(6.5)



#Visualizing  The   Regression :￼

plt.scatter(x,y,color='Blue')
plt.plot(x,regressor.predict(x),color='yellow')
plt.title('Regression Model')
plt.xlabel('Levels')
plt.ylabel('Salary')
plt.show()


#Visualizing  The   Regression :(for higher reolutions)
x_grid = np.arange(min(x),max(x),0.1)
x_grid = x_grid.reshape((len(x_grid),1))
plt.scatter(x,y,color='Blue')
plt.plot(x_grid,regressor.predict(x_grid),color='yellow')
plt.title('Regression Model')
plt.xlabel('Levels')
plt.ylabel('Salary')
plt.show()



