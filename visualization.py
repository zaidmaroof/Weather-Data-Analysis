import matplotlib.pyplot as plt

def plot_temp_trend(df, city):
    plt.figure(figsize=(10,5))
    plt.plot(df["date"],df["temperature"], marker='o',linestyle='-',color='b',label="Temperature (°C)")
    plt.xlabel("Date-Time")
    plt.ylabel("Temperature (°C)")
    plt.title(f"Temperature Trend for {city}")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    plt.show()