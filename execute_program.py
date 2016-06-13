from Queue import Queue
from general_function import *
from spider_class import spider
from expDomain import *

projectName = 'VAC'
homePage = 'http://www.veterans.gc.ca/myvacaccount'
domainName = getDomainName(homePage)
queueFile = projectName + '/queue.txt'
crawledFile = projectName + '/crawled.txt'
numberOfThreads = 6
queue = Queue() #thread queue
spider(projectName, homePage, domainName)