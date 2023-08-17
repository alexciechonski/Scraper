from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser
from bs4 import BeautifulSoup
import time

# open the website
# search "trafostacja"
# get all the trafostacje addresses
# create a json with nr - address

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

