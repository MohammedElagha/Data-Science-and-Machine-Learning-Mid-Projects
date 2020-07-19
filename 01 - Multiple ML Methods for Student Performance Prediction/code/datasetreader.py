# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 19:08:30 2019

@author: Mohammed El-Agha
"""

import pandas as pd

# DatasetReader: read dataset file, and create pandas instance for it
class DatasetReader:
    
    pd_variable = None
    df_variable = None
    
    def __init__(self, file_path):
        self.file_path = file_path
    
    def read_dataset(self):
        df = pd.read_excel(self.file_path) # read dataset file
        self.pd_variable = pd # define variable for pandas
        self.df_variable = df # define variable for dataset
