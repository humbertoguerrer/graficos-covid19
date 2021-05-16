import pandas as pd
import plotly as py
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/humbe/dados/covid19.csv', parse_dates=['Date_reported'])

grupo = df.groupby(['Country','WHO_region'])['Cumulative_cases'].max()

p = grupo.keys().tolist()
paises = [i[0] for i in p]
continentes = [i[1] for i in p]

valores = grupo.tolist()

for i, v in enumerate(continentes):
    if v == 'AFRO':
        continentes[i] = 'África'
    if v == 'AMRO':
        continentes[i] = 'Américas'
    if v == 'SEARO':
        continentes[i] = 'Ásia'
    if v == 'EURO':
        continentes[i] = 'Europa'
    if v == 'EMRO':
        continentes[i] = 'Mediterrâneo'
    if v == 'WPRO':
        continentes[i] = 'Pacífico'
        
df_tree = pd.DataFrame(dict(paises=paises,continentes=continentes,valores=valores))

df_tree["all"] = "Regiões"
fig = px.treemap(df_tree, path=['all', continentes, paises], values=valores)
fig.show()