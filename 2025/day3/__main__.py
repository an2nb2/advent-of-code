#!/usr/bin/env python3
"""
Solution to day 3.
"""

from functools import cache
from typing import *
from re import sub, search

class Solution:
    def part1(self):
        result = 0
        with open('./input.txt', 'r') as f:
            for l in f.read().strip().split('\n'):
                result += self.solve(2, l)
        return result

    def part2(self):
        result = 0
        with open('./input.txt', 'r') as f:
            for l in f.read().strip().split('\n'):
                result += self.solve(12, l)
        return result

    def solve(self, k, l):
        l = list(l.strip())
        n = [None] * k
        for i in range(len(l)):
            for j in range(max(0, i-(len(l)-len(n))), len(n), 1):
                if n[j] is None or int(l[i]) > int(l[n[j]]):
                    n[j] = i
                    for k in range(j+1, len(n), 1):
                        n[k] = None
                    break
        rr = ''
        for i in n:
            rr += l[i]
        return int(rr)


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
