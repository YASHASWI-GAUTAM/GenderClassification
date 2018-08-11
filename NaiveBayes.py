from sklearn.naive_bayes import GaussianNB

# To check the accuracy of your model
from sklearn.metrics import accuracy_score

# Now make an object for GaussianNB()
gnb = GaussianNB()

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']
     
# Training the model
gnb=gnb.fit(X,Y)

# Testing using the same data
pred_gnb = gnb.predict(X)
acc_gnb = accuracy_score(Y, pred_gnb) * 100
print('Accuracy for NaiveBayes: {}'.format(acc_gnb))

# Prediction
prediction = gnb.predict([[190, 70, 43]])

print("The person with height, weight, shoe_size as [190,70,43] is",prediction)
