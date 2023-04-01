import pandas as pd
import plotly.figure_factory as ff
import csv

df=pd.read_csv("data.csv")
fig=ff.create_distplot([df["Avg Rating"].tolist()],["AMAZON MOBILE BRANDS AVG RATING"])
fig.show()