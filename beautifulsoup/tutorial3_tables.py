import bs4 as bs
import urllib.request
import pandas as pd

# sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
# soup = bs.BeautifulSoup(sauce, 'lxml')

# # two ways to find the table
# table = soup.table
# table = soup.find('table')

# # find all the rows
# table_rows = table.find_all('tr')

# # find all the data in the rows
# for tr in table_rows:
#     td = tr.find_all('td')
#     row = [i.text for i in td]
#     print(row)

# # better way of doing this is with pandas
# dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface/', header=0)
# for df in dfs:
#     print(df)

sauce = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()
soup = bs.BeautifulSoup(sauce, 'xml')

for url in soup.find_all('loc'):
    print(url.text)