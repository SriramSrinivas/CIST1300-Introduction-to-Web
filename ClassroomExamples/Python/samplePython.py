
import urllib
from bs4 import BeautifulSoup    

# Fetch the html file


response = urllib.request.urlopen('https://apps.sarpy.com/sarpyproperty/pdisplay3.aspx?locid=010416110')
html_doc = response.read()

# Parse the html file
soup = BeautifulSoup(html_doc, "html.parser")

# Format the parsed html file
strhtm = soup.prettify()

# Print the first few characters
print (strhtm)

htmlTags = soup.find_all("b")

for eachTag in htmlTags:
    eachTag.attrs["id"] = htmlTags.index(eachTag)

# print(htmlTags)

with open("out.html", "w") as saveFile:
    saveFile.write(str(htmlTags))

test=str(htmlTags)
print(test.find("521"))
#for x in soup.find("b",{"id":"512"}): print(x.string)