from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get('https://phptravels.com/demo/') #Open traveldocumentation window
driver.maximize_window() # For maximizing window

driver.execute_script("window.open('https://temp-mail.org/en/');") #Open temporary mail where you will get info
#driver.switch_to.window(driver.window_handles[1]) #switch to use the temp mail window

driver.switch_to.window(driver.window_handles[1])

time.sleep(10)

emailTemp = driver.find_element('xpath', '//*[@id="tm-body"]/div[1]/div/div/div[2]/div[1]/form/div[2]/button').click() #copy temp email address

driver.switch_to.window(driver.window_handles[0])

firstName = driver.find_element('xpath', '//*[@id="content"]/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/input[1]')
firstName.send_keys('Oskari')

lastName = driver.find_element('xpath', '//*[@id="content"]/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/input[2]')
lastName.send_keys('Kurtti')

businessName = driver.find_element('xpath', '//*[@id="content"]/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/input[3]')
businessName.send_keys('Oskar.IO')

email = driver.find_element('xpath', '//*[@id="content"]/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/input[4]')
email.send_keys(Keys.CONTROL, 'v')

first_NumAsStr = driver.find_element('xpath', '//*[@id="numb1"]').text


second_NumAsStr = driver.find_element('xpath', '//*[@id="numb2"]').text


var1 = int(first_NumAsStr)
var2 = int(second_NumAsStr)
total = var1 + var2

resultInsert = driver.find_element('xpath', '//*[@id="number"]')
resultInsert.send_keys(total)

submitButton = driver.find_element('xpath', '//*[@id="demo"]')
submitButton.click()
time.sleep(1)

driver.switch_to.window(driver.window_handles[1])

time.sleep(10)

driver.execute_script("window.scrollTo(0, 600)") 

driver.find_element('xpath', '//*[@id="tm-body"]/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/ul/li[2]/div[2]/span/a').click()

driver.quit