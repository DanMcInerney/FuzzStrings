#!/usr/bin/env python

from urllib import quote

with open('ShortFuzzList.txt', 'r') as f:
    with open('ShortFuzzList-partial-URL-encoded.txt', 'w') as e:
        lines = f.readlines()
        for l in lines:
            print l
            encoded = quote(l)[:-3] #remove encoded newline
            e.write(encoded+'\n')
