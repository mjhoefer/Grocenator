# To-do
# Format into functions
#	login()
#	addToCart(url)
#	checkout()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv


options = dict()

# product_url = 'http://www.amazon.com/Post--Notes-Jaipur-Collection-654-5UC/dp/B00006JNN7/ref=sr_1_1?tag=grocerator-20'


print("Thank you for using InstaSite")
print("Your options are: \n")

#read CSV file into options dict
with open('itemList.csv', 'rb') as csvfile:
	itemListReader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
	for row in itemListReader:
		print ', '.join(row['keyPressed']), ' to order ', ''.join(row['name'])
		options[row['keyPressed']] = row['link']
csvfile.close()

#grab data

item = raw_input("Select items to order:")





#def fun_start_driver():
driver = webdriver.Chrome()
driver.set_window_size(1366, 768)
	#return(driver)

#def fun_login(driver):
driver.get('https://www.amazon.com/ap/signin/180-2149652-6711159?_encoding=UTF8&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fsign-in.html%2F180-2149652-6711159%3Fie%3DUTF8%26*Version*%3D1%26*entries*%3D0')
	# Sets up variables
	 
email = driver.find_element_by_xpath('//*[@id="ap_email"]')
password = driver.find_element_by_xpath('//*[@id="ap_password"]')

	# Input
email.send_keys('da.peiffer@gmail.com')
password.send_keys('admin967%')

	# Logs into Amazon.  For some reason, it does not redirect to the homepage, however a new session is started

test = driver.find_element_by_id('signInSubmit-input')
    
if test = 'NoSuchElementException':
    print('Login error')







        # idType =  'signInSubmit-input'
        # print('--------------')
        # #print(driver.find_element_by_xpath('signInSubmit'))
        # try:
        # 	driver.find_element_by_id(idType) 
        # except Exception e:
        #     idType = 'signInSubmit'

        # login = driver.find_element_by_xpath('//*[@id="signInSubmit-input"]')
        # login.send_keys(Keys.ENTER)
        # print('First login screen\nLogin Successful!\n')
        # #print('Login Successful!')

        # driver.find_element_by_id('signInSubmit') != 'NoSuchElementException':
        # login = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
        # login.send_keys(Keys.ENTER)
        # print('Second login screen\nLogin Successful!\n')

#def fun_add_to_cart():
	# Login is assumed to be successful.  Go to the page of the product we're interested in buying.

for x in options:
		if x in item:
				print "Opening ", options[x]
				driver.get(options[x])
				add_item_to_cart = driver.find_element_by_xpath('//*[@id="add-to-cart-button"]')
				if add_item_to_cart <> 'NoSuchElementException':
						add_item_to_cart.send_keys(Keys.ENTER)
						print('Item added to cart\n\n')
				else:
						print('ERROR - Could not be added to cart!\n\n')

# Checkout
#def fun_checkout():
btn_proceed_to_checkout = driver.find_element_by_xpath('//*[@id="hlb-ptc-btn-native"]')

if btn_proceed_to_checkout <> 'NoSuchElementException':
	btn_proceed_to_checkout.send_keys(Keys.ENTER)
	print('At checkout screen\n\n')

# global_driver = fun_start_driver()
# fun_login(global_driver)
# fun_add_to_cart()
