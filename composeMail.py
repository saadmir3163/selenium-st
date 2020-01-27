from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By

EMAILFIELD = (By.ID, "i0116")
PASSWORDFIELD = (By.ID, "i0118")
NEXTBUTTON = (By.ID, "idSIButton9")
mainSinin = (By.XPATH, "/html/body/header/div/aside/div/nav/ul/li[2]/a")
compose = (By.ID, "id__3")
recepient = (By.XPATH, "//*/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/div/div/div/div[1]/div/div/input")
subject = (By.ID, "subjectLine0")
message = (By.XPATH, "//*/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div[1]/div/div/div/div[1]/div[2]/div[1]")


browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://outlook.live.com/owa/')


# browser.find_element_by_xpath("/html/body/header/div/aside/div/nav/ul/li[2]/a").click()
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(mainSinin)).click()
# wait for email field and enter email
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(EMAILFIELD)).send_keys("stproject2020@outlook.com")

# Click Next
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()

# wait for password field and enter password
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(PASSWORDFIELD)).send_keys("Saad3163")

# Click Login - same id?
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()


WebDriverWait(browser, 10).until(EC.element_to_be_clickable(compose)).click()


WebDriverWait(browser, 10).until(EC.element_to_be_clickable(recepient)).send_keys("ghostrocker40@gmail.com")


WebDriverWait(browser, 10).until(EC.element_to_be_clickable(subject)).send_keys("ST Project Testing")


WebDriverWait(browser, 10).until(EC.element_to_be_clickable(message)).send_keys("My Name i Saad Mir this is my first project of ST")



browser.close()