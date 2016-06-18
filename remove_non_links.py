from __future__ import print_function
import re

generate_links = re.compile('http://(.*)') #compile all http links
generate_links2 = re.compile('(.*)/eng/(.*)') #compile all english url
with open ("VAC\queue.txt", "r") as queued_list, open('newqueue.txt','w') as queued_list_updated:
    for links in queued_list:
        url = ""
        services_url = ""
        match = generate_links2.search(links)
        if match is not None:
            url = match.group()
            generate_links3 = re.compile('(.*)/services/(.*)') #compile all services links
            match2 = generate_links3.search(links)
            if match2 is not None:
                services_url = match2.group()
               # print services_url
                output = services_url + '\n '
                #print output
                queued_list_updated.write(output)
                with open('newqueue.txt') as unsolved_links, open('valid_url.txt','w') as valid_url:
                    cured_url = [line for line in unsolved_links.readlines() if 'search?' not in line]

                    for url in cured_url:
                        print(url, file=valid_url)