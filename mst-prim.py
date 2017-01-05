#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'siyadong.xiong'

from heapq import *

def build_graph(filename):
    with open(filename, 'r') as f:
        n_vertex, n_edges = map(int, f.readline().rstrip().split(' '))

        g = [None] + [set([]) for _ in range(n_vertex)]

        cost_lookup = {}

        for edge in f:
            u, v, cost = map(int, edge.rstrip().split(' '))

            cost_lookup[(u, v)] = cost
            cost_lookup[(v, u)] = cost
            g[u].add(v)
            g[v].add(u)

    return g, cost_lookup

def mst_prims(g, cost_lookup):
    mst = []
    start = 1

    # init
    key = [float('inf') for _ in range(len(g))]
    key[start] = 0

    pq = []
    for v in g[start]:
        edge = (start, v)
        heappush(pq, (cost_lookup[edge], edge))

    visited = set([start])
    while len(visited) < len(g) - 1:
        _, edge = heappop(pq)

        _to = edge[1]
        if _to in visited:
            continue

        mst.append(edge)
        visited.add(_to)

        for neighbor in g[_to]:
            if neighbor not in visited:
                new_edge = (_to, neighbor)
                heappush(pq, (cost_lookup[new_edge], new_edge))

    return mst

if __name__ == '__main__':
    g, cost_lookup = build_graph('edges.txt')
    mst = mst_prims(g, cost_lookup)
    cost = 0
    for edge in mst:
        cost += cost_lookup[edge]
    print cost
    print mst

