from html_patterns import *


def search_create(header, items, path):
    f = open(path, 'w', encoding='utf-8')
    f.write(search_header(header))

    for item in items:
        f.write(search_item(item))

    f.write(search_footer())
    f.close()
