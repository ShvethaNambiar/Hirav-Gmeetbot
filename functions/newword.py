import random
from selenium.webdriver.common.keys import Keys

def newWord(driver):
    words = ["sesquipedalian - having many syllables or using long words", "hobbit - a member of a fictitious peaceful and genial race of small humanlike creatures that dwell underground", "quash - to nullify especially by judicial action", "jurisprudent - the science of law or a system of law", "inimitable - not capable of being imitated"]
    # driver.find_element_by_xpath('// *[ @ id = "ow3"] / div[1] / div / div[9] / div[3] / div[1] / div[3] / div / div[2] / div[3] / span / span').click()
    driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[4]/div[1]/div[1]/div[2]/textarea').send_keys(words[random.randint(0, 4)])
    driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[4]/div[1]/div[1]/div[2]/textarea').send_keys(Keys.ENTER)
