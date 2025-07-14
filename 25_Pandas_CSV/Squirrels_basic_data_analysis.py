import pandas

data= pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250714.csv")
print(data.head())
print(data["Primary Fur Color"])
grey_squirrels= data[data["Primary Fur Color"] == "Gray"]
total_grey_squirrels = len(grey_squirrels)
print(total_grey_squirrels)
red_squirrels= data[data["Primary Fur Color"] == "Cinnamon"]
total_red_squirrels = len(red_squirrels)
print(total_red_squirrels)
total_black_squirrels=len(data[data["Primary Fur Color"] == "Black"])
print(total_black_squirrels)
data_dict = {"Fur Color": ["Gray", "Cinnamon", "Black"],
             "Count": [total_grey_squirrels, total_red_squirrels, total_black_squirrels],
             }
data_frame=pandas.DataFrame(data_dict)
print(data_frame)
data_frame.to_csv("./Total_different_Squirrels.csv")