
# with open("./weather_data.csv") as weather_data:
#     contents = weather_data.readlines()

import csv
with open("weather_data.csv") as weather_report:
    data = csv.reader(weather_report)
    # print(data)
    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature.append(row[1])
    # print(temperature)
    for temp in range(0, len(temperature)):
        temperature[temp] = int(temperature[temp])
    print(temperature)

#There is no need to write several lines of codes while Pandas is around
#Important: Pandas library should be installed first.

import pandas
weather_data = pandas.read_csv("weather_data.csv")
print(weather_data)
print(weather_data["temp"])

