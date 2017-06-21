
import time
from selenium import webdriver

# Create an instance of Firefox WebDriver
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# Navigate to Qxf2 Tutorial page        
driver.get("URL")

# Find the name field using xpath with id
name = driver.find_element_by_xpath("//input[@id='username']")
# Send text to the name element using send_keys method
name.send_keys('')

# Find the email field using xpath without id
email = driver.find_element_by_xpath("//input[@id='password']")
email.send_keys('')

# Take screenshot
driver.save_screenshot('LoginSalersforce.png')

# Identify the xpath for Click me button and click on it 
button  = driver.find_element_by_xpath("//button[text()='Log In']")  
button.click()

# Pause the script for 3 sec
time.sleep(3)

# Verify user is taken to Qxf2 tutorial redirect url
if (driver.current_url== ''):
    print ("Success")
else:
    print ("Failure")

print (driver.current_url)

# Pause the script for 3 sec
time.sleep(3)

# Close the browser       
driver.close()
