from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(executable_path="/Users/ronaldharris/PycharmProjects/browser_automation/drivers/chromedriver")
browser.get("https://techstepacademy.com/trial-of-the-stones")
stone_input = browser.find_element(By.ID, 'r1Input')
stone_answer = browser.find_element(By.ID, 'r1Btn')
stone_result = browser.find_element(By.ID, "passwordBanner")

riddle_input = browser.find_element(By.ID, 'r2Input')
riddle_answer = browser.find_element(By.ID, 'r2Butn')
riddle_result = browser.find_element(By.ID, "successBanner1").text

richest_merchant_name = browser.find_element(By.XPATH, "//p[text()='3000'] /.. /span")

merchant_input = browser.find_element(By.ID, "r3Input")
merchant_answer = browser.find_element(By.ID, "r3Butn")

check_answer = browser.find_element(By.NAME, "checkButn")

complete_message = browser.find_element(By.ID, "trialCompleteBanner")

stone_input.send_keys('rock')
stone_answer.click()
password = stone_result.text

riddle_input.send_keys(password)
riddle_answer.click()

merchant_input.send_keys(richest_merchant_name.text)
merchant_answer.click()

check_answer.click()

assert complete_message.text == 'Trial Complete'

browser.quit()