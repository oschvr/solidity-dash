#!/usr/local/bin/python

import os, re, sqlite3
from bs4 import BeautifulSoup, NavigableString, Tag

conn = sqlite3.connect('solidity.docset/Contents/Resources/docSet.dsidx')
cur = conn.cursor()

try: cur.execute('DROP TABLE searchIndex;')
except: pass
cur.execute('CREATE TABLE searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT);')
cur.execute('CREATE UNIQUE INDEX anchor ON searchIndex (name, type, path);')

docPath = 'solidity.docset/Contents/Resources/Documents'

for docPage in os.listdir(docPath):
  if docPage.endswith('.html'):
    print 'docPage: %s' % docPage
    
    page = open(os.path.join(docPath, docPage)).read()
    soup = BeautifulSoup(page, 'lxml')

    any = re.compile('.*')
    for tag in soup.find_all('a', {'href': any}):
      name = tag.text.strip()
      if len(name) > 1:
        path = tag.attrs['href'].strip()
        if path != 'index.html':
          cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name, 'func', path))
          print 'name: %s, path: %s' % (name, path)


conn.commit()
conn.close()  
