# visualize the data
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
import mysql.connector as mysql
import pandas as pd

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "ektimo"
)

# Load dataset
dataset = pd.read_sql('select * from podatki where Claim_Amount > 0', con=db)

# box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(5,5), sharex=False, sharey=False)
pyplot.show()

# histograms
dataset.hist()
pyplot.show()

# scatter plot matrix
scatter_matrix(dataset)
pyplot.show()