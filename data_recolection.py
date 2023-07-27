import requests
import json
import sqlite3

def create_db():
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            city TEXT,
            main_weather TEXT,
            description TEXT,
            temperature REAL,
            humidity INTEGER
        )
    ''')
    conn.commit()
    return conn, c


def get_weather(conn, c, api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        weather_data = response.json()
        if 'weather' in weather_data:
            main_weather = weather_data['weather'][0]['main']
            description = weather_data['weather'][0]['description']
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']

            try:
                c.execute('''
                    INSERT INTO weather VALUES (?, ?, ?, ?, ?)
                ''', (city, main_weather, description, temperature, humidity))
                conn.commit()
            except sqlite3.Error as e:
                print(f"An error occurred while trying to insert data into the database: {e}")

            print(f"Weather in {city}:")
            print(f"Main: {main_weather}")
            print(f"Description: {description}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
        else:
            print("The 'weather' key is not in the response. Here's the full response:")
            print(weather_data)
    else:
        print(f"The API request was not successful. Status code: {response.status_code}")

def check_table_exists(conn, table_name):
    c = conn.cursor()
    c.execute(f'''
        SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';
    ''')
    result = c.fetchone()
    if result:
        print(f"The table '{table_name}' exists.")
    else:
        print(f"The table '{table_name}' does not exist.")

def main():
    conn, c = create_db()
    api_key = "api_key"  # Replace with your actual API key
    check_table_exists(conn, 'weather')
    city = "London"  # Replace with the city you want
    get_weather(conn, c, api_key, city)
    conn.close()


if __name__ == "__main__":
    main()
