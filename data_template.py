#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 16:37:27 2018

@author: aaronfernandez
"""
#@author: aaronfernandez

#Data Preprocessing
#Importing libraries 
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
#import dataset 
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values

y = dataset.iloc[:, 3].values

#splitting dataset into Training and Test set
from sklearn.model_selection import train_test_split
X_train, X_test ,y_train ,y_test = train_test_split (X,y,test_size = 0.2, random_state = 0)

#Feature Scaling
"""
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
"""

