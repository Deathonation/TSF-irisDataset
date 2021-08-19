# -*- coding: utf-8 -*-
"""IrisTask.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rAjzkd7fD-sOftGJ8CrFfJ1rbrZ2zgfk
"""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

"""### **LOADING DATASET**

"""

df = pd.read_csv("Iris.csv")
df.head()

df1 = df.drop(columns=["Id"])
df1.head()

df1.describe()

df1.info()
#no null values

# to display no. of samples on each class
df1['Species'].value_counts()

# check for null values
df1.isnull().sum()

"""### **PREPROCESSING**"""

df1.isnull().sum()
# no null values present

"""### **EXPLORATORY DATA ANALYSIS**"""

df1['SepalLengthCm'].hist()

df1['PetalLengthCm'].hist()

df1['SepalWidthCm'].hist()

df1['PetalWidthCm'].hist()

# scatterplot
colors = ['red', 'orange', 'blue']
species = ['Iris-setosa', 'Iris-virginica', 'Iris-versicolor']

for i in range(3):
  x=df1[df1['Species']==species[i]]
  plt.scatter(x['SepalLengthCm'], x['SepalWidthCm'], c =colors[i], label= species[i])
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend()

for i in range(3):
  x=df1[df1['Species']==species[i]]
  plt.scatter(x['PetalLengthCm'], x['PetalWidthCm'], c =colors[i], label= species[i])
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.legend()

"""### **In the above plot we can see that all three samples are more classified and has a linear relation and can be identified seperately.**"""

for i in range(3):
  x=df1[df1['Species']==species[i]]
  plt.scatter(x['SepalLengthCm'], x['PetalLengthCm'], c =colors[i], label= species[i])
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.legend()

for i in range(3):
  x=df1[df1['Species']==species[i]]
  plt.scatter(x['SepalWidthCm'], x['PetalWidthCm'], c =colors[i], label= species[i])
plt.xlabel('Sepal Width')
plt.ylabel('Petal Width')
plt.legend()

"""### **CORRELATION MATRIX**"""

df1.corr()

corr = df1.corr()
fig, ax = plt.subplots(figsize=(5,5))
sns.heatmap(corr, annot = True, ax=ax, cmap = 'Wistia')

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

df1['Encoded Species'] = le.fit_transform(df['Species'])
df1.head()

sns.pairplot(df1)

sns.catplot(x= 'PetalLengthCm', y= 'PetalWidthCm', palette='husl', hue='Encoded Species', data= df1)

"""### **MODELLING**

"""

from sklearn.model_selection import train_test_split
#train-70%
#test-30%
train, test = train_test_split(df1, test_size=0.2)

train.shape, test.shape

df1.columns

train_x = train[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
test_x = test[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
train_y = train['Encoded Species']
test_y = test['Encoded Species']

from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

dtree = DecisionTreeClassifier()
dtree.fit(train_x, train_y);

predictions = dtree.predict(test_x)
print("The accuracy of decision tree is: ", metrics.accuracy_score(predictions, test_y))

"""### **The accuracy is 96%. So we can create model for entire data**"""

X = df1[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
Y = df1['Encoded Species']

dtree1 = DecisionTreeClassifier()
dtree1.fit(X,Y)
print("Decision Tree Classifier is ready")

"""### **VISUALIZING THE DECISION TREE**"""

from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus
import sklearn.datasets as datasets

iris_set = datasets.load_iris()
dot_data = StringIO()
export_graphviz(dtree1, out_file= dot_data, feature_names= iris_set.feature_names,
                filled = True, rounded = True,
                special_characters = True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
Image(graph.create_png())

"""### **It is observed that the leaf nodes are homogeneous**"""