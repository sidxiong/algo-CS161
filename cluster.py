#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'siyadong.xiong'

class UF(object):
    def __init__(self, n):
        self.n_cluster = n
        self.data = [None] + [i+1 for i in range(n)]
        self.size = [None] + [1 for i in range(n)]
    

    def union(self, u, v):
        root_u = self.root(u)
        root_v = self.root(v)

        if root_u != root_v:
            if self.size[root_u] < self.size[root_v]:
                self.data[root_u] = root_v
                self.size[root_v] += self.size[root_u]
            else:
                self.data[root_v] = root_u
                self.size[root_u] += self.size[root_v]
            self.n_cluster -= 1


    def is_connected(self, u, v):
        return self.root(u) == self.root(v)


    def union_if_not_connected(self, u, v):
        root_u = self.root(u)
        root_v = self.root(v)

        if root_u == root_v:
            return False

        if self.size[root_u] < self.size[root_v]:
            self.data[root_u] = root_v
            self.size[root_v] += self.size[root_u]
        else:
            self.data[root_v] = root_u
            self.size[root_u] += self.size[root_v]

        self.n_cluster -= 1

        return True


    def root(self, x):
        while self.data[x] != x:
            self.data[x] = self.data[self.data[x]]
            x = self.data[x]
        return x


def cluster_small(filename, k=4):
    if k == 1:
        return 0

    with open(filename, 'r') as f:
        n_nodes = int(f.readline().rstrip())
        _ = [line.rstrip().split(' ') for line in f]
        edges = [map(int, x) for x in _]
    edges.sort(key=lambda x: x[-1])

    uf = UF(n_nodes)
    for i, edge in enumerate(edges):
        u, v = edge[:-1]
        if uf.union_if_not_connected(u, v) and uf.n_cluster == k:
            i += 1
            break

    while i < len(edges):
        u, v, cost = edges[i]
        if not uf.is_connected(u, v):
            return cost
        i += 1

    return -1

def cluster_big(filename):
    with open(filename, 'r') as f:
        _, length = [int(x) for x in f.readline().rstrip().split(' ')]
        nodes = set([''.join(line.rstrip().split(' ')) for line in f])

    nodes_list = list(nodes)

    uf = UF(len(nodes_list)) # wtf, given nodes have duplicates!

    node_lookup = {node: i for i, node in enumerate(nodes_list)}

    for idx, _ in enumerate(nodes_list):
        if idx % 10000 == 0 and idx > 0:
            print 'idx ', idx

        ori_node = list(_)
        for i in range(length):
            for j in range(length):
                node = ori_node[:]
                node[i] = '1' if node[i] == '0' else '0'
                if i != j:
                    node[j] = '1' if node[j] == '0' else '0'
                flip = ''.join(node)
                if flip in node_lookup:
                    uf.union(idx + 1, node_lookup[flip] + 1)

    return uf.n_cluster


if __name__ == '__main__':
    cost = cluster_small('clustering1.txt')
    print 'cost: ', cost

    # cost = cluster_big('clustering_big.txt')
    # print 'cost: ', cost
