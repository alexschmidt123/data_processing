import csv

# Open the input CSV file and read the data
with open('test_file/05122023.csv', 'r') as infile:
    reader = csv.reader(infile)
    data = [list(map(float, row)) for row in reader]

# Sort each row and calculate the average of the 6 largest numbers
for row in data:
    row.sort(reverse=True)
    row.append(sum(row[:6]) / 6)

# Open the output CSV file and write the data
with open('test_file/05122023_output.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(data)