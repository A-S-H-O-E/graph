import pandas as pd
import plotly.express as px
df = pd.read_csv('data.csv')
graph = px.bar(df, x = 'Country', y = 'Population')
graph.show()