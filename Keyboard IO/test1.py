import csv
import json

tomato = "YES"

print("Your options are: \n")
with open('itemList.csv', 'rb') as csvfile:
    itemListReader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in itemListReader:
        print ', '.join(row)

item = "hey"
print("Thank you for using PMS, ")
item = raw_input("order something:")

print "you ordered item", item
if '1' in item:
    print ("You're getting a ham & cheese")
    sandwichType = "ham & cheese"
elif '2' in item:
    print ("You're getting a roast beef")
    sandwichType = "roast beef"
if '3' in item:
    print ("You're not getting tomatao")
    tomato = "NO"

# we have access to 0-9, enter, plus, 

jimmyOrder = {
  "email": "",
  "company": "",
  "address": "Coover Hall",
  "apt/suite": "",
  "city": "Ames",
  "state": "Iowa",
  "zip": "50014",
  "sandwich": sandwichType,
  "who": "Travis",
  "bread": "French Bread",
  "cut": "true",
  "drink": "",
  "chips": "Regular Jimmy Chips",
  "cookie": "",
  "pickle": "",
  "Tomato": tomato,
  "tip": "2",
  "billing_address": "123 Main St.",
  "billing_city": "Carrollton",
  "billing_state": "Texas",
  "billing_zip": "75007"
}


f = open('order.json', 'w')
f.write(json.dumps(jimmyOrder))
f.close()
