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

# Группируем данные по годам и создаем временную диаграмму
grouped = df.groupby(df['StartDate'].dt.year)['Participants'].sum().reset_index()
time_series_figure = px.line(grouped, x='StartDate', y='Participants', title='Количество участников по годам')

# Создаем круговую диаграмму
pie_chart_figure = px.pie(df, names='Status')

# Создаем гистограмму
histogram = px.histogram(df, x='Category')

# Запускаем веб-приложение
if __name__ == '__main__':
    app.run_server(debug=True)
