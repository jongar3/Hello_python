# with open("./weather_data.csv", mode="r") as f:
#     data2= f.readlines()
#     data=[]
#     for row in data2:
#         data.append(row.strip().split(','))
#     print(data)
# import csv
import pandas
# with open("./weather_data.csv") as f:
#     data=csv.reader(f)
#     data_list=list(data)
#     for row in data_list:
#         print(row)
#     temperatures= [int(row[1]) for row in data_list[1:]]
#     print(temperatures)


import pandas as pd

data= pd.read_csv("./weather_data.csv")
temperatures=data['temp']
#print([temperature for temperature in temperatures])
print(temperatures.tolist())
print(data[["temp", "day"]])
data_dict= data.to_dict()
print(data_dict)
print(data_dict["temp"])

average= sum(temperatures) / len(temperatures)
print(round(average,2))
print(data["temp"].mean())
print(data["temp"].max())
print(data.day=="Monday")
print(data[data.day == "Monday"])
print(data[data.index==0])

#Example: print the row in which the temperature is maximun

print(data[data.temp.max()==data.temp])

#Create a dataframe form scratch

data_dict =  { "students": ["Amy", "James", "Angela"],
               "scores": [90, 85, 70],
}
data= pandas.DataFrame(data_dict)
print(data)
data.to_csv("./new_data.csv")