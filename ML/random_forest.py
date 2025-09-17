#8.随机森林 (Random Forest)
#random forest
#import library
from sklearn.ensemble import  RandomForestClassifier
#assumed you have x(predictor)and y(target) for training data set and x_test(predictor)of test_dataset
#create random forest object
model=RandomForestClassifier()
#train the model using the training sets and chek score
model.fit(x,y)
#predict output
predict=model.presort(x_test)