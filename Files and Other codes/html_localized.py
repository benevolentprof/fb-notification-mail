import urllib

url =[]
with open("validurl2.txt", "r") as file:
    for row in file:
        new_list = row.rstrip()
        url.append(new_list)
print url

def create_html_file(url, html_file_name):
    sock = urllib.urlopen(url)
    htmlSource = sock.read()
    sock.close()
    with open(html_file_name, "w") as file_out:
        return file_out.write(htmlSource)

disabilities = create_html_file("http://www.veterans.gc.ca/eng/services/after-injury/disability-benefits/benefits-determined/table-of-disabilities/ch-04-2006", "ch4disabilities.xml")