# Hirav - Smart companion to your G-Meet
- Hirav is a smart companion G-Meet bot which uses selenium to add an bot to G-Meet to add multiple functionality in the meeting.

## Description
The bot can do the following things with the following commands on inputing the commands into the G-Meet chat box-
- Survey/attendance form ` /attendaceform `
- checking for inappropriate/foul language (inbuilt function)
- making a list of attendees ` /attendance `
- making an mom and putting the attendance and writing the names of defaulters who used inappropriate language and forming them into a pdf once the bot exits ` m/text `
- taking screenshot ` /ss `
- providing the name of a random attendee ` /random `
- providing with a new word  ` /newword `
- activating chat bot `bot/text`
- generating the pdf with MOM, attendance, and profanity `/exit`


Needed python libraries
- Selenium  ` pip install -U seleium `
- pyautogui  `pip install pyautogui `
- torch      `pip install torch`
- fpdf        `pip install fpdf`
- nltk       `pip install nltk`
