from sklearn.linear_model import LogisticRegression

# To check the accuracy of your model
from sklearn.metrics import accuracy_score

# Now make an object for LogisticRegression()
lreg=LogisticRegression()

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']
     
# Training the model
lreg=lreg.fit(X,Y)

# Testing using the same data
pred_lreg = clf.predict(X)
acc_lreg = accuracy_score(Y, pred_lreg) * 100
print('Accuracy for Logistic Regression: {}'.format(acc_lreg))

# Prediction
prediction = lreg.predict([[190, 70, 43]])

print("The person with height, weight, shoe_size as [190,70,43] is",prediction)
