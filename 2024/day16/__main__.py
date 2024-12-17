#!/usr/bin/env python3
"""
Solution to day 16.
"""

from functools import cache
from typing import *
from re import sub, search
from heapq import heappop, heappush
from math import inf


class Solution:
    def part1(self):
        result = inf
        grid, start, end = self._readfile()
        visits = self._traverse(grid, start, end)
        for (p, d), (cost, _) in visits.items():
            if p == end:
                result = min(result, cost)
        return result

    def part2(self):
        result = 0
        grid, start, end = self._readfile()
        visits = self._traverse(grid, start, end)
        for (p, d), (cost, path) in visits.items():
            if p == end:
                result += len(path)
        return result

    def _readfile(self):
        with open('./input.txt', 'r') as f:
            grid, start, end = [], None, None
            for l in f.read().strip().split('\n'):
                grid.append(list(l))
                if 'S' in grid[-1]:
                    start = (len(grid)-1, grid[-1].index('S'))
                if 'E' in grid[-1]:
                    end = (len(grid)-1, grid[-1].index('E'))
            return grid, start, end

    def _traverse(self, grid, start, end):
        direction = (0, 1)
        q = [(0, start, direction, {start})]
        visits = {}
        while len(q) > 0:
            (cost, (i, j), direction, path) = heappop(q)
            prevpath = set()

            if ((i, j), direction) in visits:
                c, prevpath = visits[((i, j), direction)]
                if c < cost:
                    continue

            visits[(i, j), direction] = (cost, prevpath | path)
            if (i, j) == end:
                continue
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ii = i + di
                jj = j + dj
                if grid[ii][jj] == '#':
                    continue
                c = cost + 1
                if (di, dj) != direction:
                    c += 1000
                heappush(q, (c, (ii, jj), (di, dj), path | {(ii, jj)}))
        return visits


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
