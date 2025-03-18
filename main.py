from data_fetch import fetch_weather
from data_processing import analyse_weather
from visualization import plot_temp_trend
from utils import save_to_csv

def main():
    city = input("Enter city name: ")
    df=fetch_weather(city)

    if df is not None:
        analysis=analyse_weather(df)
        print("\nWeather Analysis:")
        for key,value in analysis.items():
            print(f"{key}: {value:.2f}")

        plot_temp_trend(df,city)
        save_to_csv(df)
        print("Saved to csv")

if __name__=="__main__":
    main()