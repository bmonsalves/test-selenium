from selenium import webdriver
from login import Login
from dropdown import Dropdown

driver = webdriver.Chrome('drivers/chromedriver')
driver.get('http://newtours.demoaut.com/')
driver.implicitly_wait(5)
# prueba login
login = Login(driver)
login.test_login()

# prueba dropdown
dropdown = Dropdown(driver)
dropdown.test_dropdown()

driver.implicitly_wait(5)
driver.quit()
