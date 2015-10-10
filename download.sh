#!/bin/sh

wget https://www.gutenberg.org/cache/epub/29765/pg29765.txt

sed -f format.sed pg29765.txt > pg.txt
