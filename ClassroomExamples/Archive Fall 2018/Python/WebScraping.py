
import urllib
from bs4 import BeautifulSoup

# Fetch the html file


response = urllib.request.urlopen('https://www.amazon.com/dp/B0792KTHKJ/ref=ods_gw_d_cmdw_dnut_aucc_1127?pf_rd_p=984825d7-7af6-44a5-953c-1d5e3c0af1f5&pf_rd_r=N7S1PKSXRX94TFDMR7XH')
html_doc = response.read()

# Parse the html file
soup = BeautifulSoup(html_doc, "html.parser")

# Format the parsed html file
strhtm = soup.prettify()

# Print the first few characters
# print (strhtm[:225])
for x in soup.find("span",{"id":"priceblock_dealprice"}): print(x.string)