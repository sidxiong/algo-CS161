#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'siyadong.xiong'

def read_data(filename):
    with open(filename, 'r') as f:
        n = f.readline().rstrip()
        _ = f.readlines()
        weight_and_length = [s.rstrip().split(' ') for s in _]
    return n, map(lambda x: (int(x[0]), int(x[1])), weight_and_length)


def weighted_time(weight_and_length):
    w, _l = zip(*weight_and_length)

    l, x = [], 0
    for elem in _l:
        x += elem
        l.append(x)

    return sum([x[0]*x[1] for x in zip(w, l)])

if __name__ == '__main__':
    n, weight_and_length = read_data('jobs.txt')

    jobs_schedule_by_diff = sorted(weight_and_length,
            cmp=lambda x, y: -cmp(x[0]-x[1], y[0]-y[1]) if x[0]-x[1] != y[0]-y[1] 
                                                        else -cmp(x[0], y[0]))
    jobs_schedule_by_ratio = sorted(weight_and_length,
            cmp=lambda x, y: -cmp(float(x[0])/x[1], float(y[0])/y[1]))

    print weighted_time(jobs_schedule_by_diff)
    print weighted_time(jobs_schedule_by_ratio)



