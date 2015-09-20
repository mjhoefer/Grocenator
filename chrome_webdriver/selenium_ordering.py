# To-do
# Format into functions
#	login()
#	addToCart(url)
#	checkout()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# product_url = 'http://www.amazon.com/Post--Notes-Jaipur-Collection-654-5UC/dp/B00006JNN7/ref=sr_1_1?tag=grocerator-20'

#def fun_start_driver():
driver = webdriver.Chrome()
driver.set_window_size(1366, 768)
	#return(driver)

#def fun_login(driver):
driver.get('https://www.amazon.com/gp/sign-in.html')
	# Sets up variables
	 
email = driver.find_element_by_xpath('//*[@id="ap_email"]')
password = driver.find_element_by_xpath('//*[@id="ap_password"]')

	# Input
email.send_keys('da.peiffer@gmail.com')
password.send_keys('admin967%')

	# Logs into Amazon.  For some reason, it does not redirect to the homepage, however a new session is started


if driver.find_element_by_id('signInSubmit-input') <> 'NoSuchElementException':
	login = driver.find_element_by_xpath('//*[@id="signInSubmit-input"]')
	login.send_keys(Keys.ENTER)
	print('First login screen')
else:
	login = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
	login.send_keys(Keys.ENTER)
	print('Second login screen')

print('Login (assumed) successful!')

#def fun_add_to_cart():
	# Login is assumed to be successful.  Go to the page of the product we're interested in buying.
driver.get('http://www.amazon.com/Post--Notes-Jaipur-Collection-654-5UC/dp/B00006JNN7/ref=sr_1_1?tag=grocerator-20')


add_item_to_cart = driver.find_element_by_xpath('//*[@id="add-to-cart-button"]')

if add_item_to_cart <> 'NoSuchElementException':
	add_item_to_cart.send_keys(Keys.ENTER)
	print('Item added to cart')
else:
	print('ERROR - Could not be added to cart!')

# Checkout
#def fun_checkout():
btn_proceed_to_checkout = driver.find_element_by_xpath('//*[@id="hlb-ptc-btn-native"]')

if btn_proceed_to_checkout <> 'NoSuchElementException':
	btn_proceed_to_checkout.send_keys(Keys.ENTER)
	print('At checkout screen')

# global_driver = fun_start_driver()
# fun_login(global_driver)
# fun_add_to_cart()