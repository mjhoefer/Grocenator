import csv
import json
import webbrowser

options = dict()
        
print("Thank you for using InstaSite")
print("Your options are: \n")

#read CSV file into options dict
with open('itemList.csv', 'rb') as csvfile:
    itemListReader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    for row in itemListReader:
        print ', '.join(row['keyPressed']), ' to order ', ''.join(row['option'])
        options[row['keyPressed']] = row['option']
csvfile.close()

#grab data
item = raw_input("order something:")


#check for first entered sandwich type 
for x in options:
    if x in item:
        print "You're getting a ", options[x]
        sandwichType = options[x]
        webbrowser.open(options[x], new=1)
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
#makemeasandwich doesn't seem to work, so new idea is needed
f = open('order.json', 'w')
f.write(json.dumps(jimmyOrder))
f.close()



