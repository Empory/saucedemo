from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get("https://saucedemo.com")
driver.maximize_window()
button = driver.find_element(By.ID, "login-button")


class Test_Sauce:

    def test_empty_login(self):
        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        username.send_keys("")
        password.send_keys("")
        button.click()

    def test_empty_password(self):
        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        username.send_keys("standard_user")
        password.send_keys("")
        button.click()

    def test_invalid_login(self):
        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        username.clear()
        password.clear()
        username.send_keys("locked_out_user")
        password.send_keys("secret_sauce")
        button.click()

    def test_error_message(self):
        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        error = driver.find_element(
            By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3/button")
        username.clear()
        password.clear()
        username.send_keys("")
        password.send_keys("")
        button.click()

        error.click()

    def test_valid_login(self):
        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        course = driver.find_elements(By.CLASS_NAME, "inventory_item")
        username.clear()
        password.clear()
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        button.click()
        print(len(course))


testClass = Test_Sauce()
# testClass.test_empty_login()
# sleep(5)
# testClass.test_empty_password()
# sleep(5)
# testClass.test_invalid_login()
# sleep(5)
# testClass.test_error_message()
# sleep(5)
testClass.test_valid_login()
while True:
    continue
