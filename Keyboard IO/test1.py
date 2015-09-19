import csv
import json

tomato = "YES"
options = dict()
i=0

print("Your options are: \n")
with open('itemList.csv', 'rb') as csvfile:
    itemListReader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    for row in itemListReader:
        print ', '.join(row['keyPressed']), ' to order ', ''.join(row['option'])
        options[row['keyPressed']] = row['option']
        i = i +1 
        
print("Thank you for using InstaJim")
item = raw_input("order something:")


#check for sandwich type and tomato
for x in options:
    if x in item:
        print "You're getting a ", options[x]
        sandwichType = options[x]
        break


# create the json object with the correct sandwich type

jimmyOrder = {
  "email": "",
  "company": "",
  "address": "Coover Hall",
  "apt/suite": "",
  "city": "Ames",
  "state": "Iowa",
  "zip": "50014",
  "sandwich": sandwichType,
  "who": "Mr. HackISU",
  "bread": "French Bread",
  "cut": "true",
  "drink": "",
  "chips": "",
  "cookie": "",
  "pickle": "",
  "Tomato": "",
  "tip": "2",
  "billing_address": "123 Main St.",
  "billing_city": "Carrollton",
  "billing_state": "Texas",
  "billing_zip": "75007"
}


#write json to file just for makemeasandwich api
f = open('order.json', 'w')
f.write(json.dumps(jimmyOrder))
f.close()




