from selenium import webdriver
from time import sleep
import urllib.request

driver = webdriver.Chrome()

driver.get('https://www.instagram.com/')
sleep(2)

login_link = driver.find_element_by_xpath("//*[@id='loginForm']")
login_link.click()

sleep(2)

username_input = driver.find_element_by_css_selector("input[name='username']")
password_input = driver.find_element_by_css_selector("input[name='password']")

username_input.send_keys("USERNAME")
password_input.send_keys("PASSWORD")

login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(3)
driver.get("https://instagram.com/funnywhimsical/")
#Scroll to Last
lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match = False
while(match==False):
    lastCount = lenOfPage
    sleep(3)
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True

posts = []
links = driver.find_elements_by_tag_name('a')
for link in links:
    post = link.get_attribute('href')
    if '/p/' in post:
        posts.append(post)

print(posts)

download_url = ''
for post in posts:
    driver.get(post)
    url = driver.current_url
    shortcode = url.split("/")[-2]
    urllib.request.urlretrieve(url, "{}.jpg".format(shortcode))

    print( download_url )

driver.close()