#!/usr/bin/env python3
"""
Solution to day 6.
"""

from functools import cache
from typing import *
from re import sub, search

class Solution:
    def part1(self):
        result = 0
        grid, start = self._readfile()
        visits = set()
        for current, _ in self._traverse(grid, start):
            visits.add(current)
        return len(visits)

    def part2(self):
        result = 0
        grid, start = self._readfile()
        visits = set()
        for current, _ in self._traverse(grid, start):
            visits.add(current)
        candidates = visits - {start}
        for c in candidates:
            visits = set()
            grid[c[0]][c[1]] = '#'
            for current, direction in self._traverse(grid, start):
                if (current, direction) in visits:
                    result += 1
                    break
                visits.add((current, direction))
            grid[c[0]][c[1]] = '.'
        return result

    def _traverse(self, grid, start):
        direction = (-1, 0)
        di, dj = start
        while di >= 0 and dj >= 0 and di < len(grid) and dj < len(grid[di]):
            yield((di, dj), direction)
            while len(grid) > di+direction[0] >= 0 and len(grid[di]) > dj+direction[1] >= 0 and grid[di+direction[0]][dj+direction[1]] == '#':
                if direction == (-1, 0):
                    direction = (0, 1)
                elif direction == (0, 1):
                    direction = (1, 0)
                elif direction == (1, 0):
                    direction = (0, -1)
                else:
                    direction = (-1, 0)
            di, dj = di+direction[0], dj+direction[1]

    def _readfile(self):
        grid = []
        start = (0, 0)
        with open('./input.txt', 'r') as f:
            while True:
                l = f.readline()
                if not l:
                    break
                l = l.strip()
                j = l.find('^')
                if j >= 0:
                    start = (len(grid), j)
                grid.append(list(l))
        return grid, start



if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
