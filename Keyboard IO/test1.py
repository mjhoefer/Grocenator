import csv

item = "hey"
print("Thank you for using PMS, ")
item = raw_input("order something:")

print"you ordered item", item

with open('eggs.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
    print ', '.join(row)
