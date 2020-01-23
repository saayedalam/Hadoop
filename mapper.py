#!/usr/bin/env python
import sys
sys.path.append('.')

def mapper():
    # read standard input line by line
    for line in sys.stdin:
        # strip off extra whitespace, split on tab and put the data in an array
        data = line.strip().split("\t")

        if len(data)!= 6:
            print "bad data"
        else:
            date, time, store, item, cost, payment = data
            print '{0}\t{1}'.format(item, cost)

if __name__ == "__main__":
    mapper()
