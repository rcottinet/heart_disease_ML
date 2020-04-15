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
df_heartdisease.drop(['TenYearCHD'], axis=1)

# Split data
X_train, X_test, y_train, y_test = train_test_split(df_heartdisease.drop(
    ['TenYearCHD'], axis=1), df_heartdisease['TenYearCHD'], test_size=0.3, random_state=1)

# Train model
clf_rf = RandomForestClassifier(random_state=1, n_estimators=40,
                                min_samples_leaf=2, min_samples_split=2)  # by default, 10 trees are used
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

predictors = ["male", "Age", "Education", 'CurrentSmoker', 'cigsPerDay', "BPMeds", "prevalentStroke",
              "prevalentHyp",	"diabetes",	"totChol",	"sysBP",	"diaBP",	"BMI",	"heartRate",	"glucose"]

patient_value = [1, 65, 2, 1, 10, 100, 0.0,
                 0, 1, 150, 196.0, 75.0, 25.0, 65.0, 66.0]
patient_value2 = [1, 39, 4.0,	0, 0.0, 0.0, 0,	0,
                  0, 195.0, 106.0,	70.0,	26.97, 80.0, 77.0]

df = pd.DataFrame(np.array(patient_value).reshape(1, -1), columns=predictors)

predict_score = clf_rf.predict(df)
prob_score = clf_rf.predict_proba(df)

print('predict score: ', predict_score)
print('proba score: ', prob_score)
