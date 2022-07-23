from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep


class InstagramFollowerBot:
    def __init__(self, driver_path):
        ser = Service(driver_path)
        op = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ser, options=op)
        self.driver.implicitly_wait(30)
        self.instagram_link = "https://www.instagram.com/"

    def login(self, instagram_account, instagram_password):

        self.driver.get(f'{self.instagram_link}accounts/login/')
        sign_in = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        sign_in.send_keys(f'{instagram_account}{Keys.TAB}{instagram_password}{Keys.ENTER}')
        sleep(1)

        popup = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/button')
        popup.click()
        sleep(1)

        popup = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]')
        popup.click()
        sleep(1)

    def find_followers(self, similar_account_name: str):

        sleep(5)
        self.driver.get(f"{self.instagram_link}{similar_account_name}/")

        sleep(2)
        see_followers = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a')
        see_followers.click()
        try:
            scroll = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]')
            for i in range(10):
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
                sleep(2)
        except ElementClickInterceptedException:
            pass


    def follow(self):
        all_follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        print(len(all_follow_buttons))
        keep_following = True
        for button in all_follow_buttons:
            if button.text == "Follow" and keep_following:
                try:
                    button.click()
                    sleep(1)
                except ElementClickInterceptedException:
                    try_again_later = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/button[2]')
                    try_again_later.click()
                    keep_following = False
                    sleep(2)
