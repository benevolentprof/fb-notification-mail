"""
This program parses HTML and treats element tree to get information with tags
"""
import requests
from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join

directory = "data"


def get_file_list():
    only_files = [f for f in listdir(directory) if isfile(join(directory, f))]
    return only_files


def parse_file(file_name):
    with open(file_name, "r") as input_file:
        print file_name
        file_contents = input_file.read()

        soup = BeautifulSoup(file_contents, "lxml")
        web_title = soup.find_all("title")

        print web_title



file_list = get_file_list()

for f in file_list:
    parse_file(directory + "/" + f)

def urlOpener():
    print "I don't do anything"

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
    soup = urlOpener()
    main_content = soup.find_all("main", {"property": "mainContentOfPage"})
    for content in main_content:
        header_1 = content.find_all("h1", {"property": "name"}) #Why is it incomplete?
        paragraph = content.find_all("p")
    return header_1, paragraph


# title = title()
# meta = metaVariables()
# main = main()
#
# print main
