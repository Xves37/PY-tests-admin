from bs4 import BeautifulSoup as bs

with open('src/index.html', encoding='utf-8') as f:
    page = f.read()
    f.close()

soup = bs(page, 'html.parser')

print(soup.body)
soup.body.insert(len(soup.body), 'test')
print(soup)
