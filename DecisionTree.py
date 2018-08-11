# Importing the library that includes DecisionTreeClassifier
from sklearn import tree

# To check the accuracy of your model
from sklearn.metrics import accuracy_score

# Now make an object for DecisionTreeClassifier()
clf=tree.DecisionTreeClassifier()

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']
     
# Training the model
clf=clf.fit(X,Y)

# Testing using the same data
pred_tree = clf.predict(X)
acc_tree = accuracy_score(Y, pred_tree) * 100
print('Accuracy for DecisionTree: {}'.format(acc_tree))

# Prediction
prediction = clf.predict([[190, 70, 43]])

print("The person with height, weight, shoe_size as [190,70,43] is",prediction)
