from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

df = pd.read_csv('xx.csv')
 
inputs = df.drop('runs',axis = 'columns')
target = df['runs']


//model fitting
model = RandomForestClassifier()
model.fit(inputs,target)

//output of model based on various input turned into numerals
print(model.predict([[2,2,6,4,0,5]]))
