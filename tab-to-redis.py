#!/usr/bin/env python
#-*- coding: utf-8 -*-
u"""Convert TAB-separated data into redis SET commands
"""
import sys

def tab_to_redis(handle):
    for line in handle:
        key, val = line.split("\t", 1)
        sys.stdout.write("*%d\r\n$%d\r\nSET\r\n$%d\r\n%s\r\n$%d\r\n%s\r\n" % (3, 3, len(key), key, len(val), val))

def test():
    pass

def main():
    try:
        if sys.argv[1] == "test":
            test()
            exit
    except IndexError: pass
    tab_to_redis(sys.stdin)


if __name__ == "__main__":
    main()

