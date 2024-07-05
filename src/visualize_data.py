import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sqlite3
import plotly.express as px
import os

def fetch_all_data():
    conn = sqlite3.connect('weather_data.db')
    df = pd.read_sql_query('SELECT * FROM weather', conn)
    conn.close()
    return df

def plot_time_series():
    df = fetch_all_data()
    plt.figure(figsize=(14, 7))
    sns.lineplot(x=pd.to_datetime(df['timestamp']), y=df['temperature'], label='Temperature')
    sns.lineplot(x=pd.to_datetime(df['timestamp']), y=df['humidity'], label='Humidity')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Weather Trends')
    plt.legend()
    plt.show()

def plot_bar():
    df = fetch_all_data()
    df['date'] = pd.to_datetime(df['timestamp']).dt.date
    daily_avg = df.groupby('date')[['temperature', 'humidity', 'wind_speed']].mean().reset_index()

    plt.figure(figsize=(14, 7))
    sns.barplot(x='date', y='temperature', data=daily_avg, color='blue')
    plt.xlabel('Date')
    plt.ylabel('Average Temperature (°C)')
    plt.title('Daily Average Temperature')
    plt.xticks(rotation=45)
    plt.show()

def plot_box():
    df = fetch_all_data()
    plt.figure(figsize=(14, 7))
    sns.boxplot(x='location', y='temperature', data=df)
    plt.xlabel('Location')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Distribution by Location')
    plt.show()

def plot_heatmap():
    df = fetch_all_data()
    corr = df[['temperature', 'humidity', 'wind_speed']].corr()

    plt.figure(figsize=(14, 7))
    sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Heatmap')
    plt.show()

def plot_wind_speed_distribution():
    df = fetch_all_data()
    plt.figure(figsize=(14, 7))
    sns.histplot(df['wind_speed'], bins=20, kde=True)
    plt.xlabel('Wind Speed (m/s)')
    plt.ylabel('Frequency')
    plt.title('Wind Speed Distribution')
    plt.show()

def plot_scatter():
    df = fetch_all_data()
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    fig = px.scatter(df, x='temperature', y='humidity', color='timestamp',
                     title='Temperature vs Humidity Scatter Plot',
                     labels={'temperature': 'Temperature (°C)', 'humidity': 'Humidity (%)'},
                     hover_data=['timestamp'])
    fig.show()

def plot_histogram():
    df = fetch_all_data()
    plt.figure(figsize=(14, 7))
    sns.histplot(df['temperature'], bins=20, kde=True)
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Frequency')
    plt.title('Temperature Distribution')
    plt.show()

def plot_pie_chart():
    df = fetch_all_data()

    conditions = [
        (df['humidity'] < 30),
        (df['humidity'] >= 30) & (df['humidity'] <= 60),
        (df['humidity'] > 60)
    ]
    choices = ['Low Humidity', 'Medium Humidity', 'High Humidity']
    df['humidity_category'] = pd.cut(df['humidity'], bins=[-1, 30, 60, 100], labels=choices)

    humidity_counts = df['humidity_category'].value_counts().reset_index()
    humidity_counts.columns = ['Category', 'Count']

    fig = px.pie(humidity_counts, names='Category', values='Count', title='Humidity Distribution')
    fig.show()

if __name__ == '__main__':
    plot_time_series()
    plot_bar()
    plot_box()
    plot_heatmap()
    plot_wind_speed_distribution()
    plot_scatter()
    plot_histogram()
    plot_pie_chart()
