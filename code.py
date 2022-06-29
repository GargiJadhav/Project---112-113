#---------------------------------Hi Reader 👋------------------------------------------


# This project contains two projects , means ( Project-112 & Project-113)



#-------------------------------PROJECT - 112-----------------------------------------
import pandas as pd
import plotly.express as pe
import csv
import plotly.graph_objects as go
import statistics as st
import numpy as np
import plotly.figure_factory as pf
import random
#import seaborn as sns

data = pd.read_csv("data.csv")

savings = data["quant_saved"].tolist()

female = data["female"].tolist()

graph = pe.scatter(data , y = savings , color = female)

#graph.show()

with open("data.csv") as file :
    read = csv.reader(file)
    savingsData=list(read)

print(savingsData[0])
savingsData.pop(0)

totalFemales = 0

totalMale = 0

for i in savingsData:
    if int(i[2]) == 1:
        totalFemales = totalFemales + 1
    else :
        totalMale = totalMale + 1

graph = go.Figure(go.Bar(x = ["Females , Male"] , y = [totalFemales , totalMale]))
#graph.show()

#------------------------------Mean / Mode / Median of savings of all people----------------

mean = st.mean(savings)
mode = st.mode(savings)
median = st.median(savings)

print("---------------All People-----------------")
print("Mean is " , mean)
print("Mode is ", mode)
print("Median is ", median)

#------------------------------Mean / Mode / Median of female-------------------------------
females = []
males = []

for i in savingsData:
    if int(i[2]) == 1:
        females.append( float(i[0]) )
    else :
        males.append( float(i[0]) )

mean = st.mean(females)
mode = st.mode(females)
median = st.median(females)

print("---------------Only Females-----------------")
print("Mean is " , mean)
print("Mode is ", mode)
print("Median is ", median)

#------------------------------Mean / Mode / Median of female-------------------------------

mean = st.mean(males)
mode = st.mode(males)
median = st.median(males)

print("---------------Only Males-----------------")
print("Mean is " , mean)
print("Mode is ", mode)
print("Median is ", median)

#-------------------------------------Correlation--------------------------------------------

highSchoolCompletion = data["highschool_completed"].tolist()

correlation = np.corrcoef(highSchoolCompletion , savings)

print("Correlation is" , correlation[0,1])

#---------------------Not at all relation 🤣🤣----------------------------------------

graph = pf.create_distplot([savings] , ["Savings"] , show_hist=False)

#graph.show()

#----------------------------------The Happy End 😃---------------------------------------

#---------------------------------A New Start 😇-----------------------------------------

#--------------------------------PROJECT - 113-----------------------------------------

q1 = data["quant_saved"].quantile(0.25)

q3 = data["quant_saved"].quantile(0.75)

iqr = q3-q1
#------------------------------Project-113
print(q1,q3,iqr)


lowerWhisker = q1 - 1.5*iqr
upperWhisker = q3 + 1.5*iqr

print("Lower Whisker is ", lowerWhisker)
print("Upper Whisker is ", upperWhisker)

#---------------------------------Creating New Data -----------------------------------------------

newData = data[data["quant_saved"] < upperWhisker]

newSavings = newData["quant_saved"]

mean = st.mean(newSavings)
mode = st.mode(newSavings)
median = st.median(newSavings)
stdev = st.stdev(newSavings)

print("Mean of New Df is" , mean)
print("Mode of New Df is" , mode)
print("Median of New Df is" , median)
print("Stdev of New Df is" , stdev)


graph = pf.create_distplot( [newSavings] , ["Savings"] , show_hist=False )

#graph.show()

#----------------------------------Sampling 🧪🧪-------------------------------------

meanList=[]

for i in range(1000):
    dataSet=[]
    for i in range(100):
        id = random.choice(newSavings)
        dataSet.append(id)
    meanList.append(st.mean(dataSet))



meanOfSample = st.mean(meanList)
stdevOfSample = st.stdev(meanList)

print("-------------------------------------------")
print("Mean of  sample is" , meanOfSample)
print("Stdev of  sample is" , stdevOfSample)


graph = pf.create_distplot( [meanList] , ["Savings"] , show_hist=False )

graph.show()

#----------------------------------Completed 🎊🎉--------------------------------------------------

