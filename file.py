import csv

data = [
    ["Name", "Age", "Country"],
    ["John", 25, "USA"],
    ["Emma", 32, "Canada"],
    ["Alex", 19, "UK"]
]

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
