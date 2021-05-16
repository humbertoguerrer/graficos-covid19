import pandas as pd
import plotly as py
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/humbe/dados/covid19.csv', parse_dates=['Date_reported'])

df_am = df[df['WHO_region'] == 'EURO'].copy()

paises = df_am.groupby(['Country'])['Cumulative_cases'].max()

data = dict (
    type = 'choropleth',
    locations = paises.keys(),
    locationmode='country names',
    z = paises.tolist(),
    colorbar_title = 'Casos',
    colorscale = 'blues'
)

mapa = go.Figure(data=[data])
mapa.update_layout(
    title_text = 'Casos de COVID-19 no continente europeu',
)
mapa.show( )