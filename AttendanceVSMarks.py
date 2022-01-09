import numpy as np
import csv
import plotly.express as px

def getDataSource(data_path):
    days_present = []
    marks_in_percentage = []
    
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            days_present.append(float(row["Days Present"]))
            marks_in_percentage.append(float(row["Marks In Percentage"]))
    
        return{"x":days_present, "y":marks_in_percentage}
    
def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation between the Attendance and the Average Marks is: \n", correlation[0,1])

def setup():
    data_path = "Student Marks vs Days Present.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)

setup()