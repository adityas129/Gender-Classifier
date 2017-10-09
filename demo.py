from sklearn import tree
from sklearn import neighbors
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm

#[height, weight, shoe size]

X = [[181,80,44], [177,70,43],[160,60,38], [166,65,40], [190,90,47],[175,64,39],[177,70,40], [159,55,37], [171,75,42], [181,85,43], [170,76,42]]

Y = ['male', 'female', 'female', 'female', 'male', 'male', 'male', 'female', 'male', 'female', 'male']

clf = tree.DecisionTreeClassifier()
clf1 = neighbors.KNeighborsClassifier()
clf2 = svm.SVC()
clf3 = MultinomialNB()

clf = clf.fit(X,Y)
clf1 = clf1.fit(X,Y)
clf2 = clf1.fit(X,Y)
clf3 = clf1.fit(X,Y)

prediction= clf.predict([[190,70, 43]])
prediction1= clf1.predict([[190,70, 43]])
prediction2= clf2.predict([[190,70, 43]])
prediction3= clf3.predict([[190,70, 43]])

print prediction
print prediction1
print prediction2
print prediction3
