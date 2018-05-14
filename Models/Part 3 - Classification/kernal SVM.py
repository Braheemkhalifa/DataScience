#logistic Kernal SVM : 

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 


#importing Data: 

DataSet = pd.read_csv('Social_Network_Ads.csv')
x = DataSet.iloc[:,2:4].values
y = DataSet.iloc[:,-1].values


#Splitting DataSet into Training Set and Test:

from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=1/4,random_state=0)


#Feature Scalling

from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test) 


#Fitting SVM Model in Training set

from sklearn.svm import SVC
classifier=SVC(kernel='rbf' ,random_state=0)
classifier.fit(x_train,y_train)

#predict the result
y_pred = classifier.predict(x_test)

#Making the confusion Matrix

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)


#Visualizing  The  train :￼

from matplotlib.colors import ListedColormap

x_set , y_set = x_train , y_train

x1 , x2 = np.meshgrid( 
        
        np.arange(start = x_set[:,0].min()-1,stop = x_set[:,0].max()+1, step= 0.01 ),
        np.arange(start = x_set[:,0].min()-1,stop = x_set[:,0].max()+1, step= 0.01 )
        
                    )

plt.contourf(x1,x2,classifier.predict( 
                                       np.array([x1.ravel(),x2.ravel()]).T
                                     ).reshape(x1.shape),alpha= 0.75, cmap = ListedColormap(('blue','red'))
                                    )


plt.xlim(x1.min(),x1.max())
plt.ylim(x2.min(),x2.max())


for i , j in enumerate(np.unique(y_set)):
    
    plt.scatter(x_set[y_set==j,0],x_set[y_set==j,1],
                c =  ListedColormap(('blue','red'))(i) ,label=j)

plt.title('Kernal SVM (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()


#Visualizing  The  test :￼

from matplotlib.colors import ListedColormap

x_set , y_set = x_test , y_test

x1 , x2 = np.meshgrid( 
        
        np.arange(start = x_set[:,0].min()-1,stop = x_set[:,0].max()+1, step= 0.01 ),
        np.arange(start = x_set[:,0].min()-1,stop = x_set[:,0].max()+1, step= 0.01 )
        
                    )

plt.contourf(x1,x2,classifier.predict( 
                                       np.array([x1.ravel(),x2.ravel()]).T
                                     ).reshape(x1.shape),alpha= 0.75, cmap = ListedColormap(('blue','red'))
                                    )


'''
 كل الهبل اللى فوق دا عشان تلون الماب نفسها الاحمر معناه y والازرق n 
'''
plt.xlim(x1.min(),x1.max())
plt.ylim(x2.min(),x2.max())


for i , j in enumerate(np.unique(y_set)):
    
    plt.scatter(x_set[y_set==j,0],x_set[y_set==j,1],
                c =  ListedColormap(('blue','red'))(i) ,label=j)

plt.title(' kernal SVM (Test set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()


