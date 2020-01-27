from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By

EMAILFIELD = (By.ID, "i0116")
PASSWORDFIELD = (By.ID, "i0118")
NEXTBUTTON = (By.ID, "idSIButton9")
mainSinin = (By.XPATH, "/html/body/header/div/aside/div/nav/ul/li[2]/a")
logout = (By.XPATH, "/html/body/div[2]/div/div[1]/div/div[1]/div[3]/div[1]/button")
loggingout2 = (By.ID, "meControlSignoutLink")

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://outlook.live.com/owa/')


# browser.find_element_by_xpath("/html/body/header/div/aside/div/nav/ul/li[2]/a").click()
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(mainSinin)).click()
# wait for email field and enter email
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(EMAILFIELD)).send_keys("stproject2020@outlook.co")

# Click Next
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()

# wait for password field and enter password
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(PASSWORDFIELD)).send_keys("Saad3163")

# Click Login - same id?
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()


WebDriverWait(browser, 10).until(EC.element_to_be_clickable(logout)).click()

WebDriverWait(browser, 10).until(EC.element_to_be_clickable(loggingout2)).click()