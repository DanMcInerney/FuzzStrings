#!/usr/bin/env python

from urllib import quote

with open('ShortFuzzList.txt', 'r') as f:
    with open('ShortFuzzList-full-URL-encoded.txt', 'w') as e:
        lines = f.readlines()
        for l in lines:
            print l
            encoded = "".join("%{:02x}".format(ord(c)) for c in l)
            e.write(encoded[:-3]+'\n')
