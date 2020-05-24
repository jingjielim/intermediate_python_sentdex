import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

# Find all paragraph tags
print(soup.find_all('p'))
# Print the title
print(soup.title)

for paragraph in soup.find_all('p'):
    # use .text to remove the p tags and the child tags
    print(paragraph.text)
# Just print out all the text on the page
print(soup.get_text())

# Find all the links
for url in soup.find_all('a'):
    # To get all the links use .get()
    print(url.get('href'))
