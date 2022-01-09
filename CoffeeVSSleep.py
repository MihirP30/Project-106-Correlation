# import csv
# import plotly.express as px

# with open("cups of coffee vs hours of sleep.csv") as f:
#     df = csv.DictReader(f)
#     fig = px.scatter(df, x="Coffee in ml", y="sleep in hours", color="week")
#     fig['layout']['yaxis']['autorange'] = "reversed"
#     fig.show()

import numpy as np
import csv
import plotly.express as px

def getDataSource(data_path):
    coffee = []
    sleep = []
    
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    
        return{"x":coffee, "y":sleep}
    
def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation between the amount of coffee and the amount of sleep is: \n", correlation[0,1])

def setup():
    data_path = "cups of coffee vs hours of sleep.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)

setup()