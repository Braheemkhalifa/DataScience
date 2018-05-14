#Polynominal Linear SVR

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 


#importing Data: 

DataSet = pd.read_csv('Position_Salaries.csv')
x = DataSet.iloc[:,1:2].values
y = DataSet.iloc[:,2:3].values



#Feature Scalling

from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
sc_y = StandardScaler()
x = sc_x.fit_transform(x)
y = sc_y.fit_transform(y) 
#y = DataSet.iloc[:,2:3].values

#Fitting   SVR Model in Training set

from sklearn.svm import SVR
regressor = SVR(kernel= 'rbf')
regressor.fit(x,y)





#predict the SVR

y_pred = sc_y.inverse_transform(regressor.predict(sc_x.transform( np.array(  [[6.5]]  ))) )

#Visualizing  The   SVR :￼
x_grid = np.arange(min(x),max(x),0.1)
x_grid = x_grid.reshape((len(x_grid),1))￼

plt.scatter(x,y,color='Blue')
plt.plot(x_grid,regressor.predict(x_grid),color='red')
plt.title('SVR Model')
plt.xlabel('Levels')
plt.ylabel('Salary')
plt.show()




