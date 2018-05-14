#Multiple Linear Regression 

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 


#importing Data: 

DataSet = pd.read_csv('50_Startups.csv')
x = DataSet.iloc[:,:-1].values
y = DataSet.iloc[:,-1].values

#Encoding Catigorical Data:

from sklearn.preprocessing import OneHotEncoder , LabelEncoder
labelencoder_x = LabelEncoder()
x[:, 3]=labelencoder_x.fit_transform(x[:,3])
oneHotEnoder = OneHotEncoder(categorical_features=[3])
x=oneHotEnoder.fit_transform(x).toarray()

#avoiding dummy variable trap

x=x[:,1:]

#Splitting DataSet into Training Set and Test:

from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=1/5,random_state=0)


#Fitting Simple linear Regression in Training set

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)


#Predicted th test set result

y_pred = regressor.predict(x_test)

#Bulding the optimal model using ( backward elimintation preperation ) 
import statsmodels.formula.api as sm
x = np.append(arr = np.ones((50,1)).astype(int),values = x , axis = 1 )

x_optimal = x[:,[0,1,2,3,4,5]]
regressor_osl = sm.OLS(endog=y,exog=x_optimal).fit()
regressor_osl.summary()

x_optimal = x[:,[0,1,3,4,5]]
regressor_osl = sm.OLS(endog=y,exog=x_optimal).fit()
regressor_osl.summary()

x_optimal = x[:,[0,3,4,5]]
regressor_osl = sm.OLS(endog=y,exog=x_optimal).fit()
regressor_osl.summary()

x_optimal = x[:,[0,3,5]]
regressor_osl = sm.OLS(endog=y,exog=x_optimal).fit()
regressor_osl.summary()

x_optimal = x[:,[0,3]]
regressor_osl = sm.OLS(endog=y,exog=x_optimal).fit()
regressor_osl.summary()



