import pandas as pd
data1 = pd.read_csv("cultivated_area.csv")
data2 = pd.read_csv("production.csv")

import plotly
from plotly.graph_objs import Scatter, Layout, Bar

plottedData1 = Bar(
    x = data1.Year,
    y = data1.Cultivated,
    name = "Cultivated area",
    marker = dict(color = 'rgba(85, 135, 237, 0.9)')
)

plottedData2 = Scatter(
    x = data2.Year,
    y = data2.Production,
    name = "Production",
    mode = "lines+markers",
    line = dict(width = 5),
    yaxis='y2'
)

data = [plottedData1, plottedData2]
layout = Layout(title = "Tangerine cultivation area and harvest trend in Korea",
                xaxis = dict(title = 'Year', dtick = 1),
                yaxis1 = dict(title = 'Cultivated area (unit: ha)'),
                yaxis2 = dict(title = 'Production (unit: ton)', overlaying = 'y', side = 'right')
              )

fig = plotly.offline.plot({
    "data": data,
    "layout": layout},
    image='png', image_filename='fig1'
)

#plotly.offline.plot({
#    "data": [Scatter(x=data1["Year"], y=data1["Cultivated area"]), Scatter(x=data2["Year"], y=data2["Production"])],
#    "layout": Layout(title="Tangerine cultivation area and harvest trend in Korea", xaxis= dict(title= 'Year'))
#})
