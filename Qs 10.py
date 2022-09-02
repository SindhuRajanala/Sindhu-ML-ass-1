import numpy as nm
import pandas as pd
from sklearn import preprocessing
from sklearn import utils 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import confusion_matrix
X = nm.array([[1,0], [2,0],[3,0],[6,0],[6,0],[7,0], [10,0], [11,0]]) 
print("Dataset with total 8 points: \n",X, "\n Size: ", len(X)) 
y = nm.array([0,0,1,1,1,0,0,0])
print("\nClass label for the dataset X Y:",y)
labels = preprocessing.LabelEncoder()
stand_scalars=StandardScaler() 
x_training=stand_scalars.fit_transform(X)
y_training=labels.fit_transform(y)
x_testing=stand_scalars.transform(x_training)
y_testing=labels.transform(y_training)
x_training, x_testing, y_training, y_testing, train_test_split(X, y, test_size= 0.50, random_state=0, shuffle=False )
classifiers = KNeighborsClassifier(n_neighbors=3) 
classifiers.fit(x_training,y_training)
y_pred=classifiers.predict(x_testing)
print("\nPredicted Classs labels for testing data Y: ", y_pred)
confusion_matrix_result = confusion_matrix(y_testing, y_pred) 
print("\nTraining Data X: \n", x_training) 
print("\nTraining Data label Y:", y_training)
print("\nConfusion Matrix is\n",confusion_matrix_result)
total_value = sum(sum(confusion_matrix_result)) 
accuracy = (confusion_matrix_result[0,0]+confusion_matrix_result[1,1])/total_value
print('\nAccuracy is:', accuracy)
sensitivity = confusion_matrix_result[1,1]/(confusion_matrix_result[1,0]+confusion_matrix_result[1,1])
print('Sensitivity is:', sensitivity)
specificity = confusion_matrix_result[0,0]/(confusion_matrix_result[0,0]+confusion_matrix_result[0,1])
print('specificity is :', specificity)