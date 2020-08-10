import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets
import pandas as pd
import cv2
import glob
dictionary=dict()
dictionary[1]=u'\u0b85'
dictionary[2]=u'\u0bc7'
dictionary[3]=u'\u0bae'+u'\u0bcd'
dictionary[4]=u'\u0ba9'+u'\u0bcd'
dictionary[5]=u'\u0baa'
dictionary[6]=u'\u0b9a'+u'\u0bbf'
dictionary[7]=u'\u0bb5'
"""dictionary[1]=u'\u0ba9'+u'\u0bcd'
dictionary[2]=u'\u0bc7'
dictionary[3]=u'\u0baa'
dictionary[4]=u'\u0b9a'+u'\u0bbf'
dictionary[5]=u'\u0bb5'
dictionary[6]=u'\u0bae'+u'\u0bcd'
dictionary[7]=u'\u0ba8'
dictionary[10]=u'\u0bbe'
dictionary[11]=u'\u0b9f'
dictionary[12]=u'\u0b87'
dictionary[13]=u'\u0ba8'+u'\u0bcd'
dictionary[14]=u'\u0ba4'+u'\u0bbf'
dictionary[15]=u'\u0baf'
dictionary[19]=u'\u0baf'+u'\u0bcd'
dictionary[20]=u'\u0bc8'
dictionary[21]=u'\u0bae'
dictionary[24]=u'\u0bc6'
dictionary[26]=u'\u0bb2'+u'\u0bcd'
dictionary[27]=u'\u0bb2'+u'\u0bf6'
"""
iris =pd.read_csv("CSV/merge.csv")
X = iris.drop('ANS',axis=1)
ml=glob.glob("Test/TEST_CSV/*.csv")
cou=len(ml)
for mmm in range(cou):
	iris_1=pd.read_csv("Test/TEST_CSV/file"+str(mmm)+".csv")
	# we only take the first two features. We could
	# avoid this ugly slicing by using a two-dim dataset
	y = iris['ANS']
	#print(l,)
	#print(X)
	#print(y)
	from sklearn.model_selection import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)

	from sklearn.svm import SVC 
	svclassifier = SVC(kernel='linear')
	svclassifier.fit(X_train, y_train)

	 #print(iris_1.iloc[0])

	y_pred = svclassifier.predict([iris_1.iloc[0]])

	#print(y_pred)
	if list(y_pred)==[1]:
		print(dictionary[1])
	if list(y_pred)==[2]:
		print(dictionary[2])
	if list(y_pred)==[3]:
		print(dictionary[3])
	if list(y_pred)==[4]:
		print(dictionary[4])
	if list(y_pred)==[5]:
		print(dictionary[5])
	if list(y_pred)==[6]:
		print(dictionary[6])
	if list(y_pred)==[7]:
		print(dictionary[7])
	




