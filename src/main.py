
import schedule
import time
from datetime import datetime
from fetch_data import fetch_weather_data
from store_data import init_db, store_weather_data
from visualize_data import plot_time_series, plot_bar, plot_box, plot_heatmap, plot_wind_speed_distribution, plot_scatter, plot_histogram, plot_pie_chart

def job():
    print("Starting Job")
    api_key = ''
    location = 'Pune, IN'
    data = fetch_weather_data(api_key, location)
    if data:
        store_weather_data(
            location,
            data['main']['temp'],
            data['main']['humidity'],
            data['wind']['speed']
        )
        print(f"Fetched data successfully at {datetime.now()}")
    else:
        print("Failed to fetch data")

def daily_analysis():
    print("Running Analysis")
    plot_time_series()
    plot_bar()
    plot_box()
    plot_heatmap()
    plot_wind_speed_distribution()
    plot_scatter()
    plot_histogram()
    plot_pie_chart()

if __name__ == '__main__':
    init_db()
    job()
    daily_analysis()
    schedule.every(2).minutes.do(job)
    schedule.every().day.at("00:00").do(daily_analysis)

    while True:
        schedule.run_pending()
        time.sleep(1)
