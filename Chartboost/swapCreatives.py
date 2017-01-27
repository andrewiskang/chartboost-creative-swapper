# This function removes all currently running creatives
# and swaps in new creatives in the selected campaigns.

# It also sends a message every time an error occurs,
# e.g. campaign is not found, page could not load, creative not found

# Using selenium to help navigate the Chartboost website
from selenium import webdriver
import time
import sys

# Opens a Chrome window not signed in to any Google profile
# and loads the Chartboost website to log in
browser = webdriver.Chrome()
url = "https://dashboard.chartboost.com/login"
browser.get(url)

# We will need to log in to Chartboost
time.sleep(10)
email = sys.argv[1]
password = sys.argv[2]

emailInput = browser.find_element_by_name('email')
emailInput.send_keys(email)

passwordInput = browser.find_element_by_name('password')
passwordInput.send_keys(password)

browser.find_element_by_class_name('login-layout__submit').click()

# Navigate to our advertising campaigns
time.sleep(3)
browser.get('https://dashboard.chartboost.com/all/campaigns/' + '53dc096fc26ee47d9e5a8e8e')

time.sleep(10)
print('**REMOVING CREATIVES**')
time.sleep(5)
removeButtons = browser.find_elements_by_css_selector('i.ui.minus.creatives.icon')
print(str(len(removeButtons)) + ' creatives to remove:')
for button in removeButtons:
	button.click()
	print('creative removed')
	time.sleep(2)

# Add in creatives:
# - Press "Select Existing"
# - Search for a given creative name
# - Tick the box to the left
# - Press "Confirm"

print('**TURNING IN CREATIVES**')
time.sleep(2)

browser.find_element_by_id('network-advertiser__target-0__creatives__actions--select-existing').click()
time.sleep(2)

# For now, assume a list of creatives to turn in
creative1 = '20160915-g3-trunsky-Android-English'
creative2 = '20170125-ss-trunskyleaf-Android-English'
creative3 = '20170125-g3-tigerflame-Android-English'
creative4 = '20170125-cp-gameplay-Android-English'
creative5 = '20170125-g3-gunlion-Android-English'
creativeList = [creative1, creative2, creative3, creative4, creative5]

for creative in creativeList:
	elem = browser.find_element_by_xpath("//div[contains(text(), '" + creative + "')]/preceding-sibling::div[2]")
	elem.click()
	print('+ ' + creative)
	time.sleep(2)


browser.find_element_by_id('network-advertiser__target-0__creatives__actions--confirm').click()
time.sleep(3)

# Save your progress - press the save button
browser.find_element_by_id('network-advertiser__enabled-actions--save').click()
time.sleep(10)
browser.quit()