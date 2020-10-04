# simple scraper for recent urls on urlhaus, and doesnt scrape the urls with Mozi in them so that the file doesnt just get filled with that bullshit

import requests

def scrape():
    global urlhaus
    scraper = requests.get("https://urlhaus-api.abuse.ch/v1/urls/recent/")
    jsonresp = scraper.json()
    urlhaus = []
    for x in range(1000):
        urlhaus.append(jsonresp["urls"][x]["url"])

scrape()
for i in urlhaus:
    f = open("scraped-malware-urls.txt", "a")
    f.write(str(i) + '\n')
    f.close()

with open("scraped-malware-urls.txt","r+") as f:
    withoutmozi = f.readlines()
    f.seek(0)
    for line in withoutmozi:
        if "Mozi" not in line:
            f.write(line)
    f.truncate()