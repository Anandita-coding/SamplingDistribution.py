import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics 
import random

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

fig = ff.create_distplot([data],["Result"],show_hist = False)
fig.show()


def randomSetofMeans(counter):
  randomSamples = []

  for i in range(0,counter):
    index = random.randint(0,len(data)-1)
    value = data[index]
    randomSamples.append(value)

  mean = statistics.mean(randomSamples)

  return mean

def showFigure(randomSamples):
  mean = statistics.mean(randomSamples)
  mean1 = statistics.mean(data)
  sd = statistics.stdev(randomSamples)
  print("The mean of the sample is ", mean)
  print("The mean of the population is ", mean1)
  print("The Standard deviation of the sample is ", sd)

  fig = ff.create_distplot([randomSamples],["Reading Time"], show_hist = False)
  fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.8], mode = "lines", name = "Mean"))
  fig.show()


def main():
  meanList = []

  for i in range(0,1000):
    setOfMean = randomSetofMeans(100)
    meanList.append(setOfMean)

  showFigure(meanList)
main()

