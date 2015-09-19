import csv
import json

print("Your options are: \n")
with open('itemList.csv', 'rb') as csvfile:
    itemListReader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in itemListReader:
        print ', '.join(row)

item = "hey"
print("Thank you for using PMS, ")
item = raw_input("order something:")

print "you ordered item", item



jimmyOrder = {
  "email": "",
  "company": "AllPlayers.com",
  "address": "14665 Midway Road",
  "apt/suite": "220",
  "city": "Addison",
  "state": "Texas",
  "zip": "75001",
  "sandwich": "country club",
  "who": "Travis",
  "bread": "French Bread",
  "cut": "true",
  "drink": "",
  "chips": "Regular Jimmy Chips",
  "cookie": "",
  "pickle": "",
  "Tomato": "NO",
  "tip": "2",
  "billing_address": "123 Main St.",
  "billing_city": "Carrollton",
  "billing_state": "Texas",
  "billing_zip": "75007"
}

print(json.dumps(jimmyOrder))

f = open('order.json', 'w')
f.write(json.dumps(jimmyOrder))
f.close()
