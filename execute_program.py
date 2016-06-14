from Queue import Queue
from general_function import *
from spider_class import spider
from expDomain import *

PROJECT_NAME = 'Example'
HOMEPAGE = 'http://www.veterans.gc.ca/eng'
DOMAIN_NAME = getDomainName(HOMEPAGE)
QUEUED_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
numberOfThreads = 6
queue = Queue() #thread queue
spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)
