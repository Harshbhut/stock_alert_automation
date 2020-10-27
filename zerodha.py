from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import time
from chartink import get_data

final_data_lists = get_data()
print("All " + str(len(final_data_lists)) + " Stocks Retrived Succesfully...\n")

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
# chromedriver_location = "C:/Users/hasui/Desktop/automate_alert/chromedriver.exe" 
driver = webdriver.Chrome(options=options, executable_path =r'C:/Users/hasui/Desktop/automate_alert/chromedriver.exe')
driver.get("https://kite.zerodha.com/connect/login?api_key=sentinel")
#driver.set_window_size(1920, 1080)  

# TODO Before Login Strings.....

login = "/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[1]/input"
password = "/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[2]/input"
submit = "/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[4]/button"
pin = "/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[2]/div/input"
continuee ="/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[3]/button"

# TODO After Login Strings.....

last_trade = "/html/body/main/div[1]/section/div/div[1]/div/div[1]/div[1]/select"
symbol = "/html/body/main/div[1]/section/div/div[1]/div/div[1]/div[2]/div/div/input"
less_than = "/html/body/main/div[1]/section/div/div[1]/div/div[2]/div[1]/select"
price = "/html/body/main/div[1]/section/div/div[1]/div/div[2]/div[3]/div/input"
trigger_name = "/html/body/main/div[1]/section/div/div[1]/div/div[4]/div/div/div[1]/div/input"
create = "/html/body/main/div[1]/section/div/div[1]/div/div[5]/p/button"


def login_success():
    try:
        wait = WebDriverWait(driver, 10)
        menu = wait.until(ec.visibility_of_element_located((By.XPATH, login)))
        ActionChains(driver).move_to_element(menu).perform()

        driver.find_element_by_xpath(login).click()
        driver.find_element_by_xpath(login).send_keys("UR4102")

        driver.find_element_by_xpath(password).click()
        driver.find_element_by_xpath(password).send_keys("Hasu@291682")
        driver.find_element_by_xpath(submit).click()

        wait = WebDriverWait(driver, 10)
        menu = wait.until(ec.visibility_of_element_located((By.XPATH, pin)))
        ActionChains(driver).move_to_element(menu).perform()

        driver.find_element_by_xpath(pin).click()
        driver.find_element_by_xpath(pin).send_keys("291682")

        driver.find_element_by_xpath(continuee).click()
        
    except:
        print("Login UnSuccessfull...Please Try Again...")  
        
print("Login Succesfull...\n")  
      
def master_data():
      
    for item in final_data_lists:
        
        wait = WebDriverWait(driver, 10)
        menu = wait.until(ec.visibility_of_element_located((By.XPATH, last_trade)))
        ActionChains(driver).move_to_element(menu).perform()
        driver.find_element_by_xpath(last_trade).click()
        driver.find_element_by_xpath(last_trade).send_keys("Last Traded Price")
    
        driver.find_element_by_xpath(symbol).click()
        driver.find_element_by_xpath(symbol).send_keys(Keys.CONTROL + "a")
        driver.find_element_by_xpath(symbol).send_keys(Keys.DELETE)
        driver.find_element_by_xpath(symbol).send_keys("NSE:" + item[0])
        selection = "/html/body/main/div[1]/section/div/div[1]/div/div[1]/div[2]/div[2]/ul/li[1]/div"
        driver.find_element_by_xpath(selection).click()


        driver.find_element_by_xpath(less_than).click()
        driver.find_element_by_xpath(less_than).send_keys("Less Than Equal To (<=)")


        elem1 = driver.find_element_by_xpath(price)
        elem1.click()
        wait = WebDriverWait(driver, 10)
        menu = wait.until(ec.visibility_of_element_located((By.XPATH,price)))
        ActionChains(driver).move_to_element(menu).perform()
        driver.execute_script("arguments[0].value = ''", elem1)
        elem1.send_keys(item[2])

        driver.find_element_by_xpath(trigger_name).click()
        driver.find_element_by_xpath(trigger_name).send_keys(Keys.CONTROL + "a")
        driver.find_element_by_xpath(trigger_name).send_keys(Keys.DELETE)
        driver.find_element_by_xpath(trigger_name).send_keys("Buy " + item[0] + " @ " + item[1])


        driver.find_element_by_xpath(create).click()
        print(item[0] + " Alert Created...\n")
        time.sleep(1)
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(2)


login_success()
master_data()

    



