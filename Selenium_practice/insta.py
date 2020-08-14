import getpass
import time
import requests
import requests_html
import os
from urllib.parse import urlparse
#password = getpass.getpass("What is your password?")

from conf import INSTA_PASSWORD, INSTA_USERNAME
from selenium import webdriver

browser = webdriver.Chrome('/usr/bin/chromedriver')

url = 'https://www.instagram.com/'
browser.get(url)

time.sleep(5)
username_el = browser.find_element_by_name("username")
username_el.send_keys(INSTA_USERNAME)
password_el = browser.find_element_by_name("password")
password_el.send_keys(INSTA_PASSWORD)
time.sleep(4)
submit_btn_el = browser.find_element_by_css_selector("button[type='submit']")
submit_btn_el.click()

login_innfo_save_btn_el = browser.find_element_by_css_selector("button[type='button']")
login_innfo_save_btn_el.click()
time.sleep(4)
body_el = browser.find_element_by_css_selector("body")
html_text = body_el.get_attribute("innerHTML")

#print(html_text)

login_innfo_save_btn_el = "//button[contains(text(), 'Save Info')]"
if browser.find_element_by_xpath(login_innfo_save_btn_el) != None:
    login_innfo_save_btn_el = browser.find_element_by_xpath(login_innfo_save_btn_el)
    time.sleep(4)
    login_innfo_save_btn_el.click()

"""
<button class="_5f5mN       jIbKX  _6VtSN     yZn4P   ">Follow</button>
<button class="sqdOP  L3NKy   y3zKF     " type="button">Save Info</button>
<button class="aOOlW   HoLwm " tabindex="0">Not Now</button>
"""
#xpath
#my_button_xpath = "//button"
#browser.find_elements_by_xpath(my_button_xpath)

def click_to_follow(browser):
    #my_follow_btn_xpath = "//a[contains(text(), 'Follow')] [not(contains(text(), 'Following'))]"
    #my_follow_btn_xpath = "//*[contains(text(), 'Follow')] [not(contains(text(), 'Following'))]"
    my_follow_btn_xpath = "//button[contains(text(), 'Follow')] [not(contains(text(), 'Following'))] [not(contains(text(), 'Followers'))]"
    follow_btn_elements = browser.find_elements_by_xpath(my_follow_btn_xpath)
    for btn in follow_btn_elements:
        time.sleep(2)
        try:
            btn.click()
        except:
            pass
print("kimkardasian")
time.sleep(2)
new_user_url = 'https://www.instagram.com/kimkardashian/'
browser.get(new_user_url)
time.sleep(3)
click_to_follow(browser)

time.sleep(2)
the_rock_url = "https://www.instagram.com/mooroosicity/"
browser.get(the_rock_url)

insta_post_url_pattern = "https://www.instagram.com/p/<post-url-slang>"
post_xpath_str = "//a[contains(@href, '/p/')]"
post_links = browser.find_elements_by_xpath(post_xpath_str)
post_link = None
if len(post_links) > 0:
    post_link_el = post_links[0]
if post_link_el != None:
    post_href = post_link_el.get_attribute("href")
    browser.get(post_href)

video_els = browser.find_elements_by_xpath("//video")
image_els = browser.find_elements_by_xpath("//img")
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, "data")
os.makedirs(data_dir, exist_ok=True)

def scrape_and_save(elements):
    for el in elements:
        #print(img.get_attribute('src'))
        url = el.get_attribute('src')
        base_url = urlparse(url).path
        filename = os.path.basename(base_url)
        filepath = os.path.join(data_dir, filename)
        if os.path.exists(filepath):
            continue 
        with requests.get(url, stream=True) as r:
            try:
                r.raise_for_status()
            except:
                continue
            with open(filepath, 'wb') as f:
                for chunk in r.iter_content():
                    if chunk:
                        f.write(chunk)

scrape_and_save(video_els)
scrape_and_save(image_els)

"""
while True:
    time.sleep(2)
    click_to_follow(browser)
"""