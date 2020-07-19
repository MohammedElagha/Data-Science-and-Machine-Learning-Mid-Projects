# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 21:06:08 2019

@author: Mohammed El-Agha
"""

# this is luncher class; run the app in this file

from main import Main
import tkinter as tk
from tkinter import Button
    
r = tk.Tk() # define tkinter instance
r.geometry('400x170') # size of tkinter window
    
main = Main() # make instance of Main class
main.read_dataset() # read dataset using Main instance

# declare command of 2D visualization of dataset, to be used as parameter for button
def dataset_2d_visualization_command ():
    print ("---------------- 2D Visualization of Dataset ----------------")
    main.dataset_2d_visualization()
    print ("-------------------------------------------------------------")

# declare command of DT Classification, to be used as parameter for button    
def decision_tree_classification_command ():
    print ("---------------- Decision Tree Classification ---------------")
    main.decision_tree_classification()
    print ("-------------------------------------------------------------")

# declare command of NN Classification, to be used as parameter for button    
def nearest_neighbor_classification_command ():
    print ("--------------- Nearest Neighbor Classification -------------")
    main.nearest_neighbor_classification()
    print ("-------------------------------------------------------------")
            
# declare command of Linear Regression, to be used as parameter for button
def linear_regression_command ():
    print ("--------------------- Linear Regression ---------------------")
    main.linear_regression()
    print ("-------------------------------------------------------------")
    
# declare command of Kmeans Clustering, to be used as parameter for button
def kmeans_clustering_command ():
    print ("--------------------- K-Means Clustering --------------------")
    main.kmeans_clustering()
    print ("-------------------------------------------------------------")
   
# declare command of ESD Outlier Analysis, to be used as parameter for button
def outlier_analysis_command ():
    print ("-------------- Generalized ESD Outlier Analysis -------------")
    main.outlier_analysis()
    print ("-------------------------------------------------------------")
    


_2d_btn = Button(r, text='2D Visualization', width=25, command=dataset_2d_visualization_command) 
decision_tree_btn = Button(r, text='Decision Tree Classification', width=25, command=decision_tree_classification_command) 
nearest_neighbor_btn = Button(r, text='Nearest Neighbor Classification', width=25, command=nearest_neighbor_classification_command) 
linear_regression_btn = Button(r, text='Linear Regression', width=25, command=linear_regression_command) 
kmeans_clustering_btn = Button(r, text='K-Means Clustering', width=25, command=kmeans_clustering_command) 
outlier_analysis_btn = Button(r, text='Outlier Analysis', width=25, command=outlier_analysis_command)

_2d_btn.pack(expand=tk.FALSE, fill=tk.X, side=tk.TOP) 
decision_tree_btn.pack(expand=tk.FALSE, fill=tk.X, side=tk.TOP) 
nearest_neighbor_btn.pack(expand=tk.FALSE, fill=tk.X, side=tk.TOP) 
linear_regression_btn.pack(expand=tk.FALSE, fill=tk.X, side=tk.TOP) 
kmeans_clustering_btn.pack(expand=tk.FALSE, fill=tk.X, side=tk.TOP) 
outlier_analysis_btn.pack(expand=tk.FALSE, fill=tk.X, side=tk.TOP) 

r.mainloop() 