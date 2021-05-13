#!/usr/bin/python3

import sys

def erand_convert(erand):

    erand_str = erand
    erand_list = erand_str.split(',')
    erand_list = erand_list[::-1]
    erand_str = ''.join(erand_list)
    print(erand_str)
    rand = int(erand_str, 16)
    print(rand)

if __name__ == '__main__':
    erand_convert(sys.argv[1])
