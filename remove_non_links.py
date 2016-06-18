import re

generate_links = re.compile('http://(.*)')
with open ("VAC\queue.txt", "r") as queued_list, open('newqueue.txt','w') as queued_list_updated:
    for links in queued_list:
        url = ""
        match = generate_links.search(links)
        if match is not None:
            url = match.group()
            output = url + '\n'
            queued_list_updated.write(output)


