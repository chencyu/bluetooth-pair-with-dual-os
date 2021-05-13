#!/usr/bin/python3

import sys

def ltk_convert(ltk):

    ltk_list = ltk.split(',')
    ltk = ''.join(ltk_list)
    ltk = ltk.upper()
    print(ltk)

if __name__ == '__main__':
    ltk_convert(sys.argv[1])