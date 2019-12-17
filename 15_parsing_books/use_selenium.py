# To install the Python client library:
# pip install -U selenium

# Import the Selenium 2 namespace (aka "webdriver")
import os

from selenium import webdriver
# Firefox
base = os.path.dirname(__file__)
gg = os.path.join(base, 'geckodriver')
print(gg)
driver = webdriver.Firefox(executable_path=gg, headles_mode=True)

# ------------------------------
# The actual test scenario: Test the codepad.org code execution service.

# Go to codepad.org
page = driver.get('http://quotes.toscrape.com/login')
# page = driver.get('https://ukr.net')
# print(page.page_source)
# exit(0)
# # Select the Python language option
name = driver.find_element_by_xpath("//input[@id='username']")
name.setAttribute('value',  "mane")
passsss = driver.find_element_by_xpath("//input[@id='password']")
passsss.setAttribute("value" , "name")
python_link = driver.find_element_by_xpath("//input[@type='submit']")
python_link.click()
#
# # Enter some text!
# text_area = driver.find_element_by_id('textarea')
# text_area.send_keys("print 'Hello,' + ' World!'")
#
# # Submit the form!
# submit_button = driver.find_element_by_name('submit')
# submit_button.click()
#
# # Make this an actual test. Isn't Python beautiful?
# assert "Hello, World!" in driver.get_page_source()
#
# # Close the browser!
driver.quit()




# driver.title
# driver.page_source
# driver.find_element_by_id("username")
# name = driver.find_element_by_id("username")
# name.text = "Myname"
# name.send_keys('Myname')
# pasw = driver.find_element_by_id("password")
# pasw.send_keys("password")
# driver.find_element_by_class_name("btn btn-primary")
# driver.find_element_by_class_name("btn-primary")
# btn = driver.find_element_by_class_name("btn-primary")
# btn.click()
# driver.quit()