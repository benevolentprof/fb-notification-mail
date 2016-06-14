"""Building a spider - grab a link from the waiting list and connect to that page, grab all the HTML and throw into linkFinder (where it will be parsed)
  take link from waiting list into crawled file"""
import urllib2 #connect webpages from python
from general_function import *
from link_finder import linkFinder
from httplib import HTTPResponse

class spider:
    #class variable - is shared among all instances
    projectName = ''
    baseUrl = ''
    domainName = ''
    queueFile = '' #saved into a txt file but same data with queue and crawled
    crawledFile = ''
    queue = set() #waiting list
    crawled = set() #what you've crawled

    def __init__(self, projectName, baseUrl, domainName):
        spider.projectName = projectName
        spider.baseUrl = baseUrl
        spider.domainName = domainName
        spider.queueFile = spider.projectName + '/queue.txt'
        spider.crawledFile = spider.projectName + '/crawled.txt'
        self.boot()
        self.crawlPage('First spider  ',spider.baseUrl) #initial spider in home page

    @staticmethod
    def boot(): #create project directory and 2 data files (queue and crawled txt files)
        createProjectDirectory(spider.projectName)
        createDataFiles(spider.projectName, spider.baseUrl) #create a waiting list and add the homepage to it
        spider.queue = fileToSet(spider.queueFile) #get updated list and save it to set
        spider.crawled = fileToSet(spider.crawledFile)

    @staticmethod
    def crawlPage(threadName, pageUrl):
        print "",type(spider.gatherLinks(pageUrl))
        if pageUrl not in spider.crawled:
            print threadName + 'crawling  ' + pageUrl
            print 'Queue ' + str(len(spider.queue)) + '| Crawled ' + str(len(spider.crawled))
            spider.addLinkstoQueue(spider.gatherLinks(pageUrl)) #once set of links are retrieved then add on waiting list, return a set of links
            spider.queue.remove(pageUrl) #remove to the waiting list to the crawled list
            spider.crawled.add(pageUrl)
            spider.updateFiles()

    @staticmethod
    def gatherLinks(pageUrl): #connect to the webpage and return set of links found on webpage
        print("GATHERLINKS SURE IS RUNNING")
        htmlString = '' #response is in bytes so variable will be in string
        print pageUrl
        request = urllib2.Request(pageUrl)
        try: #handle exception for network
            print("AND SURE GOES INSIDE THE TRY")
            response = urllib2.urlopen(request)
            print ("THIS IS AFTER RESPONSE")
            #if response.info().getheader('Content-Type') == 'text/html':
            if 'text/html' in response.info().getheader('Content-Type'):
                print ("IM IN THE IF-STATEMENT TOO")
                htmlBytes = response.read() #read raw response which is 1s and 0s
                htmlString = htmlBytes.decode("utf-8") #convert to readable characters which will be passed onto linkFinder
            finder = linkFinder(spider.baseUrl,pageUrl)
            finder.feed(htmlString)#pass the html data to parse it
        except:
            print 'Error: Cannot Crawl Page'
            return set() #if there is error, then return empty set
        return finder.pageLinks()

    @staticmethod
    def addLinkstoQueue(links):
        for url in links:
            if url in spider.queue: #make sure link is not in waiting list
                continue
            if url in spider.crawled: #make sure link is not in crawled list
                continue
            if spider.domainName not in url: #make sure that the spider stays in the URL and not go to different sites
                continue
            spider.queue.add(url) #add the url

    @staticmethod
    def updateFiles():
        setToFile(spider.queue,spider.queueFile)
        setToFile(spider.crawled, spider.crawledFile)

#disMahSmartSpider = spider ('Toronto', 'https://www.reddit.com/r/toronto', 'https://www.reddit.com')


