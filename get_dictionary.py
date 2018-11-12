from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.talkenglish.com/vocabulary/top-1000-verbs.aspx")

f = open("words.txt", "a")

for i in range(1, 1011):
    xpath = '//*[@id="GridView3"]/tbody/tr[' + str(i) + ']/td[2]/a'
    xpath2 = '//*[@id="GridView3"]/tbody/tr[' + str(i) + ']/td[2]'

    try:
        word = driver.find_element_by_xpath(xpath).get_attribute('innerHTML')
        f.write(word + '\n')
        print(word)
    except:
        word = driver.find_element_by_xpath(xpath2).get_attribute('innerHTML')
        f.write(word + '\n')
        print(word)

f.close()
driver.close()