# This function removes all currently running creatives
# and swaps in new creatives in the selected campaigns.

# It also sends a message every time an error occurs,
# e.g. campaign is not found, page could not load, creative not found

# Inputs: email, password, CSV list of campaigns and creatives to turn in


# Using selenium to help navigate the Chartboost website
from selenium import webdriver
import time
import sys
import csv
import ctypes
user32 = ctypes.windll.user32

# We'll use the given CSV to compile a dictionary
# of campaign IDs and a list of creatives to turn
creativeList = {}
with open(sys.argv[3]) as f:
	csv_f = csv.reader(f)
	for row in csv_f:
		creativeList.setdefault(row[0],[]).append(row[1])


# Also open a file to record any errors
outputFile = open('errors.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow([time.localtime()])

# Opens a Chrome window not signed in to any Google profile
# loads the Chartboost website to log in
# and resizes window to fit screen resolution
browser = webdriver.Chrome()
url = "https://dashboard.chartboost.com/login"
browser.get(url)
browser.set_window_size(user32.GetSystemMetrics(0),user32.GetSystemMetrics(1))

# We will need to log in to Chartboost
time.sleep(10)
email = sys.argv[1]
password = sys.argv[2]

emailInput = browser.find_element_by_name('email')
emailInput.send_keys(email)

passwordInput = browser.find_element_by_name('password')
passwordInput.send_keys(password)

browser.find_element_by_class_name('login-layout__submit').click()

# For every campaign ID in the CSV:
for campaignID in creativeList.keys():
	# Error checking: tries to turn creatives,
	# returns campaign IDs that were not turned
	try:
		# Navigate to our advertising campaigns
		time.sleep(3)
		browser.get('https://dashboard.chartboost.com/all/campaigns/' + campaignID)
		print('Navigating to '+campaignID)
		time.sleep(10)
		print('**REMOVING CREATIVES**')
		time.sleep(5)
		removeButtons = browser.find_elements_by_css_selector('i.ui.minus.creatives.icon')
		if len(removeButtons) == 0:
			raise ValueError('0 creatives to remove')
		print(str(len(removeButtons)) + ' creatives to remove:')
		time.sleep(2)
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

		for creative in creativeList[campaignID]:
			elem = browser.find_element_by_xpath("//div[contains(text(), '" + creative + "')]/preceding-sibling::div[2]")
			elem.click()
			print('+ ' + creative)
			time.sleep(2)


		browser.find_element_by_id('network-advertiser__target-0__creatives__actions--confirm').click()
		time.sleep(3)

		# Save your progress - press the save button
		browser.find_element_by_id('network-advertiser__enabled-actions--save').click()
		time.sleep(10)
		print('Creative turn for ' + campaignID + ' completed\n')
	except Exception as e:
		print('Error in campaign ' + campaignID + ': ' + str(e) + '\n')
		outputWriter.writerow([campaignID, e])
		continue
	#except Exception as e:
	#	print('Error for campaign', campaignID, ':', e)
	#	outputWriter.writerow(list(campaignID, e))
	#	continue


outputFile.close()
browser.quit()