#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'siyadong.xiong'

def build_graph(filename):
    g = []
    with open(filename, 'r') as f:
        lines = f.readlines()

    lines = [line.rstrip().split('\t') for line in lines]
    for line in lines:
        v, edge_and_weights = int(line[0]), line[1:]
        _ = [t.split(',') for t in edge_and_weights]
        edges = {int(edge): int(weight) for edge, weight in _}
        g.append((v, edges))
        
    return {node[0]: node[1] for node in g}

def find_shortest_path(graph, src=1):
    d = {n : float('inf') if n != src else 0 for n in graph.keys()}

    v_set = set([])
    q_set = {n for n in graph.keys()}

    while len(q_set) > 0:
        min_dis = float('inf')
        v_extracted = -1
        for v in q_set:
            dis = d[v]
            if dis < min_dis:
                min_dis = dis
                v_extracted = v

        v_set.add(v_extracted)
        q_set.remove(v_extracted)

        for neighbor, weight in graph[v_extracted].items():
            if d[neighbor] > d[v_extracted] + weight:
                d[neighbor] = d[v_extracted] + weight

    return d

if __name__ == '__main__':
    graph = build_graph('dijkstraData.txt')
    d = find_shortest_path(graph)
    des = '7,37,59,82,99,115,133,165,188,197'
    out = ','.join([ str(d[int(_des)]) for _des in des.split(',') ])
    print out

