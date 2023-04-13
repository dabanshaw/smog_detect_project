from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

path = "C:/Users/USER/Desktop/AI/chromedriver.exe"

options = Options()
prefs = {"download.default_directory": path}
options.add_experimental_option("prefs", prefs)

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
browser.get("https://polcar.epa.gov.tw/case/Step1.aspx")

time.sleep(1)
search_1 = browser.find_element(By.XPATH, "/html/body/form/div[3]/main/div/div/article[1]/div/a[1]/img")
search_1.click()

time.sleep(1)
search_2 = browser.find_element(By.XPATH, "/html/body/form/div[3]/main/div/div/article/center/table/tbody/tr[1]/td/label")
search_2.click()

time.sleep(1)
search_3 = browser.find_element(By.XPATH, "/html/body/form/div[3]/main/div/div/article/p[28]/input")
search_3.click()


time.sleep(2)

