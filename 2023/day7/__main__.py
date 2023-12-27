#!/usr/bin/env python3
"""
Solution to day 7.
"""

from functools import cache, cmp_to_key
from typing import *
from re import sub, search

class Solution:
    def part1(self):
        mapping = {
            'A': 14,
            'K': 13,
            'Q': 12,
            'J': 11,
            'T': 10,
            '9': 9,
            '8': 8,
            '7': 7,
            '6': 6,
            '5': 5,
            '4': 4,
            '3': 3,
            '2': 2,
        }
        result = 0
        with open('./input.txt', 'r') as f:
            combs = self.parse(f)
            combs.sort(key=cmp_to_key(self.compare(mapping, False)))
            for i in range(len(combs)):
                result += combs[i][1] * (i+1)
        return result

    def part2(self):
        mapping = {
            'A': 14,
            'K': 13,
            'Q': 12,
            'T': 10,
            '9': 9,
            '8': 8,
            '7': 7,
            '6': 6,
            '5': 5,
            '4': 4,
            '3': 3,
            '2': 2,
            'J': 1,
        }
        result = 0
        with open('./input.txt', 'r') as f:
            combs = self.parse(f)
            combs.sort(key=cmp_to_key(self.compare(mapping, True)))
            for i in range(len(combs)):
                result += combs[i][1] * (i+1)
        return result

    def parse(self, f) -> List[tuple[str, int]]:
        result = []
        for l in f:
            c, b = l.strip().split(' ')
            result.append((c.strip(), int(b.strip())))
        return result

    def compare(self, mapping: dict[str, int], joker: bool):
        def c(c1: tuple[str, int], c2: tuple[str, int]) -> int:
            v1 = self.getCombValue(c1[0], joker)
            v2 = self.getCombValue(c2[0], joker)
            if v1 != v2:
                return v1-v2
            for i in range(len(c1[0])):
                if c1[0][i] != c2[0][i]:
                    return mapping[c1[0][i]] - mapping[c2[0][i]]
            return 0
        return c

    def getCombValue(self, c: str, joker: bool) -> int:
        cmap = dict()
        for s in c:
            if s not in cmap:
                cmap[s] = 0
            cmap[s] += 1
        vals = sorted(cmap.values())
        if joker and 'J' in cmap and len(vals) > 1:
            if cmap['J'] == vals[-1]:
                vals[-2] = vals[-2] + cmap['J']
            else:
                vals[-1] = vals[-1] + cmap['J']
            vals.remove(cmap['J'])
        return sum([v**2 for v in vals])

if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
