import pandas as pd
import plotly as py
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/humbe/dados/covid19.csv', parse_dates=['Date_reported'])

df_br = df[df['Country_code'] == 'BR'].copy()

df_br['data'] = df_br['Date_reported'].dt.strftime('%d/%m/%Y')

fig = plt.figure(figsize=(15,5))
plt.title('COVID-19 - Brasil')
plt.xlabel('Datas')
plt.ylabel('Pessoas contaminadas')

plt.plot( df_br['data'], df_br['Cumulative_cases'], label='Casos')
plt.plot( df_br['data'], df_br['Cumulative_deaths'], label='Óbitos')

plt.xticks(rotation=75, ticks=df_br['data'][::10])

plt.grid(True)
plt.legend() 
plt.show()