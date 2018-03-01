#!/usr/local/bin/python
# -*- coding: utf-8 -*-

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
   if not docPage.startswith('index'):
    if not docPage.startswith('genindex'):
      if not docPage.startswith('search'):
        print 'docPage: %s' % docPage
        
        page = open(os.path.join(docPath, docPage)).read()
        soup = BeautifulSoup(page, 'lxml')

        any = re.compile('.*')

        for tag_h1 in soup.find_all('h1'):
          name_h1 = tag_h1.text.strip().replace(u'¶', '')
          if len(name_h1) > 1:
            path_h1 = tag_h1.find('a').get('href')
            path_h1 = docPage + path_h1
            if path_h1 != 'index':
              cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name_h1, 'Section', path_h1))
              print 'name_h1: %s, path_h1: %s, type: Section' % (name_h1, path_h1)


        for tag_h2 in soup.find_all('h2'):
          name_h2 = tag_h2.text.strip().replace(u'¶', '')
          if len(name_h2) > 1 and tag_h2.find('a') > 1:
            path_h2 = tag_h2.find('a').get('href')
            path_h2 = docPage + path_h2
            if path_h2 != 'index.html':
              if name_h2 != 'Table Of Contents':
                cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name_h2, 'Guide', path_h2))
                print 'name_h2: %s, path_h2: %s, type: Guide' % (name_h2, path_h2) 


        for tag_h3 in soup.find_all('h3'):
          name_h3 = tag_h3.text.strip().replace(u'¶', '')
          if len(name_h3) > 1 and tag_h3.find('a') > 1:
            path_h3 = tag_h3.find('a').get('href')
            path_h3 = docPage + path_h3
            if path_h3 != 'index.html':
              if name_h3 != 'Table Of Contents': 
            
                cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name_h3, 'Guide', path_h3))
                print 'name_h3: %s, path_h3: %s, type: Guide' % (name_h3, path_h3)      


conn.commit()
conn.close() 


print "\n DONE "
print "\n Author: oschvr <os@oscvhr.com> \n" 
