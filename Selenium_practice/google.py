import time
from selenium import webdriver

browser = webdriver.Chrome('/usr/bin/chromedriver')
#executable_path='/usr/bin/google-chrome', service_log_path='/usr/share/man/man1/google-chrome.1.gz'
url = 'https://www.google.com/'
browser.get(url)

"""
<input type='text'  class='' id='' name='??/>
<textarea></textarea
----------------------------
<input name="q" type="text">

"""
time.sleep(2)
name = 'q'
search_el = browser.find_element_by_name("q")
#print(search_el)

search_el.send_keys("selenium python")

"""
<input type='submit' />
<button type='submit' />
<form> </form>
"""

submit_btn_el = browser.find_element_by_css_selector("input[type='submit']")
print(submit_btn_el.get_attribute('name'))
time.sleep(2)
submit_btn_el.click()