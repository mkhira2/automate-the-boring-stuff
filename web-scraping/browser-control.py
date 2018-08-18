from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://automatetheboringstuff.com')

elem = browser.find_element_by_css_selector('body > div.main > div:nth-child(1) > ul:nth-child(18) > li:nth-child(1) > a') # finds single element

elem.click()

elems = browser.find_elements_by_css_selector('p') # finds multiple elements
print(len(elems))

searchElem = browser.find_element_by_css_selector('.search-field')
searchElem.send_keys('zophie')
searchElem.submit()

#-- other useful selenium methods --#
# browser.back()
# browser.forward()
# browser.refresh()
# browser.quit()

browser = webdriver.Chrome()
browser.get('https://automatetheboringstuff.com')
elem = browser.find_element_by_css_selector('.entry-content > p:nth-child(4)')
print(elem.text)