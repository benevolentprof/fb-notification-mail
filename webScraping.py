"""Project to scrap information from the websites"""
import requests
from bs4 import BeautifulSoup
with open("parseExample.txt", 'w') as parseOut:

    vacSite = requests.get("http://www.veterans.gc.ca/eng/services/financial/cf-income-support")
    # print vacSite.content
    soup = BeautifulSoup(vacSite.content, "lxml") #convert it to something usable using BeautifulSoup
    # print soup.prettify()
    vacLink = {}
    links = soup.find_all("a")
    """Take all links from the page"""
    for link in links:
        print "<a href='%s'>%s</a>" %(link.get("href"), link.text)
        parseOut.write("<a href='%s'>%s</a> + \n" %(link.get("href"), link.text.encode("utf-8")))

with open("parseExample2.txt", 'w') as infoOut:

    generalData = soup.find_all("main", {"property": "mainContentOfPage"})
    for information in generalData:
        print information.text
        infoOut.write(information.text.encode("utf-8"))






