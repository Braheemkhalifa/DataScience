#logistic K-Means Clustering  : 

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 


#importing Data: 

DataSet = pd.read_csv('Mall_Customers.csv')
x = DataSet.iloc[:,3:5].values


#using the elblow method  to find the optimal number of k

from sklearn.cluster import KMeans
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i, init ='k-means++', max_iter=300 , n_init=10 ,random_state=0 )
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.title('The Elblow Method')
plt.xlabel('Number of cluster')
plt.ylabel('WCSS')
plt.show()


''''
كده عرفت ان افضل k هو 5 
'''

#applying the cluster method:

kmeans = KMeans(n_clusters=5, init ='k-means++', max_iter=300 , n_init=10 ,random_state=0 )
y_kmeans = kmeans.fit_predict(x)


#visualization of clusters 

plt.scatter(x[y_kmeans==0,0],x[y_kmeans==0,1],s=100,c='red',label='c1')
plt.scatter(x[y_kmeans==1,0],x[y_kmeans==1,1],s=100,c='blue',label='c2')
plt.scatter(x[y_kmeans==2,0],x[y_kmeans==2,1],s=100,c='green',label='c3')
plt.scatter(x[y_kmeans==3,0],x[y_kmeans==3,1],s=100,c='yellow',label='c4')
plt.scatter(x[y_kmeans==4,0],x[y_kmeans==4,1],s=100,c='orange',label='c5')

plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=100 ,c='cyan',label='centroid')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()








