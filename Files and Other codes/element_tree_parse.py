"""
This program parses HTML and treats element tree to get information with tags
"""
import requests
from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join

directory = "data"
txt_directory = "txt"
xml_directory = "xml"

def get_file_list():
    only_files = [f for f in listdir(directory) if isfile(join(directory, f))]
    return only_files


def parse_file(file_name):
    with open(file_name, "r") as input_file:
        file_contents = input_file.read()
        soup = BeautifulSoup(file_contents, "lxml")

        # output = ""
        output = unicode.join(u'\n', map(unicode, soup.find_all("title")))
        output += unicode.join(u'\n', map(unicode, soup.find_all("meta", {"name": "description"})))
        output += unicode.join(u'\n', map(unicode, soup.find_all("meta", {"name": "dcterms.title"})))
        output += unicode.join(u'\n', map(unicode, soup.find_all("meta", {"name": "dcterms.creator"})))
        output += unicode.join(u'\n', map(unicode, soup.find_all("meta", {"name": "dcterms.issued"})))
        output += unicode.join(u'\n', map(unicode, soup.find_all("meta", {"name": "dcterms.modified"})))
        output += unicode.join(u'\n', map(unicode, soup.find_all("meta", {"name": "dcterms.subject"})))
        output += unicode.join(u'\n', map(unicode, soup.find_all("meta", {"name": "dcterms.language"})))

        main_content = soup.find_all("main", {"property": "mainContentOfPage"})
        for content in main_content:
            output += unicode.join(u'\n', map(unicode, content.find_all("h1", {"property": "name"})))
            output += unicode.join(u'\n', map(unicode, content.find_all("p")))

        return output
        # with open("workinfo.txt", "w") as output_file:
        #     output_file.write(output.encode('utf8'))


file_list = get_file_list()
for f in file_list:
    data_needed = parse_file(directory + '/' + f)
    output = open(f+'.xml', 'w')
    output.write(data_needed.encode('utf8'))
    print parse_file(directory + '/' + f)
