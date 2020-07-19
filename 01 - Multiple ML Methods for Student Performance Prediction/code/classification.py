# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:33:05 2019

@author: Mohammed El-Agha
"""

# DT classification
class DecisionTreeClassifier:
    X_train = None 
    X_test = None 
    y_train = None
    y_test = None
    y_pred = None
    accuracy = 0
    classification_report = None
    confusion_matrix = None
    
    # constructor; take preprocessed dataset instance
    def __init__(self, df_variable):
        self.df_variable = df_variable
    
    # function to run classification
    def classify (self):
        X = self.df_variable.iloc[:,0:17] # attrbuites
        y = self.df_variable.iloc[:,18] # Class 
        
        # use splitter from sklearn, with 65% training, 35% test
        from sklearn.model_selection import train_test_split 
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size = 0.35, train_size = 0.65)
        
        # ---- Decision Tree -----------
        from sklearn import tree
        model = tree.DecisionTreeClassifier(criterion='entropy', max_depth=10) # max depth of tree is 10 levels
        
        # build the model on training data
        model.fit(self.X_train, self.y_train)
        
        # make predictions for test data
        self.y_pred = model.predict(self.X_test)
        
        self.accuracy() # call accuracy function
        self.classification_report()  # call classification_report function
        self.confusion_matrix()  # call confusion_matrix function
    
    # calculate accuracy of DT classifier
    def accuracy (self):
        from sklearn.metrics import accuracy_score # use accuracy_score from sklearn.metrics
        self.accuracy =  accuracy_score(self.y_test, self.y_pred) * 100 # equation of calculating accuracy
    
    # generate report of DT classifier
    def classification_report (self):
        from sklearn.metrics import classification_report # use classification_report from sklearn.metrics
        self.classification_report = classification_report(self.y_test, self.y_pred)
      
    # generate confusion matrix of DT classifier
    def confusion_matrix (self):
        from sklearn.metrics import confusion_matrix # use confusion_matrix from sklearn.metrics  
        self.confusion_matrix = confusion_matrix(self.y_test, self.y_pred)


# NN classification
class NearestNeighborClassifier:
    X_train = None 
    X_test = None 
    y_train = None
    y_test = None
    y_pred = None
    accuracy = 0
    classification_report = None
    confusion_matrix = None
    
    # constructor; take preprocessed dataset instance
    def __init__(self, df_variable):
        self.df_variable = df_variable
    
    # function to run classification
    def classify (self):
        X = self.df_variable.iloc[:,0:17] # attrbuites
        y = self.df_variable.iloc[:,18] # Class 
        
        # use splitter from sklearn, with 60% training, 40% test
        from sklearn.model_selection import train_test_split
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X,y,test_size=0.4,random_state=0)
        
        from sklearn.neighbors import KNeighborsClassifier  
        classifier = KNeighborsClassifier(n_neighbors=5)  
        
        model=classifier.fit(self.X_train, self.y_train) # build the model on training data
        clf=model.fit(self.X_train, self.y_train)
        
        # make predictions for test data
        self.y_pred = model.predict(self.X_test)
        
        self.accuracy() # call accuracy function
        self.classification_report()  # call classification_report function
        self.confusion_matrix()  # call confusion_matrix function
        
    
    # calculate accuracy of KNN classifier
    def accuracy (self):
        from sklearn.metrics import accuracy_score # use accuracy_score from sklearn.metrics
        self.accuracy =  accuracy_score(self.y_test, self.y_pred) * 100 # equation of calculating accuracy
    
    # generate report of KNN classifier
    def classification_report (self):
        from sklearn.metrics import classification_report # use classification_report from sklearn.metrics
        self.classification_report = classification_report(self.y_test, self.y_pred)
      
    # generate confusion matrix of KNN classifier
    def confusion_matrix (self):
        from sklearn.metrics import confusion_matrix # use confusion_matrix from sklearn.metrics  
        self.confusion_matrix = confusion_matrix(self.y_test, self.y_pred)
