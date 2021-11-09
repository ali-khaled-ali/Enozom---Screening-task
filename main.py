#! python3
import json
import csv

file = open("countries.json")

data = json.load(file)

header = ["Country Name", "Number of cities", "City with max length"]

max_city_name = ""
total_cities = 0

with open('countries.csv', 'w') as f:
    writer = csv.writer(f)

    writer.writerow(header)

    for countries, cities in data.items():
        total_cities += (len(cities))

        for city in cities:
            if len(city) > len(max_city_name):
                max_city_name = city

        writer.writerow([countries, len(cities), max(cities, key=len)])


print(max_city_name)
print(total_cities)