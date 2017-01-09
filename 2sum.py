#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'siyadong.xiong'

from bisect import bisect_left, bisect_right

def two_sum(filename, t_range=(-10000,10000)):
    with open(filename, 'r') as f:
        data = [int(line.rstrip()) for line in f]
    data.sort()

    s = set([])
    for num1 in data:
        lo = bisect_left(data, t_range[0] - num1)
        hi = bisect_right(data, t_range[1] - num1)
        for num2 in data[lo:hi]:
            s.add(num1 + num2)

    return len(s)


if __name__ == '__main__':
    t = two_sum('2sum.txt')
    print t
