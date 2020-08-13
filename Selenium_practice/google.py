from selenium import webdriver

browser = webdriver.Chrome(executable_path='/usr/bin/google-chrome', service_log_path='/usr/share/man/man1/google-chrome.1.gz')

url = 'https://www.google.com/'
browser.get(url)

"""
<input type='text'  class='' id='' name='??/>
<textarea></textarea
----------------------------
<input name="q" type="text">

"""
name = 'q'
search_el = browser.find_element_by_name("q")
print(search_el)

search_el.send_keys("selenium python")