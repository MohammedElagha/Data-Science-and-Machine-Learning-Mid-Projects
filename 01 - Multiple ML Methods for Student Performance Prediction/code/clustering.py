# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 18:06:40 2019

@author: Mohammed El-Agha
"""

from sklearn.cluster import KMeans
import numpy as np
from sklearn import metrics

# KmeansClustering
class KmeansClustering:
    X = None
    Y = None
    K = 3
    kmeans_model = None
    labels = None
    cluster_centers = None
    purity_of_labels = ''
    
    # constructor; take preprocessed dataset instance
    def __init__(self, df_variable):
        self.df_variable = df_variable
        
    def purity_score(y_true, y_pred,label):
        # compute contingency matrix (also called confusion matrix)
        contingency_matrix = metrics.cluster.contingency_matrix(y_true, y_pred)
        # return purity
        return np.sum(np.amax(contingency_matrix[label], axis=0)) / np.sum(contingency_matrix[label]) 
    
    # function to run clustering
    def cluster (self):
        self.X = self.df_variable.iloc[:,0:18] # attrbuites
        self.Y = self.df_variable.iloc[:,18] # Class 
        
        # fit clustering model
        self.kmeans_model = KMeans(n_clusters=self.K).fit(self.X)
        
        self.labels() # call labels function
        self.cluster_centers() # call cluster_centers function
        #self.purity_of_labels()
    
    # get labels using kmeans_model instance
    def labels (self):
        self.labels =  self.kmeans_model.labels_
    
    # get centriods using kmeans_model instance
    def cluster_centers (self):
        self.cluster_centers =  self.kmeans_model.cluster_centers_
        
    #def purity_of_labels (self):
    #    for i in range(self.K):    
    #        purity=self.purity_score(self.Y, self.kmeans_model.labels_ , i)
    #        self.purity_of_labels = self.purity_of_labels + "purity of label " + str(i) +"  is "+ str(purity)
