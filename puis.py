import time
from selenium import webdriver

web = webdriver.Chrome()
web.get('https://puis.president.ac.id')

username = web.find_element_by_id("email")
password = web.find_element_by_id("pass")

username.send_keys("newbie.xtkj2@gmail.com")
password.send_keys("Okky1910dtf")

web.find_element_by_xpath('//*[@id="login"]/dl/dd[3]/input').click()
time.sleep(2)
web.get('https://puis.president.ac.id/student/custom_lecturing_evaluation/middle/2002256425/8206')

RadioButtonPeriod = web.find_element_by_xpath('//*[@id="2002256425"]/tbody/tr[3]/td[5]/input')
RadioButtonPeriod.click() #1
RadioButtonPeriod = web.find_element_by_xpath('//*[@id="2002256425"]/tbody/tr[4]/td[5]/input')
RadioButtonPeriod.click() #2
RadioButtonPeriod = web.find_element_by_xpath('//*[@id="2002256425"]/tbody/tr[5]/td[5]/input')
RadioButtonPeriod.click() #3
RadioButtonPeriod = web.find_element_by_xpath('//*[@id="2002256425"]/tbody/tr[6]/td[5]/input')
RadioButtonPeriod.click() #4
RadioButtonPeriod = web.find_element_by_xpath('//*[@id="2002256425"]/tbody/tr[7]/td[5]/input')
RadioButtonPeriod.click() #5
RadioButtonPeriod = web.find_element_by_xpath('//*[@id="2002256425"]/tbody/tr[8]/td[5]/input')
RadioButtonPeriod.click() #6
RadioButtonPeriod = web.find_element_by_xpath('//*[@id="2002256425"]/tbody/tr[9]/td[5]/input')
RadioButtonPeriod.click() #7
RadioButtonPeriod = web.find_element_by_xpath('//*[@id="2002256425"]/tbody/tr[10]/td[5]/input')
RadioButtonPeriod.click() #8
RadioButtonPeriod = web.find_element_by_xpath('//*[@id="2002256425"]/tbody/tr[11]/td[5]/input')
RadioButtonPeriod.click() #9
RadioButtonPeriod = web.find_element_by_xpath('//*[@id="2002256425"]/tbody/tr[12]/td[5]/input')
RadioButtonPeriod.click() #10
RadioButtonPeriod = web.find_element_by_xpath('//*[@id="2002256425"]/tbody/tr[13]/td[5]/input')
RadioButtonPeriod.click() #11
RadioButtonPeriod = web.find_element_by_xpath('//*[@id="2002256425"]/tbody/tr[14]/td[5]/input')
RadioButtonPeriod.click() #12
RadioButtonPeriod = web.find_element_by_xpath('//*[@id="2002256425"]/tbody/tr[15]/td[5]/input')
RadioButtonPeriod.click() #13
RadioButtonPeriod = web.find_element_by_xpath('//*[@id="2002256425"]/tbody/tr[16]/td[5]/input')
RadioButtonPeriod.click() #14
RadioButtonPeriod = web.find_element_by_xpath('//*[@id="2002256425"]/tbody/tr[17]/td[5]/input')
RadioButtonPeriod.click() #15
RadioButtonPeriod = web.find_element_by_xpath('//*[@id="2002256425"]/tbody/tr[18]/td[5]/input')
RadioButtonPeriod.click() #16
RadioButtonPeriod = web.find_element_by_xpath('//*[@id="2002256425"]/tbody/tr[19]/td[5]/input')
RadioButtonPeriod.click() #17
RadioButtonPeriod = web.find_element_by_xpath('//*[@id="2002256425"]/tbody/tr[20]/td[5]/input')
RadioButtonPeriod.click() #18
RadioButtonPeriod = web.find_element_by_xpath('//*[@id="2002256425"]/tbody/tr[21]/td[5]/input')
RadioButtonPeriod.click() #19
RadioButtonPeriod = web.find_element_by_xpath('//*[@id="2002256425"]/tbody/tr[22]/td[5]/input')
RadioButtonPeriod.click() #20
RadioButtonPeriod = web.find_element_by_xpath('//*[@id="2002256425"]/tbody/tr[23]/td[5]/input')
RadioButtonPeriod.click() #21

Comment = "The lecturing is good enough"
com = web.find_element_by_xpath('//*[@id="comment"]')
com.send_keys(Comment)

web.find_element_by_xpath('//*[@id="2002256425"]/button').click()