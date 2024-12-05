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
        rulesmap, pages = self._readfile()
        for p in pages:
            eligible = True
            prev = set()
            for n in p:
                if n in rulesmap:
                    if len(rulesmap[n].intersection(prev)) > 0:
                        eligible = False
                        break
                prev.add(n)
            if eligible:
                result += p[len(p)//2]
        return result

    def part2(self):
        result = 0
        rulesmap, pages = self._readfile()
        for page in pages:
            eligible = False
            pageset, prev = set(page), set()
            n = len(page)
            for p in page:
                if len(rulesmap[p].intersection(prev)) > 0:
                    eligible = True
                    break
                prev.add(p)
            if eligible:
                for p in page:
                    if len(rulesmap[p].intersection(pageset)) == n//2:
                        result += p
                        break
        return result

    def _readfile(self):
        with open('./input.txt', 'r') as f:
            rules, pages = f.read().strip().split('\n\n')
            pages = [list(map(int, p.split(','))) for p in pages.split('\n')]
            rules = [tuple(map(int, r.split('|'))) for r in rules.split('\n')]
            rulesmap = dict()
            for (b, a) in rules:
                if b not in rulesmap:
                    rulesmap[b] = set()
                rulesmap[b].add(a)
            return rulesmap, pages


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
