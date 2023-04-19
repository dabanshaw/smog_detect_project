from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time


class Bug(object):
    def __init__(self):
        
        self.path = "C:/Users/USER/Desktop/AI/chromedriver.exe"

        self.options = Options()
        self.prefs = {"download.default_directory": self.path}
        self.options.add_experimental_option("prefs", self.prefs)

        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
    
    def start(self):
        self.browser.get("https://motor.epa.gov.tw/query/Query_Check.aspx")
        time.sleep(1)
        self.search_1 = self.browser.find_element(By.NAME, "ctl00$MainContent$txtCarNo")
        self.search_1.click()
        self.search_1.send_keys("L2U-296")
        time.sleep(1)

        self.search_2 = self.browser.find_element(By.NAME, "ctl00$MainContent$btnQuery")
        self.search_2.click()
        time.sleep(1)
        self.search_3 = self.browser.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div[3]/div[1]/table/tbody/tr[2]")

        self.search_3 = self.search_3.text
        # search_3 = search_3["檢驗別"]
        self.search_3 = self.search_3.split(" ")
        print(self.search_3)
        self.vehicle = {"車牌號碼":self.search_3[0],
                        # "是否檢測":self.search_3[1],
                        "檢測結果":self.search_3[2],
                        "HC":self.search_3[3],
                        "CO":self.search_3[4],
                        "CC":self.search_3[5],
                        "型程別":self.search_3[6],
                        "檢測日期":self.search_3[7]}
        time.sleep(1)
        self.browser.close()

    def open_web(self):
        self.browser.get("https://polcar.epa.gov.tw/case/Step1.aspx")

        time.sleep(1)
        search_1 = self.browser.find_element(By.XPATH, "/html/body/form/div[3]/main/div/div/article[1]/div/a[1]/img")
        search_1.click()

        time.sleep(1)
        search_2 = self.browser.find_element(By.XPATH, "/html/body/form/div[3]/main/div/div/article/center/table/tbody/tr[1]/td/label")
        search_2.click()

        time.sleep(1)
        search_3 = self.browser.find_element(By.XPATH, "/html/body/form/div[3]/main/div/div/article/p[28]/input")
        search_3.click()

        while True:
            pass

    
        # for i in self.vehicle:
        #     print(self.vehicle[i])

# test = Bug()
# test.start()