#!/usr/bin/env python
# -*- coding: utf-8 -*-

for x in xrange(1, 11):
    for y in xrange(1, 11):
        print '%d * %d = %d' % (x, y, x * y)

for x in xrange(3):
    print "Numero: " + str(x)
    if x == 1:
        break

for x in xrange(3):
    print x
else:
    print 'Final x = %d' % (x)

string = "Hello World"

for x in string:
    print x

collection = ['hey', 5, 'd']

for x in collection:
    print x

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for lista in list_of_lists:
    for x in lista:
        print x

import time

# use time.time() on Linux

start = time.clock()
for x in range(10000000):
    pass
stop = time.clock()

print stop - start

start = time.clock()
for x in xrange(10000000):
    pass
stop = time.clock()

print stop - start
