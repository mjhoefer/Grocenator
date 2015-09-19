#read key from file
import csv
import webbrowser

accessKeys = dict()

with open('rootkey.csv', 'rb') as csvfile:
    itemListReader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    for row in itemListReader:
        accessKeys[row['keyName']] = row['keyValue']

csvfile.close()

print accessKeys



#start bottlenose test
import bottlenose
amazon = bottlenose.Amazon(accessKeys['AWS_ACCESS_KEY_ID'],
                           accessKeys['AWS_SECRET_ACCESS_KEY'],
                           accessKeys['AWS_ASSOCIATE_TAG'])
response = amazon.ItemLookup(ItemId="0596520999", ResponseGroup="Images",
                             SearchIndex="Books", IdType="ISBN")

#this isn't working
#response = amazon.CartCreate(Items=response, Quantity=1)

print("NEW NEW NEW \n\n\n")
#print(response)
###start amazon api test
##api = API(locale='us')
##items = api.item_search('Books', Publisher="O'Reilly")
##
### get all books from result set and
### print author and title
##for book in items:
##    print '%s: "%s"' % (book.ItemAttributes.Author,
##                        book.ItemAttributes.Title)
##
##

#start other test
