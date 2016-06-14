"""create a class to take a look at HTML and sift through it and find all the links/a tags"""
from HTMLParser import HTMLParser
import urlparse


class linkFinder(HTMLParser):

    def __init__(self, baseURL, pageURL):
        super(type(self),self).__init__()
        self.reset()
        self.baseURL = baseURL
        self.pageURL = pageURL
        self.links = set() #just to store in set

    def handle_starttag(self, tag, attrs):
        if tag == 'a': #whenever we come across a link
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = urlparse.urljoin(self.baseURL, value) #convert partial URL into its URL
                    self.links.add(url) #add a properly formatted URL in a set of links

    def pageLinks(self):
        return self.links #create a linkfinder project to feed it into a website and once we've gathered links in pageLinks


    def error(self,message):
        pass

#finder = linkFinder()
#finder.feed('https://www.reddit.com/r/toronto', 'https://www.reddit.com')

