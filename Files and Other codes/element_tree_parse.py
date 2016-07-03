"""
This program parses HTML and treats element tree to get information with tags
"""
import requests
from bs4 import BeautifulSoup

# vacSite = requests.get("http://www.veterans.gc.ca/eng/services/financial")
# soup = BeautifulSoup(vacSite.content, "lxml")
def urlOpener():
    vacSite = requests.get("http://www.veterans.gc.ca/eng/services/financial")
    soup = BeautifulSoup(vacSite.content, "lxml")
    return soup

def title():
    soup = urlOpener()
    web_title = soup.find_all("title")
    return web_title

def metaVariables():
    soup = urlOpener()
    meta_description = soup.find_all("meta", {"name": "description"})
    meta_title = soup.find_all("meta", {"name": "dcterms.title"})
    meta_creator = soup.find_all("meta", {"name": "dcterms.creator"})
    meta_issued = soup.find_all("meta", {"name": "dcterms.issued"})
    meta_modified = soup.find_all("meta", {"name": "dcterms.modified"})
    meta_subject = soup.find_all("meta", {"name": "dcterms.subject"})
    meta_language = soup.find_all("meta", {"name": "dcterms.language"})
    return meta_description, meta_title, meta_creator, meta_issued, meta_modified, meta_subject, meta_language

def main():


title = title()
meta = metaVariables()




