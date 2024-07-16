# -*- coding: utf-8 -*-
"""Project_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rDFNv2suQoNFf60AodgZG0wAF_GiwaBE
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('global_co2.csv')
df.head()

# CHECKING NULL VALUES
# AS YOU CAN SEE BELOW WE HAVE 199 NULL VALUES IN PER CAPITA COLUMN
df.isnull().sum()

df.info()

df.fillna(df.mean(), inplace = True)
df

df.info()

df.isnull().sum()

duplicate_records = df.duplicated().sum()
print("Duplicate Records:\n", duplicate_records)

df1 = df.round(2)
df1

#SPLITTING DATA
X = df1['Year'].values.reshape(-1,1)
y = df1['Per Capita'].values

X

y

#SPLITTING DATA SKLEARN
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#Linear Regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# VISUALIZATION
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Per Capita vs Year (Training set)')
plt.xlabel('Year')
plt.ylabel('Per Capita')
plt.show()

plt.scatter(X_test, y_test, color='orange')
plt.plot(X_train, regressor.predict(X_train), color = 'green')
plt.title('Per Capita vs Year (Training set)')
plt.xlabel('Year')
plt.ylabel('Per Capita')
plt.show()

#predict
print(regressor.predict([[2011]]))

print(regressor.predict([[2012]]))

print(regressor.predict([[2013]]))

"""**POLYNOMIAL REGRESSION**"""

#polynomial
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X)
poly_reg.fit(X_poly, y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

X_poly

#VISUALIZATION POLYNOMIAL REGRESSION
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.title('Per Capita vs Year (Polynomial Regression)')
plt.xlabel('Year')
plt.ylabel('Per Capita')
plt.show

#Predict
print(lin_reg_2.predict(poly_reg.fit_transform([[2011]])))

print(lin_reg_2.predict(poly_reg.fit_transform([[2012]])))

print(lin_reg_2.predict(poly_reg.fit_transform([[2013]])))

"""**RANDOM_FOREST**"""

# RANDOM FOREST
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
regressor.fit(X, y)

X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color="blue")
plt.title('Per Capita Vs Year')
plt.xlabel('Year')
plt.ylabel('Per_Capita')
plt.show()

#Predict
print(regressor.predict([[2011]]))

print(regressor.predict([[2012]]))

print(regressor.predict([[2013]]))

"""**DECISION TREE**"""

# DECISION TREE
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X, y)

# VISUALIZATION
X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color="blue")
plt.title('Percapita vs Year')
plt.xlabel('Year')
plt.ylabel('Per capita')
plt.show()

#Predict
print(regressor.predict([[2011]]))

print(regressor.predict([[2012]]))

print(regressor.predict([[2013]]))

# I HAVE PUT ALL REGRESSION MODELS IN DATASET ,
# DECISION TREE GIVES ME BEST RESULT
# IT PREDICT RESULT WITH 98...% ACCURACY