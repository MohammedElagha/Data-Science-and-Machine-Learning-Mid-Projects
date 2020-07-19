# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 19:17:41 2019

@author: Mohammed El-Agha
"""

#from datasetreader import DatasetReader

class DataPreProcessor:
    
    # constructor, talk dataset (df) and pandas (pd)
    def __init__(self, df_variable, pd_variable):
        self.df_variable = df_variable
        self.pd_variable = pd_variable
    
    # config of dataset for only printing
    def config(self):
        self.pd_variable.set_option('display.max_columns', None) # No limit on number of columns in print
        self.pd_variable.set_option('display.width', 1000) 
        self.pd_variable.set_option('display.max_rows', 50) # 50 rows as max in print
        self.pd_variable.options.display.float_format = '{:,.0f}'.format # format of all floats in dataset to not show floating digits
    
    # drop irrelevant features to study goal
    def remove_irrelevant_features (self):
        self.df_variable = self.df_variable.drop('school', 1)
        self.df_variable = self.df_variable.drop('famsize', 1)
        self.df_variable = self.df_variable.drop('reason', 1)
        self.df_variable = self.df_variable.drop('traveltime', 1)
        self.df_variable = self.df_variable.drop('nursery', 1)
        self.df_variable = self.df_variable.drop('guardian', 1)
    
    # drop features which have similar values, because it not effect on process
    def remove_similar_values_features (self):
        self.df_variable = self.df_variable.drop('age', 1)
    
    # drop features which there are other features can be used instead of
    def remove_redundent_features (self):
        self.df_variable = self.df_variable.drop('Medu', 1)
        self.df_variable = self.df_variable.drop('Fedu', 1)
        self.df_variable = self.df_variable.drop('Pstatus', 1)
        self.df_variable = self.df_variable.drop('G1', 1)
        self.df_variable = self.df_variable.drop('G2', 1)
    
    # fill None values by 0, to prevent errors in run
    def fill_na_by_zero (self):
        self.df_variable['failures'] = self.df_variable['failures'].fillna(0)
        self.df_variable['studytime'] = self.df_variable['studytime'].fillna(0)
        self.df_variable['famrel'] = self.df_variable['famrel'].fillna(0)
        self.df_variable['freetime'] = self.df_variable['freetime'].fillna(0)
        self.df_variable['goout'] = self.df_variable['goout'].fillna(0)
        self.df_variable['health'] = self.df_variable['health'].fillna(0)
    
    # convert nominal string to nominal int
    def string_to_int_convert (self):
        # sex: 
        # 'M' -> 1 (Male)
        # 'F' -> 2 (Female)
        sex = {'M': 1, 'F': 2}
        self.df_variable["sex"] = [sex[item] for item in self.df_variable["sex"]]
        
        # address: 
        # 'R' -> 1 (rural)
        # 'U' -> 2 (urban)
        address = {'R': 1, 'U': 2}
        self.df_variable["address"] = [address[item] for item in self.df_variable["address"]]
        
        # mother job
        # 'at_home' => 5
        # 'teacher' => 4
        # 'services' => 3
        # 'health' => 2
        # 'other' => 1
        Mjob = {'at_home': 5, 'teacher': 4, 'services': 3, 'health': 2, 'other': 1}
        self.df_variable["Mjob"] = [Mjob[item] for item in self.df_variable["Mjob"]]
        
        # father job
        # 'at_home' => 5
        # 'teacher' => 4
        # 'services' => 3
        # 'health' => 2
        # 'other' => 1
        Fjob = {'at_home': 5    , 'teacher': 4, 'services': 3, 'health': 2, 'other': 1}
        self.df_variable["Fjob"] = [Fjob[item] for item in self.df_variable["Fjob"]]
        
        # schoolsup: school support
        # 'yes' -> 1
        # 'no' -> 0
        schoolsup = {'yes': 1, 'no': 0}
        self.df_variable["schoolsup"] = [schoolsup[item] for item in self.df_variable["schoolsup"]]
        
        # famsup: family support
        # 'yes' -> 1
        # 'no' -> 0
        famsup = {'yes': 1, 'no': 0}
        self.df_variable["famsup"] = [famsup[item] for item in self.df_variable["famsup"]]
        
        # paid: extra paid courses/learning
        # 'yes' -> 1
        # 'no' -> 0
        paid = {'yes': 1, 'no': 0}
        self.df_variable["paid"] = [paid[item] for item in self.df_variable["paid"]]
        
        # activities: learing activities
        # 'yes' -> 1
        # 'no' -> 0
        activities = {'yes': 1, 'no': 0}
        self.df_variable["activities"] = [activities[item] for item in self.df_variable["activities"]]
        
        # higher: student would to talk higher education?
        # 'yes' -> 1
        # 'no' -> 0
        higher = {'yes': 1, 'no': 0}
        self.df_variable["higher"] = [higher[item] for item in self.df_variable["higher"]]
        
        # internet: student has Internet
        # 'yes' -> 1
        # 'no' -> 0
        internet = {'yes': 1, 'no': 0}
        self.df_variable["internet"] = [internet[item] for item in self.df_variable["internet"]]
        
        # romantic: student in romantic relationship
        # 'yes' -> 1
        # 'no' -> 0
        romantic = {'yes': 1, 'no': 0}
        self.df_variable["romantic"] = [romantic[item] for item in self.df_variable["romantic"]]
       
    
    def discretize_features (self):
        # discretize "absences" feature to 4 bins
        # bin 1 [0-24], bin 2 [25-49], bin 3 [50-74], bin 4 [75-100]
        bins = [0, 25, 50, 75, 100]
        labels = [1, 2, 3, 4]
        self.df_variable['absences'] = self.pd_variable.cut(self.df_variable['absences'], bins, labels=labels)

    def discretize_target (self):
        # discretize "G3" feature to 3 bins
        # Fail [0-9], Pass [10-14], Good [15-20]
        bins = [0, 10, 15, 20]
        labels = ["Fail", "Pass", "Good"]
        self.df_variable['G3'] = self.pd_variable.cut(self.df_variable['G3'], bins, labels=labels)



# DataPreProcessorForTask class is use DataPreProcessor functions to make special preprocessing for each method as it need
class DataPreProcessorForTask:
        
    # constructor; take DataPreProcessor instance
    def __init__(self, data_preprocessor):
        self.data_preprocessor = data_preprocessor
    
    def preprocess_for_decision_tree_classification(self):
        self.data_preprocessor.config()
        self.data_preprocessor.remove_irrelevant_features()
        self.data_preprocessor.remove_similar_values_features()
        self.data_preprocessor.remove_redundent_features()
        self.data_preprocessor.fill_na_by_zero()
        self.data_preprocessor.string_to_int_convert()
        self.data_preprocessor.discretize_features()
        self.data_preprocessor.discretize_target()
        
    def preprocess_for_nearest_neighbor_classification(self):
        self.data_preprocessor.config()
        self.data_preprocessor.remove_irrelevant_features()
        self.data_preprocessor.remove_similar_values_features()
        self.data_preprocessor.remove_redundent_features()
        self.data_preprocessor.fill_na_by_zero()
        self.data_preprocessor.string_to_int_convert()
        self.data_preprocessor.discretize_features()
        self.data_preprocessor.discretize_target()
        
    def preprocess_for_linear_regression(self):
        self.data_preprocessor.config()
        self.data_preprocessor.remove_irrelevant_features()
        self.data_preprocessor.remove_similar_values_features()
        self.data_preprocessor.remove_redundent_features()
        self.data_preprocessor.fill_na_by_zero()
        self.data_preprocessor.string_to_int_convert()
        self.data_preprocessor.discretize_features()
        
    def preprocess_for_kmeans_clustering(self):
        self.data_preprocessor.config()
        self.data_preprocessor.remove_irrelevant_features()
        self.data_preprocessor.remove_similar_values_features()
        self.data_preprocessor.remove_redundent_features()
        self.data_preprocessor.fill_na_by_zero()
        self.data_preprocessor.string_to_int_convert()
        
    def preprocess_for_generalized_esd_outlier_analysis(self):
        self.data_preprocessor.config()
        self.data_preprocessor.remove_irrelevant_features()
        self.data_preprocessor.remove_similar_values_features()
        self.data_preprocessor.remove_redundent_features()
        self.data_preprocessor.fill_na_by_zero()
        self.data_preprocessor.string_to_int_convert()
        
        
        
        
        
        