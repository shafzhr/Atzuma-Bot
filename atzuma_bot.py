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


# proxyString = "118.174.211.220:11"
# desired_capability = webdriver.DesiredCapabilities.FIREFOX
# desired_capability['proxy'] = {
#     "proxyType": "manual",
#     "httpProxy": proxyString,
#     "ftpProxy": proxyString,
#     "sslProxy": proxyString
# }
# browser = webdriver.Firefox(capabilities=desired_capability)
browser = webdriver.Firefox()

fake = Faker()
amount_of_signs = 9999999
for _ in range(amount_of_signs):
    name = fake.name()
    email = fake.free_email()
    browser.get("https://www.atzuma.co.il/skillz")

    try:
        name_path = '//*[@id="187bb954b1e32240d02a385304bf64f3ba4dc8b6"]'
        print("waiting for name")
        wait_for_element(browser, By.XPATH, name_path)
        print("found name")
        name_field = browser.find_element_by_xpath(name_path)
        name_field.send_keys(name)

        email_path = '//*[@id="42d90866a91cbdf64121b3316eb470a2172d7773"]'
        print("waiting for email")
        wait_for_element(browser, By.XPATH, email_path)
        print("found email")
        email_field = browser.find_element_by_xpath(email_path)
        email_field.send_keys(email)

        submit_path = '//*[@id="submitbuttoncontainer"]/input'
        print("waiting for submit")
        wait_for_element(browser, By.XPATH, submit_path)
        print("found submit")
        submit_field = browser.find_element_by_xpath(submit_path)
        submit_field.click()
    except Exception as e:
        print('------ERR------')
        print(e)
        print('------ERR------')


browser.quit()
