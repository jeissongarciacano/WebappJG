from selenium import webdriver

driver = webdriver.Edge("C:\\Users\\jeiis\\Downloads\\edgedriver_win64\\msedgedriver.exe")

driver.get('https://webappjg.herokuapp.com/')

driver.find_element_by_id("b1").click()



