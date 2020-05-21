import urllib
import requests
from bs4 import BeautifulSoup

print('''


  _   _ _  _       _ _____        ____                   _        ____             _             
 | | | | || |   __| |___ / ___   / ___| ___   ___   __ _| | ___  |  _ \  ___  _ __| | _____ _ __ 
 | |_| | || |_ / _` | |_ \/ __| | |  _ / _ \ / _ \ / _` | |/ _ \ | | | |/ _ \| '__| |/ / _ | '__|
 |  _  |__   _| (_| |___) \__ \ | |_| | (_) | (_) | (_| | |  __/ | |_| | (_) | |  |   |  __| |   
 |_| |_|  |_|  \__,_|____/|___/  \____|\___/ \___/ \__, |_|\___| |____/ \___/|_|  |_|\_\___|_|   
                                                   |___/  
''')

print("Programmed: 5/21/2020")


# desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
# mobile user-agent
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"

query = input("Google Dorks =>:  ")
query = query.replace(' ', '+')
URL = f"https://google.com/search?q={query}"

headers = {"user-agent": USER_AGENT}
resp = requests.get(URL, headers=headers)

if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, "html.parser")
    results = []
    for g in soup.find_all('div', class_='r'):
        anchors = g.find_all('a')
        if anchors:
            link = anchors[0]['href']
            #title = g.find('h3').text
            #item = {
                #link
                #"title": title,
                #"link": link
            #}
            item = link
            results.append(item)
            with open(input('Filename For the Dorked Websites ==>: '), 'a') as f:
                print(results, file=f)
