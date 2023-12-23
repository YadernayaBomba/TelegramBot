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

# Создаем таблицу
data_table = dash_table.DataTable(
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
    page_size=10,  # Количество строк на странице
    style_table={'height': '300px', 'overflowY': 'auto'},
    style_cell={
        'textAlign': 'left',
        'padding': '10px',
        'minWidth': '100px', 'width': '100px', 'maxWidth': '100px',
        'whiteSpace': 'normal'
    },
    style_header={
        'backgroundColor': 'rgb(230, 230, 230)',
        'fontWeight': 'bold'
    }
)

# Запускаем веб-приложение
if __name__ == '__main__':
    app.run_server(debug=True)
