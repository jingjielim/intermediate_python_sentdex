import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

# # Get all the urls but we only want a specific set of urls in the nav bar
# nav = soup.nav

# for url in nav.find_all('a'):
#     print(url.get('href'))

# # Getting paragraph text from body
# body = soup.body
# for paragraph  in body.find_all('p'):
#     print(paragraph.text)

# Find the text by tag and class
for div in soup.find_all('div', class_='body'):
    print(div.text)