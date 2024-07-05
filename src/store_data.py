import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location TEXT,
            temperature REAL,
            humidity INTEGER,
            wind_speed REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def store_weather_data(location, temperature, humidity, wind_speed):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('INSERT INTO weather (location, temperature, humidity, wind_speed, timestamp) VALUES (?, ?, ?, ?, ?)',
                   (location, temperature, humidity, wind_speed, timestamp))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    store_weather_data('London', 18.5, 77, 5.4)
