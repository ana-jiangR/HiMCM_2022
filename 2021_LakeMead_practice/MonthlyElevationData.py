# import pygal

# bar_chart = pygal.Bar()
# bar_chart.title = 'Browser usage evolution (in %)'
# bar_chart.x_labels = map(str, range(2002, 2013))
# bar_chart.add('Firefox', [None, None, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
# bar_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
# bar_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
# bar_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
# bar_chart.render()



from cmath import nan
import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_excel("LakeMead_MonthlyElevationData.xlsx", index_col=0)

MonthList = ['JAN', 'FEB',	'MAR',	'APR',	'MAY',
             'JUN',	'JUL',	'AUG',	'SEP',	'OCT',	'NOV',	'DEC']
YearStart = 1935
YearEnd   = 2021

Maxi = 0
Mini = 20000
newdf = pd.DataFrame(columns=['Month', 'Year', 'Elevation'])
for year in range(YearStart, YearEnd+1):
    for mth in MonthList:
        Ele = df.at[year, mth]
        Maxi = max(Maxi, Ele)
        Mini = min(Mini,Ele)
        new_row = pd.Series({'Month': mth, 'Year': year, 'Elevation': Ele})
        newdf = pd.concat([newdf, new_row.to_frame().T], ignore_index=True)

# print(newdf)


# df = px.data.gapminder()
# df = pd.read_csv("gapminderDataFiveYear.csv")
# df = pd.read_csv("animationLakeMead.csv")

# fig = px.bar(df, x="continent", y="pop", color="continent",
#   animation_frame="year", animation_group="country", range_y=[0,4000000000])

fig = px.bar(newdf, x="Month", y="Elevation", color="Month",
             animation_frame="Year", range_y=[Mini-50, Maxi+50], width=1500, height=1000, title= "Elevation of water at Lake Mead (in feet above sea level) at end of month by year")

fig.write_html("animationLakeMead.html")

fig.show()



