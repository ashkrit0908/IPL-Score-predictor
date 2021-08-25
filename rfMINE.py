//importing library
import pandas as pd
//df is our data base
df = pd.read_csv('xx.csv')
//defining inputs and target 
inputs = df.drop('runs',axis = 'columns')
target = df['runs']
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
//model fitting
model = RandomForestClassifier()
model.fit(inputs,target)
//output of model based on various input turned into numerals
print(model.predict([[2,2,6,4,0,5]]))
