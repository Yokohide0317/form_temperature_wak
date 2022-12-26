# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.support.select import Select
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import argparse
import io
import sys
import pyotp

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class sel_main:
    def __init__(self, wait_time):
        self.url = ""
        self.email = ""
        self.password = ""
        self.key = ""
        self.webdriver = ""
        self.wait = int(wait_time)
        print("Login as : ", self.email)

    # https://tanuhack.com/selenium-2step-authentication/
    # 二段階認証突破
    def get_two_facta(self):
        self.two_auth_pass = pyotp.TOTP(self.key).now()

    def login_365(self, driver):
        # Input email
        element = driver.find_element(By.ID, "i0116")
        element.send_keys(self.email)
        time.sleep(self.wait)
        # click "Next"
        element = driver.find_element(By.ID, "idSIButton9")
        element.click()
        time.sleep(self.wait)

        # Input Password
        element = driver.find_element(By.ID, "i0118")
        element.send_keys(self.password)
        time.sleep(self.wait)

        # click "Next"
        element = driver.find_element(By.ID, "idSIButton9")
        element.click()
        time.sleep(self.wait)

        # 2Facta認証
        # click "mobile auth"
        element = driver.find_element(By.CLASS_NAME, "table")
        element.click()
        time.sleep(self.wait)

        # Get and Enter 2facta
        self.get_two_facta()
        element = driver.find_element(By.XPATH, '//*[@id="idTxtBx_SAOTCC_OTC"]')
        element.send_keys(self.two_auth_pass)
        time.sleep(self.wait*2)

        # Click Enter
        element = driver.find_element(By.XPATH, '//*[@id="idSubmit_SAOTCC_Continue"]')
        element.click()
        time.sleep(self.wait+2)

        # Stay signin -> No
        element = driver.find_element(By.ID, "idBtn_Back")
        element.click()
        time.sleep(self.wait+2)

        # ラジオボタン選択
        x_path = '' # いいえ
        element = driver.find_element(By.XPATH, x_path)
        element.click()
        time.sleep(self.wait+2)

        # Submit
        x_path = ''
        element = driver.find_element(By.XPATH, x_path)
        element.click()
        time.sleep(self.wait+2)

        time.sleep(int(self.wait*2))


    def open_url(self):
        #Chromeを操作
        driver = webdriver.Chrome(executable_path=self.webdriver)
        driver.implicitly_wait(2)

        driver.get(self.url)
        driver.implicitly_wait(2)

        time.sleep(int(self.wait*3))
        cur_url = driver.current_url
        if cur_url != self.url:
            print("認証画面に移行しました. ２段階認証も行います.")
            self.login_365(driver)

        print("アクセス完了")

        driver.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='自動で健康行動観察表を提出。')
    parser.add_argument("-w", "--wait", default=3)
    args = parser.parse_args()

    sel = sel_main(args.wait)
    sel.open_url(args.debug)
