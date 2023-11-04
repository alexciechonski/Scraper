from playwright.sync_api import sync_playwright
import requests
import json

url = 'https://mapa.targeo.pl/trafostacje,21,21.0611944,52.2237696?data=eyJmdHMiOnsicSI6InRyYWZvc3RhY2plIn0sIndpbiI6InNlYXJjaC1mb3JtIn0='

def get_php_session_id():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto(url)

        page.wait_for_selector('#targeo-fts-result') #change 

        # Get the PHPSESSID cookie
        cookies = page.context.cookies()
        php_session_id = None
        for cookie in cookies:
            if cookie['name'] == 'PHPSESSID':
                php_session_id = cookie['value']
                break

        return php_session_id


php_session_id = get_php_session_id()
if php_session_id:
    print(f'PHPSESSID: {php_session_id}')
else:
    print('PHPSESSID not found.')

endpoint = "https://m44.targeo.pl/service.html?xhr=1&rpc=FTS&q=trafostacje&c=%7B%22x%22%3A21.0372319%2C%20%22y%22%3A52.2302547%7D&area=%7B%22l%22%3A0%2C%20%22t%22%3A0%2C%20%22r%22%3A691%2C%20%22b%22%3A1004%7D&tmk=TargeoMap&k=ODY2NzI1YjgzOWFlMWM4YjM5Zjc2N2U5MTAzNjY1Y2Q5MTE2ODA0NQ%3D%3D&vn=2_5&uu=ff56a51a7a27a902de4e6a8bbaa446c7"

headers = {
    'accept': '/',
    'accept-language': 'en-GB,en;q=0.6',
    'authority': 'm44.targeo.pl',
    'content-type': 'text/plain; charset=UTF-8',
    'cookie': f'cpw=231002%2F1; __sn=m4; PHPSESSID={php_session_id}; U=ff56a51a7a27a902de4e6a8bbaa446c7; cc=2; ln=en; _ox_searchcnt=4; o=20,21.0406973,52.2303861,drag; PHPSESSID={php_session_id}',
    'origin': 'https://mapa.targeo.pl',
    'referer': 'https://mapa.targeo.pl/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Brave";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'macOS',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

response = requests.get(endpoint, headers=headers)
response.json()