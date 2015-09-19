import csv
import webbrowser
import msvcrt # built-in module

options = dict()
        
print("Thank you for using InstaSite")
print("Your options are: \n")

#read CSV file into options dict
with open('itemList.csv', 'rb') as csvfile:
    itemListReader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    for row in itemListReader:
        #print ', '.join(row['keyPressed']), ' to order ', ''.join(row['name'])
        options[row['keyPressed']] = row['link']
csvfile.close()

#grab data
#item = raw_input("order something:")

def kbfunc():
    return ord(msvcrt.getch()) if msvcrt.kbhit() else 0

##item2=0
##while item2 == 0:
##    item2 = kbfunc()

x = keyboard.read(1000, timeout = 0)

if len(x):
    print ''.join(repr(x))

defaultBrowser = webbrowser.get('windows-default')

###check for first entered sandwich type 
##for x in options:
##    if x in item:
##        #print "Opening ", options[x]
##        defaultBrowser.open(options[x], new=1)
        



