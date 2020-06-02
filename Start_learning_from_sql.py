# Load libraries
from pandas import read_csv
from pandas.plotting import scatter_matrix
from pandas import DataFrame
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import mysql.connector as mysql
import pandas as pd

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "ektimo"
)

#Load dataset
dataset = pd.read_sql('select * from podatki where Claim_Amount > 0', con=db)

# shape
print(dataset.shape)

# head
print(dataset.head(20))

# descriptions
print(dataset.describe())

# class distribution
print(dataset.groupby('Claim_Amount').size())