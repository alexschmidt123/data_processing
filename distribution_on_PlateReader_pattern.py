import csv
from itertools import islice

# Open the input CSV file and read the data
with open('test_file/05272023.csv', 'r') as infile:
    reader = csv.reader(infile)
    data = [list(map(float, row)) for row in reader]
# column numbers for each record
len_2d = [3,5,7,7,7,5,3]

# convert the record information from data to output_data line by line
def convert(listA, len_2d):
    res = iter(listA)
    return [list(islice(res,i)) for i in len_2d]
output_data=list()
for row in data:
    res = [convert(row, len_2d)]
    output_data.append(res)

# modify records line by line to fit plate reader scan pattern
for row in output_data:
    for i in range(0, 7):
        s = len(row[0][i])
        diff = int((7-s)/2);
        for j in range (0,diff):
            row[0][i].insert(0," ")
            row[0][i].append(" ")
            
# Open the output CSV file and write the output data
with open('test_file/05272023_output.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    for row in output_data:
        writer.writerows(row[0])
        writer.writerows("  ")
