from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser
from bs4 import BeautifulSoup
import time

'''
I'm trying to scrape the adresses of all electrical transformer stations in Poland from a map.

The map is dynamically loaded and to get an address of a given station the user has to hover their mouse over
an icon respresenting a station, then wait until a balloon(?) pops up and then click "more", which redirects
them to a new page in a new window in their browser.

The number of stations to be scraped is in the hundreds, so using a web crawler will be very time-indefficient(?).

There are no <a> tags in the html so I couln't find any links.

I tried looking through the requests the website sends to the server, but I didn't find  any that would lead
me to the appropriate website.

I am mainly looking to understand how the website sends requests to the server to redirect the user to the new window
and find the best way to scrape the website.
'''

url = 'https://mapa.targeo.pl/trafostacja,26,21.3768641,52.0938685?data=eyJmdHMiOnsicSI6InRyYWZvc3RhY2phIn0sIndpbiI6InNlYXJjaC1mb3JtIn0='


with sync_playwright() as p:
    # open the page
    browser = p.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto(url)

    page.wait_for_selector('span[onclick="document.body.removeChild(this.parentNode.parentNode.parentNode)"]')
    page.click('span[onclick="document.body.removeChild(this.parentNode.parentNode.parentNode)"]')

    #use the cursor to get to the other page

    #page.click('#POI21626226')
    time.sleep(3)
    #print('click')
    
    #POI21626226

#targeo-balloon-footerlink-white

