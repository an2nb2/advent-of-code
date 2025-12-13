#!/usr/bin/env python3
"""
Solution to day 5.
"""

from functools import cache
from typing import *
from re import sub, search

class Solution:
    def part1(self):
        result = 0
        with open('./input.txt', 'r') as f:
            ranges, ids = self.parse(f)
            for iid in ids:
                for (fr, to) in ranges:
                    if iid >= fr and iid <= to:
                        result += 1
                        break
        return result

    def part2(self):
        result = 0
        with open('./input.txt', 'r') as f:
            ranges, _ = self.parse(f)
            ranges = sorted(ranges, key=lambda x: x[0])
            i = 0
            while i < len(ranges):
                j = i+1
                while j < len(ranges):
                    r1, r2 = ranges[i], ranges[j]
                    if r1[1] >= r2[0]:
                        ranges[i] = (r1[0], max(r1[1], r2[1]))
                        ranges.pop(j)
                    else:
                        j += 1
                i += 1
            for r in ranges:
                result += r[1]-r[0]+1
        return result

    def parse(self, f):
        ranges, ids = [], []
        _ranges, _ids = f.read().strip().split('\n\n')
        for r in _ranges.split('\n'):
            f, t = r.split('-')
            ranges.append((int(f), int(t)))
        ids = [int(_id) for _id in _ids.split('\n')]
        return (ranges, ids)


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
