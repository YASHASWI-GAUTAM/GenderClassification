from sklearn.ensemble import RandomForestClassifier

# To check the accuracy of your model
from sklearn.metrics import accuracy_score

# Now make an object for RandomForestClassifier(), here n_estimator is no. of trees in the model
clf = RandomForestClassifier(n_estimators=2)

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']
     
# Training the model
clf=clf.fit(X,Y)

# Testing using the same data
pred_clf = gnb.predict(X)
acc_clf = accuracy_score(Y, pred_clf) * 100
print('Accuracy for RandomForest: {}'.format(acc_clf))

# Prediction
prediction = clf.predict([[190, 70, 43]])

print("The person with height, weight, shoe_size as [190,70,43] is",prediction)
