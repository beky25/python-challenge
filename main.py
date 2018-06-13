import os
import csv
csv1=os.path.join('..','Homework','03-Python','Instructions','PyBank','raw_data','budget_data_1.csv')
with open(csv1,newline='') as csv2:
    csvfile=csv.reader(csv2,delimeter=',')
#create lists to in rows 
    year=[]
    Revenue=[]
#loop through every row
    for row in csvfile:
        year.append(row[0])
        Revenue.append(int (row[1]))
    
    date = len(year)
    Rev = sum(Revenue)

    print("Financial Analysis")
    print("Total Months:", len(year))
    print("Total Revenue: $", sum(Rev))

