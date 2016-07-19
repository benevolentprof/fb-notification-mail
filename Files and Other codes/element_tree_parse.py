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
        file_contents = input_file.read()
        soup = BeautifulSoup(file_contents, "lxml")
        web_title = soup.find_all("title")
        web_title = str(web_title)
        meta_description = soup.find_all("meta", {"name": "description"})
        meta_description = str(meta_description)
        meta_title = soup.find_all("meta", {"name": "dcterms.title"})
        meta_title = str(meta_title)
        meta_creator = soup.find_all("meta", {"name": "dcterms.creator"})
        meta_creator = str(meta_creator)
        meta_issued = soup.find_all("meta", {"name": "dcterms.issued"})
        meta_issued = str(meta_issued)
        meta_modified = soup.find_all("meta", {"name": "dcterms.modified"})
        meta_modified = str(meta_modified)
        meta_subject = soup.find_all("meta", {"name": "dcterms.subject"})
        meta_subject = str(meta_subject)
        meta_language = soup.find_all("meta", {"name": "dcterms.language"})
        meta_language = str(meta_language)
        main_content = soup.find_all("main", {"property": "mainContentOfPage"})
        for content in main_content:
            header_1 = content.find_all("h1", {"property": "name"})
            header_1 = str(header_1)
            paragraph = content.find_all("p")
            paragraph = str(paragraph)
        # all_content = web_title + "\n" + meta_description + "\n" + meta_title + "\n" + meta_creator + "\n" + meta_issued + "\n" + meta_modified + "\n" + meta_subject + "\n" +  meta_language + "\n" + header_1 + "\n" + paragraph
        # all_content = str(all_content)
        all_content = web_title, meta_description, meta_title, meta_creator, meta_issued, meta_modified, meta_subject, meta_language, header_1, paragraph
        for info in all_content:
            print info
        # with open("all_content.txt", "w") as output_file:
        #     return output_file.write(all_content)


file_list = get_file_list()

for f in file_list:
    parse_file(directory + "/" + f)


#
# def urlOpener():
#     print "I don't do anything"
#
# def title():
#     soup = parse_file()
#     web_title = soup.find_all("title")
#     return web_title
#
# def metaVariables():
#     soup = parse_file()
#     meta_description = soup.find_all("meta", {"name": "description"})
#     meta_title = soup.find_all("meta", {"name": "dcterms.title"})
#     meta_creator = soup.find_all("meta", {"name": "dcterms.creator"})
#     meta_issued = soup.find_all("meta", {"name": "dcterms.issued"})
#     meta_modified = soup.find_all("meta", {"name": "dcterms.modified"})
#     meta_subject = soup.find_all("meta", {"name": "dcterms.subject"})
#     meta_language = soup.find_all("meta", {"name": "dcterms.language"})
#     return meta_description, meta_title, meta_creator, meta_issued, meta_modified, meta_subject, meta_language
#
# def main():
#     soup = parse_file()
#     main_content = soup.find_all("main", {"property": "mainContentOfPage"})
#     for content in main_content:
#         header_1 = content.find_all("h1", {"property": "name"}) #Why is it incomplete?
#         paragraph = content.find_all("p")
#     return header_1, paragraph
#
#
# title = title()
# meta = metaVariables()
# main = main()
#
# print main
