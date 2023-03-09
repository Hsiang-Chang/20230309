import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def traversalCathayBk(chromedriverPath):
    mobile_emulation = {"deviceName":"iPhone 6"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(chromedriverPath, options=chrome_options)
    wait = WebDriverWait(driver, 5)

    driver.get("https://www.cathaybk.com.tw/cathaybk/")

    # 1. 官網截圖
    btn_burger = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='cubre-o-header__burger']")))
    wait.until(EC.presence_of_element_located((By.XPATH, "//img[@id='img_C8CE0EE57DB4429DAF30C4BCFBF2FC55']")))
    wait.until(EC.presence_of_element_located((By.XPATH, "//img[@id='img_A8E203801FAD46BB9993F7B288AECA36']")))
    wait.until(EC.presence_of_element_located((By.XPATH, "//img[@id='img_7C10E02A29584E5CBB55DD1F9F3AE8EE']")))
    wait.until(EC.presence_of_element_located((By.XPATH, "//img[@id='img_7034E5DB7C3B4EFDBD5AF85FB10F3D86']")))
    wait.until(EC.presence_of_element_located((By.XPATH, "//img[@id='img_2F82C59BCEC94363A58A881439BF622E']")))
    wait.until(EC.presence_of_element_located((By.XPATH, "//img[@id='img_AA3E3041292345D2BDCFE545A7BF4F14']")))
    
    driver.save_screenshot("webpage.png")

    # 2. 計算信用卡項目並截圖
    btn_burger.click()

    btn_product_intro = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), '產品介紹')]")))
    btn_product_intro.click()

    btn_credit = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), '信用卡')]")))
    btn_credit.click()

    elements = driver.find_elements(By.XPATH, "//div[contains(text(), '信用卡')]/../a")

    print("共計信用卡項目數量: "+ str(len(elements)))

    time.sleep(2)
    driver.save_screenshot("credict_card_list.png")

    # 3. 停發卡
    btn_card_intro = driver.find_element(By.XPATH, "//a[contains(text(), '卡片介紹')]")
    btn_card_intro.click()

    element_card_no_longer = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), '停發卡')]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", element_card_no_longer)

    attr_name = driver.find_element(By.XPATH, "//a/p[contains(text(), '停發卡')]/parent::a").get_attribute("data-anchor-btn")
    btn_slides = driver.find_elements(By.XPATH, "//section[contains(@data-anchor-block, '" + attr_name + "')]//span[@role='button']")

    for idx, btn_slide in enumerate(btn_slides):
        btn_slide.click()
        time.sleep(1)
        driver.save_screenshot(str(idx)+".png")

    print("共計停發信用卡數量: "+str(len(btn_slides)))

    driver.close()

if __name__ == '__main__':
    traversalCathayBk(sys.argv[1])