from selenium import webdriver

driver = webdriver.Edge("C:\\Users\\jeiis\\Downloads\\edgedriver_win64\\msedgedriver.exe")

driver.get('https://webappjg.herokuapp.com/')

driver.find_element_by_id("b1").click()
driver.find_element_by_id("home").click()
driver.find_element_by_id("b2").click()
driver.find_element_by_id("home").click()
driver.find_element_by_id("b3").click()
driver.find_element_by_id("home").click()
driver.find_element_by_id("b4").click()
driver.find_element_by_id("home").click()
driver.find_element_by_id("b5").click()
driver.find_element_by_id("home").click()
driver.find_element_by_id("Fibonacci").click()

driver.find_element_by_id("Factorial").click()
driver.find_element_by_id("APtriangulo").click()
driver.find_element_by_id("APrectangulo").click()
driver.find_element_by_id("APcirculo").click()





