import statistics
import numpy as np
import pandas as pd
import math
import copy
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, f1_score, recall_score


class DataAnalysis:
    def __init__(self):
        self.logistic_regression = LogisticRegression()

    def train_model_heart_disease(self):
        data = pd.read_csv("csvFiles/heart_disease_health_indicators_BRFSS2015.csv")
        data.drop_duplicates(inplace=True)
        y = data[['HeartDiseaseorAttack']]

        x = data.drop('HeartDiseaseorAttack', axis=1)
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
        x_test = x_test.values
        y_test = y_test.values
        x_train = x_train.values
        y_train = y_train.values
        model = StandardScaler()

        new_data = model.fit_transform(x_test)
        x_test = pd.DataFrame(new_data)

        new_data = model.fit_transform(x_train)
        x_train = pd.DataFrame(new_data)

        y_train = y_train.ravel()
        self.logistic_regression.fit(x_train, y_train)
        y_test = y_test.ravel()
        prediction = self.logistic_regression.predict(x_test)
        cm = confusion_matrix(y_test, prediction)
        print(cm)
        print('Accuracy Score', accuracy_score(y_test, prediction) * 100, '%')
        print('Precision Macro Score', precision_score(y_test, prediction, average='macro') * 100, '%')
        print('Recall_Score', recall_score(y_test, prediction, average='macro') * 100, '%')
        print('F_Score', f1_score(y_test, prediction, average='macro') * 100, '%')

    def calculate_median(self, data):
        sorted_values = sorted(data)
        return statistics.median(sorted_values)

    def calculate_average(self, data):
        return sum(data) / len(data)

    def standard_deviation(self, data):
        return statistics.stdev(data)

    def calculate_variance(self, data):
        return statistics.variance(data)

    def calculate_mode(self, data):
        return statistics.mode(data)

    def predict(self, row):
        self.train_model_heart_disease()
        to_return = self.logistic_regression.predict(row)
        return to_return
