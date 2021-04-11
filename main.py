from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from functions.login import turnOffMicCam,AskToJoin,Glogin,joinNow
from functions.attendance import attendance
from functions.attendanceform import attendanceForm
from functions.createpdf import createpdf
from functions.randomstudent import randomStudent
from functions.newword import newWord
from functions.quotes import quote
from functions.screenshots import ss
from functions.foullang import foulLanguage
from chat import chatbot

#ADD CREDENTIALS HERE
CREDS = {'email' : 'gmeethelpbot2@gmail.com','passwd':'chickenwings'}

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("--mute-audio")
opt.add_argument("start-maximized")
opt.add_argument("enable-usermedia-screen-capturing")
opt.add_experimental_option('excludeSwitches', ['test-type'])
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
})

driver= webdriver.Chrome(executable_path=r"C:\Users\Shvetha M Nambiar\Desktop\Hack\gmeetpluging\drivers\chromedriver.exe",options=opt)
print("browser up")

def commands():
    i=2
    key=1
    j=1
    driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[1]/div[3]/div/div[2]/div[3]/span').click()
    mom=[]
    students=[]
    foulLangUser=[]
    driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[4]/div[1]/div[1]/div[2]/textarea').send_keys("Hi! I'm Hirav, your Gmeet companion. Use '/help' to read all my commands" + Keys.ENTER)
    #infinite loop
    while(key==1):
        WebDriverWait(driver, 2000000000).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[2]/div['+str(i)+']/div[2]/div['+str(j)+']')))
        print('1. value of i is',i)
        print('1. value of j is',j)
        instText=driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[2]/div['+str(i)+']/div[2]/div['+str(j)+']').text
        instText=str(instText).lower()

        #foul language
        if(foulLanguage(instText)):
            nameFoulUser=driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[2]/div['+str(i)+']/div[1]/div['+str(j)+']').text
            foulLangUser.append(str(nameFoulUser))
            driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[4]/div[1]/div[1]/div[2]/textarea').send_keys(str(nameFoulUser)+", please don't make use of inappropriate language." + Keys.ENTER)
            i=i+2
            j=1
            print(' Foul message',i,j)
        #chatbot
        elif(instText.find('bot/')!=-1):
            answer=chatbot(instText[4:]) 
            driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[4]/div[1]/div[1]/div[2]/textarea').send_keys(answer + Keys.ENTER)
            i=i+2
            j=1  
            print(' bot message',i,j)        
        #all tags
        elif(instText=='/attendance'):
            students=attendance(driver)
            i=i+2
            j=1
            print(' Attendance printed',i,j)
        elif(instText=='/attendanceform'):
            attendanceForm(driver)
            i=i+2
            j=1
            print(' attendanceform printed',i,j)
        elif(instText.find('m/')!=-1):
            mom.append(instText[2:])
            driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[4]/div[1]/div[1]/div[2]/textarea').send_keys('Updated' + Keys.ENTER)
            i=i+2
            j=1
            print('Mom created',i,j)
        elif(instText=='/random'):
            randomStudent(driver)
            i=i+2
            j=1
            print(' random printed',i,j)
        elif(instText=='/quote'):
            quote(driver)
            i=i+2
            j=1
            print(' quote printed',i,j)
        elif(instText=='/newword'):
            newWord(driver)
            i=i+2
            j=1
            print(' newword printed',i,j)
        elif(instText=='/ss'):
            ss(driver)
            i=i+2
            j=1
            print('Screenshot taken',i,j)
        elif(instText=='/help'):
            commandingString="/attendace -Take attendace in the meeting\n/attendanceform -Generating google attendance form\n/random -Selecting a random attendee\n/quote- Generating a qoute\n/newword -Genrating a new word\n/ss -Taking and storing a screenshot\nbot/your question -Ask questions to our bot\nm/your text -To updated your mom\n/exit -To make the bot exit from the GMeet"
            driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[4]/div[1]/div[1]/div[2]/textarea').send_keys( str(commandingString)+ Keys.ENTER)
            i=i+2
            j=1
        elif(instText=='/exit'):
            key=0
            createpdf(students,mom,foulLangUser)
            i=i+2
            j=1
            print('mom printed and exit',i,j)
            driver.close()
        else:
            j=j+1
            print(' coming here')
       
        # try:
        #     elem = driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[2]/div[' + str(i + 1) + ']/div[1]/div[1]')
        #     print('try is working')
        #     flag=True
        # except NoSuchElementException: 
        #     flag=False   
        #     print('except is working')
    
        # if(flag==True):
        #     i=i+1
        #     j=1
        # print('2. value of i is',i)
        # print('2. value of j is',j)


# login()
Glogin(CREDS['email'], CREDS['passwd'],driver)
driver.get("https://meet.google.com/ruw-jhcm-szo")
time.sleep(5)
turnOffMicCam(driver)
driver.implicitly_wait(15)
joinNow(driver)
driver.implicitly_wait(10)
time.sleep(5)
commands()

