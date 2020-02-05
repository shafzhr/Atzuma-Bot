import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from faker import Faker


def is_element_present(driver, by, value):
    try:
        driver.find_element(by, value)
        return True
    except NoSuchElementException:
        return False


def wait_for_element(driver, by, element):
    while not is_element_present(driver, by, element):
        pass


proxyString = "118.174.211.220:11"
desired_capability = webdriver.DesiredCapabilities.FIREFOX
desired_capability['proxy'] = {
    "proxyType": "manual",
    "httpProxy": proxyString,
    "ftpProxy": proxyString,
    "sslProxy": proxyString
}
browser = webdriver.Firefox(capabilities=desired_capability)

fake = Faker()
amount_of_signs = 5
for _ in range(amount_of_signs):
    name = fake.name()
    email = fake.free_email()
    browser.get("https://www.atzuma.co.il/skillz")

    name_path = '/html/body/div[5]/div[3]/div[4]/div[1]/form/fieldset/div[1]/input'
    wait_for_element(browser, By.XPATH, name_path)
    name_field = browser.find_element_by_xpath(name_path)
    name_field.send_keys(name)

    email_path = '/html/body/div[5]/div[3]/div[4]/div[1]/form/fieldset/div[2]/input'
    wait_for_element(browser, By.XPATH, email_path)
    email_field = browser.find_element_by_xpath(email_path)
    email_field.send_keys(email)

    submit_path = '/html/body/div[5]/div[3]/div[4]/div[1]/form/fieldset/div[6]/input'
    wait_for_element(browser, By.XPATH, submit_path)
    submit_field = browser.find_element_by_xpath(submit_path)
    submit_field.click()

input()
browser.quit()
