import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# get the path of ChromeDriverServer
dir = os.path.dirname(os.path.realpath(__file__))
chrome_driver_path = dir + "/driver/chromedriver"

# create a new Chrome session
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to the application home page
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdAsr-EzqpZBmJS5M_7jPQ5h_o9xrOLLS9gKX07aYa-cGKdPg/viewform")

#for Email address
email_address = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/input')
email_address.send_keys("abhinish@prodevans.com")

#for Resouce Name
resource_name = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]')
resource_name.send_keys("abhi")

#for Employee Type
resource_type = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div[1]')
resource_type.send_keys("E")

# for Day and time
date = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[4]/div/div[2]/div/div[2]/div[1]/div/div[1]/input')
date.send_keys("14/12/2019")

# for Work Location
work_location = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[5]/div/div[2]/div[1]/div[1]/div[1]')
work_location.send_keys("client")

# for Project Details
project_details = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[6]/div/div[2]/div[1]/div[1]/div[1]')
project_details.send_keys("ANZ")


#for Hours Spent on Project
hours_spend = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[7]/div/div[2]/div/div[1]/div/div[1]/input')
hours_spend.send_keys("9.9")

# get the search textbox
# search_field = driver.find_element_by_name("q")
#
# # enter search keyword and submit
# search_field.send_keys("Selenium WebDriver Interview questions")
# search_field.submit()
#
# # get the list of elements which are displayed after the search
# # currently on result page using find_elements_by_class_name method
# lists= driver.find_elements_by_class_name("r")
#
# # get the number of elements found
# print ("Found " + str(len(lists)) + " searches:")
#
# # iterate through each element and print the text that is
# # name of the search
#
# i=0
# for listitem in lists:
#    print (listitem.get_attribute("innerHTML"))
#    i=i+1
#    if(i>10):
#       break

# close the browser window
#driver.quit()