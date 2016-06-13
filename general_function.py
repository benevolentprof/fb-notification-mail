"""Create a Python web crawler"""
#Crawl entire site and gather links

import os

#Each website that is crawled is a separate project (folder)
def createProjectDirectory(directory):
    if not os.path.exists(directory):
        print 'Creating Project' + directory
        os.makedirs(directory)

#Create queue and crawled files (if not created already)
def createDataFiles(projectName, baseURL):
    queue = projectName + '/queue.txt'
    crawled = projectName + '/crawled.txt'
    if not os.path.isfile(queue): #check if the file exist already
        write_file(queue, baseURL) #starts at the homepage and starts crawling from there
    if not os.path.isfile(crawled):
        write_file(crawled, '')

#Create a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

#Add data onto an existing file
def appendToFile(path,data):
    with open(path, 'a') as file: #a mode means append/add onto
        file.write(data + '\n')

#Delete the contents of a file
def deleteFileContents(path):
    with open(path, 'w'): #do nothing, if a file exists then delete the contents
        pass

#convert links and files into a set - Read a file and convert each line to set items
def fileToSet(fileName):
    results = set()
    with open(fileName, 'r') as f: #'rt' read text-file
        for line in f:
            results.add(line.replace('\n','')) #deleting the newline part of it
    return results

# Iterate through  a set, each item will be a new line in the file
def setToFile(links, file):
    deleteFileContents(file) #deleting the file, becaue its old data
    for link in sorted(links): #loop through links
        appendToFile(file, link)



