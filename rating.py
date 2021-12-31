import pandas as p
import plotly.figure_factory as ff
df=p.read_csv("data.csv")
fig=ff.create_distplot([df["Avg Rating"].to_list()],["Avg Rating"])
fig.show()