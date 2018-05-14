import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 


#importing Data: 

DataSet = pd.read_csv('Data.csv')
x = DataSet.iloc[:,:-1].values
y = DataSet.iloc[:,-1].values

#Take of Missing Data :

from sklearn.preprocessing import Imputer 
imputer = Imputer(missing_values="NaN",strategy="mean",axis=0)
imputer = imputer.fit(x[:,1:3])
x[:,1:3] = imputer.transform(x[:,1:3])

#Encoding Catigorical Data:

from sklearn.preprocessing import OneHotEncoder , LabelEncoder
labelencoder_x = LabelEncoder()
x[:,0]=labelencoder_x.fit_transform(x[:,0])
oneHotEnoder = OneHotEncoder(categorical_features=[0])
x=oneHotEnoder.fit_transform(x).toarray()
labelencoder_y = LabelEncoder()
y=labelencoder_y.fit_transform(y)

#Splitting DataSet into Training Set and Test:

from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2 ,random_state=0)


#Feature Scalling

from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)









 
 