#!/usr/bin/python3

import sys

def ediv_convert(ediv):

    ediv = int(ediv, 16)
    print(ediv)

if __name__ == '__main__':
    ediv_convert(sys.argv[1])