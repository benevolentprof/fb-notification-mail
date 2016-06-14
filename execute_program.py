from expDomain import *
from general_function import *
from Queue import Queue
from spider_class import *
import threading


PROJECT_NAME = 'VAC'
HOMEPAGE = 'http://www.veterans.gc.ca/eng'
DOMAIN_NAME = getDomainName(HOMEPAGE)
QUEUED_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 6
queue = Queue() #thread queue
spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

#Create spider threads (will die when main exits)
def create_spiders():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True #die whenever the main exits
        t.start()

#Do the next job in the queue
def work():
    while True:
        url = queue.get() #get the next item in the thread queue
        spider.crawlPage(threading.current_thread.name, url)
        queue.task_done()


#Each queued link is a new job
def create_jobs():
    for link in fileToSet(QUEUED_FILE):
        queue.put(link)
    queue.join()
    crawl()


#check in the there are items in the queue list
def crawl():
    queued_links = fileToSet(QUEUED_FILE)
    if len(queued_links)  > 0: #state how many links are left in the QUEUED_FILE
        print str(len(queued_links)) + 'links in the queue'
        create_jobs()

create_spiders()
crawl()
