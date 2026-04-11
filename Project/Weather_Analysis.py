import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Python Practice/Matplotlib/Project/Weather Data.csv")

# print(df.head())
# print(df.tail())
# print(df.info())
print("Welcome to the weather application")

while True:
    year = int(input("Enter year (1901 to 2017) and for exit enter 7: "))
    if year == 7:
        break
    elif year > 1900 and year < 2018:
        year_wise_data = df[df['YEAR'] == year]
        # print(year_wise_data.head())

        months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
                  'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
        values = year_wise_data[months].values[0]
        colors = [
            '#6C5B7B', '#C06C84', '#F67280', '#F8B195',
            '#355C7D', '#99B898', '#FECEAB', '#FF847C',
            '#2A363B', '#E84A5F', '#FFB400', '#00A8CC'
        ]
        # print(values)

        plt.bar(months, values, color=colors)
        plt.title(f"YEAR {year} weather details")
        plt.xlabel("Months")
        plt.ylabel("Celsius")
        plt.show()
    else:
        print("Invalid year,Please enter a valid year!!")
print("Thanks for using this application.I hope! you enjoy it...")
