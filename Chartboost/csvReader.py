import sys
import csv

f = open(sys.argv[1])
csv_f = csv.reader(f)

csvList = {}
for row in csv_f:
	csvList.setdefault(row[0],[]).append(row[1])
print(csvList)


