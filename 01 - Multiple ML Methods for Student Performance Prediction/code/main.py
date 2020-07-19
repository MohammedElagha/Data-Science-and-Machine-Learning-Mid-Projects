# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 21:25:34 2019

@author: Mohammed El-Agha
"""

from datasetreader import DatasetReader
from preprocess import DataPreProcessor
from preprocess import DataPreProcessorForTask
from classification import DecisionTreeClassifier
from classification import NearestNeighborClassifier
from regression import LinearRegression
from clustering import KmeansClustering
from outlier_analysis import GeneralizedESDOutlierAnalysis
import matplotlib.pyplot as plt
from tkinter import messagebox

class Main:
    
    # Define "pandas" and "dataset variable" for the class to be used in functions
    pd_variable = None
    df_variable = None
    
    # Constructor; do readiing dataset
    def __init__(self):
        self.read_dataset()
    
    
    def read_dataset (self):
        file_path = '../dataset/student-por.xlsx'
        dataset_reader = DatasetReader(file_path) # read dataset using datasetreader.DatasetReader class
        dataset_reader.read_dataset()
        self.pd_variable = dataset_reader.pd_variable # assing "pandas" from DatasetReader to local
        self.df_variable = dataset_reader.df_variable # assing "dataset" from DatasetReader to local
    
    def dataset_2d_visualization (self):
        self.df_variable.plot() # make 2D visualization of dataset
    
    def decision_tree_classification (self):
        data_preprocessor = DataPreProcessor(self.df_variable, self.pd_variable) # define preprocess.DataPreProcessor instance
        data_preprocessor_for_task = DataPreProcessorForTask(data_preprocessor) # perform preprocessing using preprocess.DataPreProcessorForTask using preprocess.DataPreProcessor instance
        data_preprocessor_for_task.preprocess_for_decision_tree_classification() # perform preprocessing for DT classification
        classification_pd_variable = data_preprocessor.pd_variable
        classification_df_variable = data_preprocessor.df_variable
        
        decision_tree_classification = DecisionTreeClassifier(classification_df_variable) # define instance of classification.DecisionTreeClassifier on preproccessed DF
        decision_tree_classification.classify() # run classification
        accuracy = decision_tree_classification.accuracy # classifier retrieve its accuracy result 
        classification_report = decision_tree_classification.classification_report # classifier retrieve its report 
        confusion_matrix = decision_tree_classification.confusion_matrix # classifier retrieve its confusion matrix 
        
        messagebox.showinfo("accuracy", accuracy) # show accuracy of classifier on message box
        messagebox.showinfo("classification_report", classification_report) # show accuracy of classifier on classification report

        print (accuracy)
        print (classification_report)
        print (confusion_matrix)
        
    def nearest_neighbor_classification (self):
        data_preprocessor = DataPreProcessor(self.df_variable, self.pd_variable) # define preprocess.DataPreProcessor instance
        data_preprocessor_for_task = DataPreProcessorForTask(data_preprocessor) # perform preprocessing using preprocess.DataPreProcessorForTask using preprocess.DataPreProcessor instance
        data_preprocessor_for_task.preprocess_for_nearest_neighbor_classification() # perform preprocessing for NN classification
        classification_pd_variable = data_preprocessor.pd_variable
        classification_df_variable = data_preprocessor.df_variable
        
        nearest_neighbor_classification = NearestNeighborClassifier(classification_df_variable) # define instance of classification.NearestNeighborClassifier on preproccessed DF
        nearest_neighbor_classification.classify() # run classification
        accuracy = nearest_neighbor_classification.accuracy # classifier retrieve its accuracy result 
        classification_report = nearest_neighbor_classification.classification_report # classifier retrieve its report 
        confusion_matrix = nearest_neighbor_classification.confusion_matrix # classifier retrieve its confusion matrix
        
        messagebox.showinfo("accuracy", accuracy) # show accuracy of classifier on message box
        messagebox.showinfo("classification_report", classification_report) # show accuracy of classifier on classification report
        
        print (accuracy)
        print (classification_report)
        print (confusion_matrix)
        
    def linear_regression (self):
        data_preprocessor = DataPreProcessor(self.df_variable, self.pd_variable) # define preprocess.DataPreProcessor instance
        data_preprocessor_for_task = DataPreProcessorForTask(data_preprocessor) # perform preprocessing using preprocess.DataPreProcessorForTask using preprocess.DataPreProcessor instance
        data_preprocessor_for_task.preprocess_for_linear_regression() # perform preprocessing for Linear Regression
        regression_pd_variable = data_preprocessor.pd_variable
        regression_df_variable = data_preprocessor.df_variable
        
        linear_regression = LinearRegression(regression_df_variable) # define instance of regression.LinearRegression on preproccessed DF
        linear_regression.regression() # run regression
        coefficients = linear_regression.coefficients # regression retrieve its coefficients result 
        intercept = linear_regression.intercept # regression retrieve its intercept result 
        liner_equation = linear_regression.liner_equation # regression retrieve its linear equation result 
        mean_squared_error = linear_regression.mean_squared_error # regression retrieve its MSE result 
        
        messagebox.showinfo("liner_equation", liner_equation) # show linear equation on message box
        messagebox.showinfo("mean_squared_error", mean_squared_error) # show regression MSE on message box
        
        print (coefficients)
        print (intercept)
        print (liner_equation)
        print (mean_squared_error)
        #linear_regression.plot_regr
        
    def kmeans_clustering (self):
        data_preprocessor = DataPreProcessor(self.df_variable, self.pd_variable) # define preprocess.DataPreProcessor instance
        data_preprocessor_for_task = DataPreProcessorForTask(data_preprocessor) # perform preprocessing using preprocess.DataPreProcessorForTask using preprocess.DataPreProcessor instance
        data_preprocessor_for_task.preprocess_for_kmeans_clustering() # perform preprocessing for Kmeans Clustering
        clustering_pd_variable = data_preprocessor.pd_variable
        cluserting_df_variable = data_preprocessor.df_variable
        
        kmeans_clustering = KmeansClustering(cluserting_df_variable) # define instance of clustering.KmeansClustering on preproccessed DF
        kmeans_clustering.cluster() # run clustering
        labels = kmeans_clustering.labels # clustering retrieve its labels 
        cluster_centers = kmeans_clustering.cluster_centers # clustering retrieve its centroids 
        #purity_of_labels = kmeans_clustering.purity_of_labels
        
        print (labels)
        print (cluster_centers)
        #print (purity_of_labels)
        
    def outlier_analysis (self):
        data_preprocessor = DataPreProcessor(self.df_variable, self.pd_variable) # define preprocess.DataPreProcessor instance
        data_preprocessor_for_task = DataPreProcessorForTask(data_preprocessor) # perform preprocessing using preprocess.DataPreProcessorForTask using preprocess.DataPreProcessor instance
        data_preprocessor_for_task.preprocess_for_generalized_esd_outlier_analysis() # perform preprocessing for ESD outlier analysis
        outlier_analysis_pd_variable = data_preprocessor.pd_variable
        outlier_analysis_df_variable = data_preprocessor.df_variable
        
        generalized_esd_outlier_analysis = GeneralizedESDOutlierAnalysis(outlier_analysis_df_variable) # define instance of outlier_analysis.GeneralizedESDOutlierAnalysis on preproccessed DF
        generalized_esd_outlier_analysis.analyze('failures') # print outliers data points for "failures" attribute
        generalized_esd_outlier_analysis.analyze('absences') # print outliers data points for "absences" attribute
        generalized_esd_outlier_analysis.analyze('G3') # print outliers data points for "G3" attribute




#dataset_2d_visualization(df_variable)
#decision_tree_classification(df_variable, pd_variable)
#nearest_neighbor_classification(df_variable, pd_variable)
#linear_regression(df_variable, pd_variable)
#kmeans_clustering(df_variable, pd_variable)
#outlier_analysis(df_variable, pd_variable)