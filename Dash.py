import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import dash_table

# Считываем данные из CSV-файла
file_path = 'Данные.csv'
df = pd.read_csv(file_path)
