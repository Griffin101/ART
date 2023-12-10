from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = [
    ["Red", 8, "Apple"],
    ["Orange", 6, "Orange"],
    ["Red", 7, "Apple"],
    ["Orange", 8, "Orange"],
    ["Red", 7, "Apple"],
    ["Orange", 6, "Orange"],
]

color_mapping = {"Red": 0, "Orange": 1}
data_numeric = [[color_mapping[color], diameter, label] for color, diameter, label in data]

X = [[row[0], row[1]] for row in data_numeric]
y = [row[2] for row in data_numeric]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier()

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

new_data_point = [[color_mapping["Orange"], 7]]  # Orange color, diameter 7
prediction = clf.predict(new_data_point)
print(f"Prediction: {prediction[0]}")