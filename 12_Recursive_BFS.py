import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB, CategoricalNB, GaussianNB
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,recall_score,f1_score,classification_report
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt 
df=pd.read_csv("dieseases.csv")
print(df)
print(df.info())
Le=LabelEncoder()
df['sore throat']=Le.fit_transform(df['sore throat'])

df['fever']=Le.fit_transform(df['fever'])
df['swallon']=Le.fit_transform(df['swallon'])
df['Congestion ']=Le.fit_transform(df['Congestion '])
df['headache']=Le.fit_transform(df['headache'])
df['diagnosis']=Le.fit_transform(df['diagnosis'])
print(df)

fig,ax=plt.subplots(figsize=(6,6))
sns.countplot(x=df['sore throat'], data=df)
plt.title("Sore throat")
plt.xlabel("sore throat")
plt.ylabel("count")
plt.show()


x=df.drop(['diagnosis'],axis=1)
y=df['diagnosis']

classifier = MultinomialNB()
print(classifier.fit(x,y))
classifier=CategoricalNB()
print(classifier.fit(x,y))
classifier=GaussianNB()
print(classifier.fit(x,y))

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
classifier=MultinomialNB()
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)
print("confusion matrix:",confusion_matrix(y_test,y_pred))
print("accuracy_score:",accuracy_score(y_test,y_pred))
print("precision score:",precision_score(y_test,y_pred))
print("recall_score:",recall_score(y_test,y_pred))
print(classification_report(y_test,y_pred))
