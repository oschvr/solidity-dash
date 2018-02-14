#!/usr/bin/bash

sudo pip install Sphinx

git clone https://github.com/ethereum/solidity
cd  solidity/docs
make html
cd ../../
mkdir -p solidity.docset/Contents/Resources/Documents
mv solidity/docs/_build/html/* solidity.docset/Contents/Resources/Documents
rm -rf solidity
cp Info.plist solidity.docset/Contents
cp docSet.dsidx solidity.docset/Contents/Resources
cp logo.svg solidity.docset
python populate.py 
