#!/usr/bin/env python3
"""
Solution to day 1.
"""

from functools import cache
from typing import *
from re import sub, search


class Solution:
    def part1(self):
        result = 0
        ids1, ids2 = [], []
        for n1, n2 in self._readfile():
            ids1.append(n1)
            ids2.append(n2)
        ids1 = sorted(ids1)
        ids2 = sorted(ids2)
        for i in range(len(ids1)):
            result += abs(ids1[i] - ids2[i])
        return result

    def part2(self):
        result = 0
        ids, repeats = [], dict()
        for n1, n2 in self._readfile():
            ids.append(n1)
            if n2 not in repeats:
                repeats[n2] = 0
            repeats[n2] += 1

        for i in ids:
            if i in repeats:
                result += i * repeats[i]

        return result


    def _readfile(self):
        with open('./input.txt', 'r') as f:
            while True:
                l = f.readline()
                if not l:
                    break
                n1, n2 = l.strip().split('   ')
                n1, n2 = int(n1), int(n2)
                yield(n1, n2)


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
