# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 19:40:58 2019

@author: Mohammed El-Agha
"""

from PyAstronomy import pyasl

# Generalized ESD Outlier Analysis
class GeneralizedESDOutlierAnalysis:
    
    # constructor; take preprocessed dataset instance
    def __init__(self, df_variable):
        self.df_variable = df_variable
    
    # function to perform outlier analysis on input feature only; not on whole dataset
    def analyze (self, feature_name):
        # run outlier analysis, and get first 100 outlier data points
        r = pyasl.generalizedESD(self.df_variable[feature_name], 100, 0.1, fullOutput=True) 
        print ('Outlier Analysis for : ' + feature_name)
        print("Number of outliers: ", r[0])
        print("Indices of outliers: ", r[1])
        
        # outlier data points
        for i in range(len(r[1])):
            print("%8.5f  " % self.df_variable[feature_name][r[1][i]])
