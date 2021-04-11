import random
from selenium.webdriver.common.keys import Keys

def quote(driver):
    quotes = ["Be yourself; everyone else is already taken. -Oscar Wilde", "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe. -Albert Einstein","You only live once, but if you do it right, once is enough. -Mae West", "Be the change that you wish to see in the world. -Mahatma Gandhi"]
    # driver.find_element_by_xpath('// *[ @ id = "ow3"] / div[1] / div / div[9] / div[3] / div[1] / div[3] / div / div[2] / div[3] / span / span').click()
    driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[4]/div[1]/div[1]/div[2]/textarea').send_keys(quotes[random.randint(0, 3)])
    driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[4]/div[1]/div[1]/div[2]/textarea').send_keys(Keys.ENTER)
