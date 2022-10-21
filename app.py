from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get('https://phptravels.com/demo/') #Open traveldocumentation window
driver.maximize_window() # For maximizing window

driver.execute_script("window.open('https://temp-mail.org/en/');") #Open temporary mail where you will get info


driver.switch_to.window(driver.window_handles[1]) #switch to temp mail tab

time.sleep(10) # wait for temporary email to load

emailTemp = driver.find_element('xpath', '//*[@id="tm-body"]/div[1]/div/div/div[2]/div[1]/form/div[2]/button').click() #copy temp email address

driver.switch_to.window(driver.window_handles[0]) #switch back to first tab

firstName = driver.find_element('xpath', '//*[@id="content"]/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/input[1]')
firstName.send_keys('Oskari') #find where to enter first name /\ and then send keys containing name

lastName = driver.find_element('xpath', '//*[@id="content"]/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/input[2]')
lastName.send_keys('Kurtti')    #same as above

businessName = driver.find_element('xpath', '//*[@id="content"]/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/input[3]')
businessName.send_keys('Oskar.IO') #same as above

email = driver.find_element('xpath', '//*[@id="content"]/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/input[4]')
email.send_keys(Keys.CONTROL, 'v') #paste the copied email address from temp email

first_NumAsStr = driver.find_element('xpath', '//*[@id="numb1"]').text #find the number for first security number


second_NumAsStr = driver.find_element('xpath', '//*[@id="numb2"]').text #find the number for second security number


var1 = int(first_NumAsStr)
var2 = int(second_NumAsStr) #convert security numbers from string to int and add them
total = var1 + var2

resultInsert = driver.find_element('xpath', '//*[@id="number"]')
resultInsert.send_keys(total) #find where to add total and add it

submitButton = driver.find_element('xpath', '//*[@id="demo"]')
submitButton.click() #click submit button
time.sleep(1)

driver.switch_to.window(driver.window_handles[1]) #switch to temp mail tab

time.sleep(10) #wait for email to be received

driver.execute_script("window.scrollTo(0, 600)") #scroll to locate the email

# then this part would click the email and open it but it is deleted due to that causing block from temp mail

driver.quit