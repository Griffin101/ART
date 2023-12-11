import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score 

data = pd.read_csv('iris.csv')
df = pd.DataFrame(data)
X = df.drop('target', axis=1) 
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred) 
print(f"Accuracy: {accuracy:.2f}")

plt.figure(figsize=(12, 8))
plot_tree(clf, filled=True, feature_names=X.columns, class_names=data['target'].unique()) 
plt.title("Decision Tree Visualization (Iris Dataset)")
plt.show()
