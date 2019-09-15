import csv

# Get high tempreatures from file.
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)
    
    print(highs)

    for index, column_header in enumerate(header_row):
        print(index, column_header)