import config
from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.keys import Keys


class Cowin:

    def __init__(self):

        options = webdriver.ChromeOptions()
        options.binary_location = r"C:\\Program Files\\Google\\Chrome\Application\\chrome.exe"
        chrome_driver_binary = r"./chromedriver.exe"
        self.driver = webdriver.Chrome(
            chrome_driver_binary, options=options)

    def logIn(self, config):

        self.driver.get("https://selfregistration.cowin.gov.in/")

        time.sleep(2)
        phoneNumber = self.driver.find_element_by_xpath(
            "/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[1]/ion-grid/form/ion-row/ion-col[2]/ion-item/mat-form-field/div/div[1]/div/input"
        )

        getOTP = self.driver.find_element_by_xpath(
            "/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[1]/ion-grid/form/ion-row/ion-col[2]/div/ion-button"
        )
        phoneNumber.send_keys(config["phoneNumber"])
        time.sleep(1)
        getOTP.click()

        time.sleep(2)

        try:
            self.driver.find_element_by_xpath(
                "/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[1]/ion-grid/form/ion-row/ion-col[2]/ion-item[2]/p"
            )
            print("Wrong phone number- restart the application")
            exit(0)
        except Exception:
            print("Enter the OTP Here")
        time.sleep(2)

        otp = input()

        inputOTP = self.driver.find_element_by_xpath(
            "/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col/ion-grid/form/ion-row/ion-col[2]/ion-item/mat-form-field/div/div[1]/div/input"
        ).send_keys(otp)

        verifyOTP = self.driver.find_element_by_xpath(
            "/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col/ion-grid/form/ion-row/ion-col[3]/div/ion-button"
        ).click()

        time.sleep(2)

        idProof = self.driver.find_element_by_xpath(
            "/html/body/app-root/ion-app/ion-router-outlet/app-registration-form/ion-content/div/ion-grid/ion-row/ion-col[2]/ion-grid/ion-row/ion-col[2]/form/ion-grid[1]/ion-row/ion-col[1]/ion-item/mat-form-field/div/div[1]/div/mat-select/div/div[2]/div").click()
        aadhar = self.driver.find_element_by_xpath(
            "/html/body/div[2]/div[2]/div/div/div/mat-option[1]/span").click()
        aadharNumber = self.driver.find_element_by_xpath(
            "/html/body/app-root/ion-app/ion-router-outlet/app-registration-form/ion-content/div/ion-grid/ion-row/ion-col[2]/ion-grid/ion-row/ion-col[2]/form/ion-grid[1]/ion-row/ion-col[2]/ion-item/mat-form-field/div/div[1]/div/input").send_keys(config["AADHARNumber"])
        name = self.driver.find_element_by_xpath(
            "/html/body/app-root/ion-app/ion-router-outlet/app-registration-form/ion-content/div/ion-grid/ion-row/ion-col[2]/ion-grid/ion-row/ion-col[2]/form/ion-grid[1]/ion-row/ion-col[3]/ion-item/mat-form-field/div/div[1]/div/input").send_keys(config["name"])
        if config["gender"] == "male":
            gender = self.driver.find_element_by_xpath(
                "/html/body/app-root/ion-app/ion-router-outlet/app-registration-form/ion-content/div/ion-grid/ion-row/ion-col[2]/ion-grid/ion-row/ion-col[2]/form/ion-grid[1]/ion-row/ion-col[4]/ion-item/div/mat-radio-group/mat-radio-button[1]/label/div[1]/div[1]").click()
        elif config["gender"] == "female":
            gender = self.driver.find_element_by_xpath(
                "/html/body/app-root/ion-app/ion-router-outlet/app-registration-form/ion-content/div/ion-grid/ion-row/ion-col[2]/ion-grid/ion-row/ion-col[2]/form/ion-grid[1]/ion-row/ion-col[4]/ion-item/div/mat-radio-group/mat-radio-button[2]/label/div[1]/div[1]").click()
        else:
            gender = self.driver.find_element_by_xpath(
                "/html/body/app-root/ion-app/ion-router-outlet/app-registration-form/ion-content/div/ion-grid/ion-row/ion-col[2]/ion-grid/ion-row/ion-col[2]/form/ion-grid[1]/ion-row/ion-col[4]/ion-item/div/mat-radio-group/mat-radio-button[3]/label/div[1]/div[1]").click()
        yearOfBirth = self.driver.find_element_by_xpath(
            "/html/body/app-root/ion-app/ion-router-outlet/app-registration-form/ion-content/div/ion-grid/ion-row/ion-col[2]/ion-grid/ion-row/ion-col[2]/form/ion-grid[1]/ion-row/ion-col[5]/ion-item/mat-form-field/div/div[1]/div/input").send_keys(config["yearOfBirth"])
        register = self.driver.find_element_by_xpath(
            "/html/body/app-root/ion-app/ion-router-outlet/app-registration-form/ion-content/div/ion-grid/ion-row/ion-col[2]/ion-grid/ion-row/ion-col[2]/form/ion-grid[2]/ion-row[1]/ion-col/div/ion-button").click()


bot = Cowin()
bot.logIn(config._config)
exit(0)
