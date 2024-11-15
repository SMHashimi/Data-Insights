import pandas

weather_data = pandas.read_csv("weather_data.csv")
# print(weather_data["temp"])
# print(type(weather_data))
# print(type(weather_data["condition"]))

# weather_data_dict = weather_data.to_dict()
# print(weather_data_dict)

#Finding the average of temperature
# print(type(weather_data))
# print(type(weather_data["temp"]))

# temp_to_list = weather_data["temp"].to_list()
# length = len(temp_to_list)
# total = 0                     ##calculating the avg
# for sum in temp_to_list:
#     total += sum
# avg = total / length
# print(round(avg))

#or
# print(weather_data["temp"].mean())
# print(weather_data["temp"].max())

#Opening rows in a dataset
# print(weather_data[weather_data.day == "Monday"])
# print(weather_data[weather_data.temp == weather_data.temp.max()])

print(type(weather_data.temp))
weather_data_list = weather_data.temp.to_list()
total = 0
length = len(weather_data_list)
for temp in weather_data_list:
    total = total + temp
print(total / length)
