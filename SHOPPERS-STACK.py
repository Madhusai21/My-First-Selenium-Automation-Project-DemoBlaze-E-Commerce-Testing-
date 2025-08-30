from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get('https://www.demoblaze.com/index.html')
driver.maximize_window()
sleep(1)
# step-1
driver.find_element("id","signin2").click()
sleep(1)
# step-2
driver.find_element("id","sign-username").send_keys("Madhusai")
sleep(1)
# step-3
driver.find_element("id","sign-password").send_keys("Madhu@21")
sleep(1)
# step 4 click sign up ----
driver.find_element("xpath","//button[text()='Sign up']").click()
sleep(1)
n=driver.switch_to.alert
n.accept()
sleep(1)
# step 5 close page ----
driver.find_element("xpath","/html/body/div[2]/div/div/div[3]/button[1]").click()
sleep(1)
#step login page
driver.find_element("id","login2").click()
sleep(1)
# # step 7 username---
driver.find_element("id","loginusername").send_keys("Madhusai")
sleep(1)
# # step 8 password
driver.find_element("id","loginpassword").send_keys("Madhu@21")
sleep(1)
# # step 9 login btn
driver.find_element("xpath","//button[text()='Log in']").click()
sleep(1)
#step 10 select the products
driver.find_element("link text","Monitors").click()
sleep(1)
#step 11
driver.find_element("link text","Laptops").click()
sleep(1)
# step 12
driver.find_element("link text","Sony vaio i7").click()
sleep(1)
# step 13
driver.find_element("link text","Add to cart").click()
sleep(1)
n=driver.switch_to.alert
n.accept()
sleep(1)
#step 14
driver.find_element("id","cartur").click()
sleep(1)
#step 15
driver.find_element("xpath","/html/body/div[6]/div/div[2]/button").click()
sleep(1)
# step 16
driver.find_element("id","name").send_keys("madhusai")
sleep(1)
driver.find_element("id","country").send_keys("India")
sleep(1)
driver.find_element("id","city").send_keys("Kurnool")
sleep(1)
driver.find_element("id","card").send_keys("98765432345678")
sleep(1)
driver.find_element("id","month").send_keys("12")
sleep(1)
driver.find_element("id","year").send_keys("2025")
sleep(1)
driver.find_element("xpath","//*[@id='orderModal']/div/div/div[3]/button[2]").click()
sleep(1)
# step `17
driver.find_element("xpath","/html/body/div[10]/div[7]/div/button").click()
sleep(2)
driver.quit()