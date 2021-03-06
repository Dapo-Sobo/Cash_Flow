#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 21:48:59 2020

@author: ibidapo
"""

#Chapter 5 K-Nearest Neighbors Algorithms

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Loading the IRS Data SET
iris = pd.read_csv("iris.csv")
iris.head()

#X & Y

X = iris.iloc[:,:-1].values
y = iris.iloc[:,4].values

#Splitting the Dataset into testing and training data

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20)

#Feature Scaling
from sklearn.preprocessing import StandardScaler
feature_scaler=StandardScaler()
feature_scaler.fit(X_train)
X_train = feature_scaler.transform(X_train)
X_test = feature_scaler.transform(X_test)


#Training the algorightm
from sklearn.neighbors import KNeighborsClassifier
knn_classifier = KNeighborsClassifier(n_neighbors=2)
knn_classifier.fit(X_train,y_train)


#Prediction

from sklearn.metrics import confusion_matrix, classification_report
pred_y=knn_classifier.predict(X_test)

#Evaluating the Accuracy of the Algorithm

print(confusion_matrix(y_test,pred_y))
print(classification_report(y_test,pred_y))

#Comparing K value with the Error Rate
error=[]
# K values range between 1 and 40
#Iterating the mean error for the predicted value of the test set 
for x in range(1,40):
    knn=KNeighborsClassifier(n_neighbors=x)
    knn.fit(X_train,y_train)
    pred_x=knn.predict(X_test)
    error.append(np.mean(pred_x != y_test))
    
print(error)


plt.figure(figsize=(12,6))
plt.plot(range(1,40), error, color='blue',linestyle='dashed', marker="o",
         markerfacecolor='blue',markersize = 10)
plt.title('Error rate for K')
plt.xlabel('K Values')
plt.ylabel("Mean Error")
plt.show()
                      
#