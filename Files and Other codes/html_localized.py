"""html_localiyzed.py

    Paola Santiago
    12 July 2016


    input: file containing urls, one per line
    output: a directory of files containing local versions of the urls in the input file

    Strips off the http and domain prefix from URL
    Creates file name by subsituting underbars for backslashes
"""

import urllib

# specific run data here
directory = "data"
url_file = "validurl2.txt"
prefix = "http://www.veterans.gc.ca/eng/"

# grabs the data and saves it locally
def create_html_file(remote_url, html_file_name):
    sock = urllib.urlopen(remote_url)
    html_source = sock.read()
    sock.close()
    print html_source
    with open(html_file_name, "w") as file_out:
        return file_out.write(html_source)

# reads in the URLs from a file
url_list = []
with open(url_file, "r") as u_file:
    for row in u_file:
        line = row.rstrip()
        url_list.append(line)

# iterates over urls
for url in url_list:
    # create a file name
    start_index = len(prefix)
    file_name = url[start_index:]
    file_name = file_name.replace("/", "_")
    file_name = directory + "/" + file_name

    print file_name
    create_html_file(url, file_name)

