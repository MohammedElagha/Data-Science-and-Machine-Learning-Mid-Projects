# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 17:38:58 2019

@author: Mohammed El-Agha
"""
import matplotlib.pyplot as plt

# Linear Regression
class LinearRegression:
    X_train = None 
    X_test = None 
    y_train = None
    y_test = None
    y_pred = None
    regr = None
    coefficients = 0
    intercept = 0
    liner_equation = ''
    mean_squared_error = 0
    
    # constructor; take preprocessed dataset instance
    def __init__(self, df_variable):
        self.df_variable = df_variable
        
    # function to run regression
    def regression (self):
        X = self.df_variable.iloc[:,0:17] # attrbuites
        y = self.df_variable.iloc[:,18] # Class 
        
        # use splitter from sklearn, with 65% training, 35% test
        from sklearn.model_selection import train_test_split
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size = 0.35, train_size = 0.65)
        
        # ---- Linear Regression -----------
        from sklearn import  linear_model
        self.regr = linear_model.LinearRegression() # define regression instance using LinearRegression from sklearn
        self.regr.fit(self.X_train, self.y_train) # fit regression model
        
        # Make predictions using the testing set
        self.y_pred = self.regr.predict(self.X_test)
        
        self.coefficients()  # call coefficients function
        self.intercept()  # call intercept function
        self.liner_equation()  # call liner_equation function
        self.mean_squared_error()  # call mean_squared_error function
        self.plot_regr()
        
    # get coefficients from regression instance
    def coefficients (self):
        self.coefficients =  self.regr.coef_
    
    # get intercept from regression instance
    def intercept (self):
        self.intercept =  self.regr.intercept_
       
    # use regression instance to create Linear Equation of regression
    def liner_equation (self):
        self.liner_equation =  self.regr.coef_ ,"X + ", self.regr.intercept_
       
    # calculate MSE using sklearn.metrics
    def mean_squared_error (self):
        from sklearn.metrics import mean_squared_error
        self.mean_squared_error =  mean_squared_error(self.y_test, self.y_pred)
        
    def plot_regr (self):
        XTest = self.X_test.mean(axis=1)
        print(XTest)
        plt.scatter(XTest, self.y_test,  color='black')
        plt.plot(XTest, self.y_pred, color='blue', linewidth=3)
        plt.xticks(())
        plt.yticks(())
        plt.show()
        
