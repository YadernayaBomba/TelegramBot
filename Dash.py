import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import dash_table

# Считываем данные из CSV-файла
file_path = 'Данные.csv'
df = pd.read_csv(file_path)

# Преобразуем столбы в формат datetime
df['StartDate'] = pd.to_datetime(df['StartDate'])
df['ExpirationDate'] = pd.to_datetime(df['ExpirationDate'], errors='coerce')

# Создаем веб-приложение
app = dash.Dash(__name__)

# Запускаем веб-приложение
if __name__ == '__main__':
    app.run_server(debug=True)
