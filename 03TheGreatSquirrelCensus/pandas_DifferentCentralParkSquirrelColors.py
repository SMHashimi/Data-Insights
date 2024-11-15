import pandas

primary_fur_color = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(primary_fur_color["Primary Fur Color"])


gray = len(primary_fur_color[primary_fur_color["Primary Fur Color"] == "Gray"])
cinnamon = len(primary_fur_color[primary_fur_color["Primary Fur Color"] == "Cinnamon"])
black = len(primary_fur_color[primary_fur_color["Primary Fur Color"] == "Black"])
print(gray)
print(cinnamon)
print(black)

primary_fur_color_dict = {
    "Fur Color": ["Gray", "Black" , "Cinnamon" ],
    "Count": [gray, black, cinnamon]
}
primary_fur_color_to_data_frame = pandas.DataFrame(primary_fur_color_dict)
# print(primary_fur_color_to_data_frame)


primary_fur_color_to_data_frame.to_csv("DifferentSquirrelsColors.csv")
