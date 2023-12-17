import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
import matplotlib.pyplot as plt

df=pd.read_csv("ai/all_practical/ART/PlayTennis.csv")
print(df)

Le=LabelEncoder()
df['Outlook']=Le.fit_transform(df['Outlook'])
df['Temperature']=Le.fit_transform(df['Temperature'])
df['Humidity']=Le.fit_transform(df['Humidity'])
df['Wind']=Le.fit_transform(df['Wind'])
df['Play Tennis']=Le.fit_transform(df['Play Tennis'])
print(df)

y=df['Play Tennis']
x=df.drop(['Play Tennis'],axis=1)

clf=tree.DecisionTreeClassifier(criterion='entropy')
clf=clf.fit(x,y)

print(clf)
print(tree.plot_tree(clf))

plt.show()
