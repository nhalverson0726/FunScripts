#! python3
#lucky.py opens top results for search tem given in comand line argument

import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
#res = requests.get('http://google.com/search?q+' + ' '.join(sys.argv[1:]))
res = requests.get('https://www.google.com/search?q=' + 'butter')
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, features="html.parser")

# Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
soup.
