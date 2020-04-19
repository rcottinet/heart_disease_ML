from sklearn.externals import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np
import pandas as pd
import pickle
import warnings
warnings.filterwarnings('ignore')

df_heartdisease = pd.read_csv("framingham.csv")

# Delete Null values
df_heartdisease.dropna(axis=0, inplace=True)


# Drop the column to predict
df_train = df_heartdisease.drop(['TenYearCHD'], axis=1)


predictors = ["male", "age", "cigsPerDay", 'BPMeds', 'prevalentHyp',
              'diabetes', 'totChol', "sysBP", "diaBP", "glucose"]

df_train2 = df_train[predictors]


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    df_train2, df_heartdisease['TenYearCHD'], test_size=0.2, random_state=5)

# Train model
clf_rf = RandomForestClassifier(random_state=1, n_estimators=40,
                                min_samples_leaf=3, min_samples_split=2)  # by default, 10 trees are used
clf_rf.fit(X_train, y_train)

train_score = clf_rf.score(X_train, y_train)
test_score = clf_rf.score(X_test, y_test)

scores_rf = cross_val_score(clf_rf, df_heartdisease.drop(
    ['TenYearCHD'], axis=1), df_heartdisease['TenYearCHD'], scoring='accuracy', cv=5)
# your code here
print('train accuracy =', train_score)

# Cross validation

print('cross validation accuracy =',  scores_rf.mean())


pickle.dump(clf_rf, open('model.pkl', 'wb'))


model = pickle.load(open('model.pkl', 'rb'))

predictors = ["male", "age", "cigsPerDay", 'BPMeds', 'prevalentHyp',
              'diabetes', 'totChol', "sysBP", "diaBP", "glucose"]
patient_value2 = [1, 50,    1.0,    0.0,    1,
                  0,    313.0,    179.0,    92.0,    86.0]
patient_value2 = [1, 39, 0.0, 0.0, 0.0, 0, 195.0, 106.0, 70.0, 77.0]
df_predict = pd.DataFrame(
    np.array(patient_value2).reshape(1, -1), columns=predictors)


predict_score = clf_rf.predict(df_predict)
prob_score = clf_rf.predict_proba(df_predict)

print('predict score: ', predict_score)
print('proba score: ', prob_score)
