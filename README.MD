[Solidity Docset](https://github.com/oschvr/solidity-dash)
=======================

This contains the docset generator for the last version of [Solidity](solidity.readthedocs.io) for Dash. Possibly for Zeal as well.

### How to

- Clone the repo and cd into it
- Executing `bash setup.sh` will:
  - Try to install dependencies (see below)
  - Fetch the **ethereum** repo
  - Go to docs dir and make them into html
  - Copy them to **solidity.docset**
  - Copy info.plist, dsidx and icon.svg into **solidity.docset**
  - Run `populate.py` to iterate through the htmls and fill the db.


#### Dependencies

**npm**, **pip** to install dependencies.

- [Sphinx](www.sphinx-doc.org), ethereum docs engine
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), to extract html tags.
- [svgexport](https://github.com/shakiba/svgexport), since icon is in svg format.

### To do

- Improve the html tag search in populate.py
- Generate the docset for the last 3 versions 
  - 0.4.19
  - 0.4.18
  - 0.4.17


### Author: [Oscar Chavez <oschvr>](http://twitter.com/oschvr)