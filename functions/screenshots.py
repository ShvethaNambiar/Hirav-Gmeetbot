import pyautogui
import json
import requests
from selenium.webdriver.common.keys import Keys

def ss(driver):
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'C:\Users\Shvetha M Nambiar\Desktop\Hack\gmeetpluging\screenshots\ss.png')
    driver.implicitly_wait(10)
    headers = {"Authorization": "Bearer ya29.a0AfH6SMAdW39Hw4WvTEC0pAtqh1-G5QhQmNiNb9Gr1R0dGOMK54bMteYLk3PwhUdNj6fZdZIzPfQsHv4U2Bmv-dE8lXdsgRY1yjnfS3gapMHVXclg903nUXMsUKda2mDJ_qTyitbQrN0ZMROL0K1DPtiFZvRd"}
    para = {
        "name": "Screenshot1",
        "parents": ["1UyuAZq5TE1NXDMW7MziJJnYSlFBZsqaI"]
    }
    files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
        'file': open(r"C:\Users\Shvetha M Nambiar\Desktop\Hack\gmeetpluging\screenshots\ss.png", "rb")
    }
    r = requests.post(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
        headers=headers,
        files=files
    )
    driver.implicitly_wait(10)
    # driver.find_element_by_xpath('// *[ @ id = "ow3"] / div[1] / div / div[9] / div[3] / div[1] / div[3] / div / div[2] / div[3] / span / span').click()
    driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[4]/div[1]/div[1]/div[2]/textarea').send_keys('https://drive.google.com/drive/folders/1P-oB0rGq9UC-i_G_oCcGlJPa682LYjJD?usp=sharing')
    driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[4]/div[1]/div[1]/div[2]/textarea').send_keys(Keys.ENTER)
