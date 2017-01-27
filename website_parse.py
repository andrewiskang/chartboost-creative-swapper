from bs4 import BeautifulSoup
import requests

r = requests.get("http://hours.lib.uchicago.edu/")
hourPageSoup = BeautifulSoup(r.text, 'lxml')
regData = hourPageSoup.find(id = "reg_data")

# define a function to return all siblings of the first result, except for the first
def rest_siblings(soup, str):
    return soup.find(str).find_next_siblings(str)

print(hourPageSoup.title.string, "\n")

lib_sections = rest_siblings(regData, "tr")


libSectionList = []


for section in lib_sections:





"""
from bs4 import BeautifulSoup
import requests

#get page
r = requests.get("http://www.lib.ucdavis.edu/ul/about/hours/")
hourPageSoup = BeautifulSoup(r.text, 'html5lib')

#find each section where hours are located
LibraryList = hourPageSoup.find_all(class_="page-section hours")

#create list for Library information
libraryInfoList = []

for hourDivSoup in LibraryList:
    #get library name and initialize the library library
    libraryInfo = {'name':hourDivSoup.h3.text, 'standardSchedule':{}, 'exceptions':[] }

    #hydrate standard hours
    hourDiv = hourDivSoup.find(class_='hours')
    for tr in hourDiv.find_all('tr'):
        day = tr.find(class_='date').text.strip()
        open,close = tr.find(class_='time').text.split("-")
        libraryInfo['standardSchedule'][day] = {'open':open, 'close':close}

    #hydrate exception dates
    exceptDiv = hourDivSoup.find(class_='exceptions')
    for tr in exceptDiv.find_all('tr'):
        date = tr.find(class_='date').text.strip()
        open,close = tr.find(class_='time').text.split("-")
        notes = tr.find(class_='name').text.strip()
        libraryInfo['exceptions'].append({'date':date, 'open':open, 'close':close, 'notes':notes})

    libraryInfoList.append(libraryInfo)

print(libraryInfoList)

for elem in libraryInfoList:
    print(elem['name'])
"""
