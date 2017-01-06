#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'siyadong.xiong'

def sort_and_count_inversion(filename):
    with open(filename, 'r') as f:
       nums = [int(x.rstrip()) for x in f]
    count = merge_sort(nums, 0, len(nums) - 1)
    return nums, count


def merge_sort(nums, lo, hi):
    if lo >= hi:
        return 0
    mid = lo + (hi - lo) / 2
    left = merge_sort(nums, lo, mid)
    right = merge_sort(nums, mid + 1, hi)
    curr = merge(nums, lo, mid, hi)
    return left + right + curr


def merge(nums, lo, mid, hi):
    inv = 0
    aux = [0] * (hi + 1 - lo)

    i, j = lo, mid+1

    for idx in range(len(aux)):
        if i <= mid and (j > hi or nums[i] < nums[j]):
            aux[idx] = nums[i]
            i += 1
        else:
            aux[idx] = nums[j]
            if i <= mid:
                inv += mid + 1 - i
            j += 1

    nums[lo:hi+1] = aux
    return inv


#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

def sort_and_count_comparison(filename, pivot_strategy='first'):
    with open(filename, 'r') as f:
       nums = [int(x.rstrip()) for x in f]
    count = quick_sort(nums, 0, len(nums) - 1, pivot_strategy)
    return nums, count


def quick_sort(nums, lo, hi, pivot_strategy):
    if lo >= hi:
        return 0
    if pivot_strategy == 'first':
    	pivot_idx = lo
    elif pivot_strategy == 'last':
    	pivot_idx = hi
    else:
    	mid = lo + (hi - lo) / 2
    	tmp_list = [(lo, nums[lo]), (mid, nums[mid]), (hi, nums[hi])]
    	tmp_list.sort(key=lambda t:t[1])
    	pivot_idx = tmp_list[1][0]


    idx = partition(nums, lo, hi, pivot_idx)
    left = quick_sort(nums, lo, idx - 1, pivot_strategy)
    right = quick_sort(nums, idx + 1, hi, pivot_strategy)
    return (hi - lo) + left + right


def partition(nums, lo, hi, pivot_idx):

    if pivot_idx != lo:
        nums[lo], nums[pivot_idx] = nums[pivot_idx], nums[lo]

    i = lo + 1
    for j in range(lo + 1, hi + 1):
    	if nums[j] < nums[lo]:
    		nums[i], nums[j] = nums[j], nums[i]
    		i += 1
    nums[lo], nums[i-1] = nums[i-1], nums[lo]
    return i-1


#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
if __name__ == '__main__':
    _, count = sort_and_count_comparison('QuickSort.txt')
    print count
    _, count = sort_and_count_comparison('QuickSort.txt', pivot_strategy='last')
    print count
    _, count = sort_and_count_comparison('QuickSort.txt', pivot_strategy='middle')
    print count
