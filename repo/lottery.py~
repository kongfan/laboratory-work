#! /usr/bin/env python
# -*- coding: utf-8 -*_

"""
    lottery
    ~~~~~~~

    统计福利彩票快三中各组号码出现的概率,回报率以及单号出现频率等.

    :copyright:(c) 2014 by kongfan.
    :license MIT, see LICENSE for more details.
"""

#TODO
list_theoretical = []
list_actual = [80, 40, 25, 16, 12, 10, 9, 9, 10, 12, 16, 25, 40, 80]

list = []
for a in range(1,7):
	for b in range(1,7):
		for c in range(1,7):
			s = a + b + c
			list.append(s)
print len(list)

for i in range(4,18):
	print i, list.count(i)
	m = list.count(i)
	list_theoretical.append(m)
	list_actual = [80, 40, 25, 16, 12, 10, 9, 9, 10, 12, 16, 25, 40, 80]

print len(list_theoretical)
print len(list_actual)
print list_theoretical
print list_actual

for n in range(0,14):
	print n+4,list_actual[n]*list_theoretical[n]
