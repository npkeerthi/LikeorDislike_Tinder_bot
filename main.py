from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

chromedriver_path= r"C:\Users\Admin\OneDrive\Desktop\Angela\chromedriver.exe"
drive=webdriver.Chrome(chromedriver_path)
drive.get("https://tinder.com/")
# drive.maximize_window()
sleep(1)

login=drive.find_element_by_xpath('//*[@id="s-2061886532"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
login.click()
sleep(1)
print("1")
try:
    moreopt=drive.find_element_by_xpath('//*[@id="s192874960"]/div/div/div[1]/div/div[3]/span/button')
    moreopt.click()
except NoSuchElementException:
    withfb = drive.find_element_by_xpath('//*[@id="s192874960"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    withfb.click()

sleep(2)
print("2")

try:
    withfb=drive.find_element_by_xpath('//*[@id="s192874960"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    withfb.click()
    sleep(2)
except NoSuchElementException:
    wrong = drive.find_element_by_xpath('//*[@id="s192874960"]/div/div/div[2]/button')
    wrong.click()
    login = drive.find_element_by_xpath('//*[@id="s-2061886532"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
    login.click()
    moreopt = drive.find_element_by_xpath('//*[@id="s192874960"]/div/div/div[1]/div/div[3]/span/button')
    moreopt.click()
    # sleep(5)
    withfb = drive.find_element_by_xpath('//*[@id="s192874960"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    withfb.click()



#IMPORTANT PART switching windows for more info scroll down comments

tindwind=drive.window_handles[0]
fbwindow=drive.window_handles[1]
drive.switch_to.window(fbwindow)
print(drive.title)
fb=drive.find_element_by_xpath('//*[@id="email"]')

fb_mail="YOURMAIL_fol95213@zwoho.com"
fb.send_keys(fb_mail)
fb_pass=drive.find_element_by_xpath('//*[@id="pass"]')
fb_pass.send_keys("YOURPASWORD")
fb_pass.send_keys(Keys.ENTER)
# login=drive.find_element_by_xpath('//*[@id="loginbutton"]')
# login.click()
sleep(2)

drive.switch_to.window(tindwind)
print(drive.title)

sleep(5)
allowlocation=drive.find_element_by_xpath('//*[@id="s192874960"]/div/div/div/div/div[3]/button[1]/span')
allowlocation.click()
notinterested=drive.find_element_by_xpath('//*[@id="s192874960"]/div/div/div/div/div[3]/button[2]/span')
notinterested.click()


for i in range(100):
        sleep(2)
        runningthings=""
    # try:
        # sleep(2)
        # like=drive.find_element_by_xpath('//*[@id="s-2061886532"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[5]/div/div[4]/button/span/span')#  //*[@id="s-2061886532"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button/span/span/svg
        # like=drive.find_element_by_css_selector("button .Scale(.5)")
        
        like = drive.find_element_by_xpath(xpath='/html/body')#xpath='/html/body')
        like.send_keys(Keys.ARROW_RIGHT)                                                                                                
        # dislike=like.send_keys(Keys.ARROW_LEFT)                    #IF YOU WANT ONLY DISLIKING UNCOMMENT THIS and comment above line

        sleep(2)  # wait atleast my eyes sees it😂
        like.click()
        sleep(2)  # wait atleast my eyes sees it😂
        print("✔")
        print(like.click(),like.text)
        runningthings+=like.text
        runninglist=runningthings.split("\n")
        print(runninglist)

        if runninglist[-1]=='NOT INTERESTED':
            print("shit")
            not_interested = drive.find_element_by_xpath('//*[@id="s192874960"]/div/div/div[2]/button[2]/span')
            not_interested.click()
            continue