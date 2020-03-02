from selenium import webdriver
import time
import numpy as np
import os

loc = os.path.abspath(os.getcwd()) + "\\chromedriver.exe"

full_name = '//*[@id="649649255120112"]'
user_name = '//*[@id="1464214030500550"]'
e_mail = '//*[@id="328991337275965"]'
m_no = '//*[@id="602863763172693"]'
rsn = '//*[@id="709786765737601"]'
submit = '//*[@id="u_0_7"]'
n = 0
n = int(input("Enter the Number of time you want to Fill Form : "))
if(n == 0):
    n = 2

for i in range(n):
    try:
        driver = webdriver.Chrome(loc)
        driver.get('https://help.instagram.com/contact/606967319425038/?ref=cr')
        driver.find_element_by_xpath(full_name).click()
        driver.find_element_by_xpath(full_name).send_keys("xxxxx")
        driver.find_element_by_xpath(user_name).click()
        driver.find_element_by_xpath(user_name).send_keys("_dirtysociety_")
        driver.find_element_by_xpath(e_mail).click()
        driver.find_element_by_xpath(e_mail).send_keys("xxxxx@gmail.com")
        driver.find_element_by_xpath(m_no).click()
        driver.find_element_by_xpath(m_no).send_keys("xxxxxxxxxx")
        driver.find_element_by_xpath(rsn).click()
        driver.find_element_by_xpath(rsn).send_keys("I have not violated any of your community guidelines. It seems that you have disabled my account by mistake. Please reactivate it as soon as possible. Thanks")
        driver.find_element_by_xpath(submit).click()
        time.sleep(np.random.randint(30,60))
        print("Successfull : ",i+1)
        driver.quit()
    except :
        print("ERROR : ",i+1)
        time.sleep(2)
