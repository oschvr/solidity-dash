#!/usr/bin/bash

sudo npm i svgexport -g
sudo pip install Sphinx BeautifulSoup

git clone https://github.com/ethereum/solidity
cd  solidity/docs
make html
cd ../../
mkdir -p solidity.docset/Contents/Resources/Documents
mv solidity/docs/_build/html/* solidity.docset/Contents/Resources/Documents
rm -rf solidity
cp Info.plist solidity.docset/Contents
cp docSet.dsidx solidity.docset/Contents/Resources
svgexport icon.svg solidity.docset/icon.png 16:
svgexport icon.svg solidity.docset/icon@2x.png 32:
python populate.py
tar --exclude='.DS_Store' -cvzf Solidity.tgz solidity.docset
