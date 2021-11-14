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

count=0
driver.find_element_by_id("Fibonacci").click()
driver.find_element_by_id("button1").click()
driver.find_element_by_id("number").send_keys("4")
driver.find_element_by_id("button1").click()
if driver.find_element_by_id("r1").text == '[0, 1, 1, 2]':
    count +=1
else:
    print('error')


driver.find_element_by_id("Factorial").click()
driver.find_element_by_id("button1").click()
driver.find_element_by_id("number").send_keys("4")
driver.find_element_by_id("button1").click()
if driver.find_element_by_id("r1").text == '24':
    count +=1
else:
    print('error')


driver.find_element_by_id("APtriangulo").click()
driver.find_element_by_id("button1").click()
driver.find_element_by_id("lado1").send_keys("4")
driver.find_element_by_id("lado2").send_keys("4")
driver.find_element_by_id("lado3").send_keys("4")
driver.find_element_by_id("button1").click()
if driver.find_element_by_id("r1").text == 'Área= 6.928203230275509' and driver.find_element_by_id("r2").text == 'Perimetro= 12.0':
    count +=1
else:
    print('error')


driver.find_element_by_id("APrectangulo").click()
driver.find_element_by_id("button1").click()
driver.find_element_by_id("ladoa").send_keys("4")
driver.find_element_by_id("ladob").send_keys("6")
driver.find_element_by_id("button1").click()
if driver.find_element_by_id("r1").text == 'Área= 24.0' and driver.find_element_by_id("r2").text == 'Perimetro= 20.0':
    count +=1
else:
    print('error')


driver.find_element_by_id("APcirculo").click()
driver.find_element_by_id("button1").click()
driver.find_element_by_id("radio").send_keys("4")
driver.find_element_by_id("button1").click()
if driver.find_element_by_id("r1").text == 'Área= 50.26548245743669' and driver.find_element_by_id("r2").text == 'Perimetro= 25.132741228718345':
    count +=1
else:
    print('error')

if count == 5:
    print("5 pass")
else:
    print('error')


