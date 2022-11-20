from datetime import datetime
from cmath import nan
import pandas as pd
import numpy as np
import plotly.graph_objects as go

df = pd.read_excel("LakeMead_LowHighElevationData.xlsx")
years = df.loc[:, 'Year'].tolist()
low_elv = df.loc[:, 'Low Elev'].tolist()
hi_elv = df.loc[:, 'High Elev'].tolist()

# the 1st "Date" for Low
low_date = df.loc[:, "Date"].tolist()

# the 2nd "Date" for High
print(low_date)


# low_datetime = []

# for dt in low_date:


# print(type(dt_object))


fig = go.Figure()

# hover template - 
# https://plotly.com/python/hover-text-and-formatting/#customizing-hover-text-with-a-hovertemplate 
fig.add_trace(go.Scatter(x=years, y=hi_elv, name='High Elevation'))
fig.add_trace(go.Scatter(x=years, y=low_elv, name='Low Elevation'))


fig.update_traces(mode="markers+lines")

fig.update_xaxes(showspikes=True)
fig.update_yaxes(showspikes=True)


fig.update_layout(title='The highest and lowest water elevation at Lake Mead (in feet above sea level) by year.',
                  xaxis_title='Year',
                  yaxis_title='Elevation')

fig.write_html("LowHighElevationData.html")

fig.show()


# ----

# datetime object containing current date and time
now = datetime.now()

print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%Y-%m-%d %H:%M")
print("date and time =", dt_string)


datestr = datetime.strptime(dt_string, "%Y-%m-%d %H:%M")
print(datestr.year)
print(type(datestr))

# replace YEAR
newdatestr = datestr.replace(year=2000)
print(datestr)
print(newdatestr)
