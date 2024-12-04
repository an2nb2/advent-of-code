#!/usr/bin/env python3
"""
Solution to day 4.
"""

from functools import cache
from typing import *
from re import sub, search

class Solution:
    def part1(self):
        result = 0
        grid = self._readfile()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 'X':
                    result += [
                        self._valid(grid, (i+1,j), (i+2,j), (i+3,j)),
                        self._valid(grid, (i-1,j), (i-2,j), (i-3,j)),
                        self._valid(grid, (i,j+1), (i,j+2), (i,j+3)),
                        self._valid(grid, (i,j-1), (i,j-2), (i,j-3)),
                        self._valid(grid, (i+1,j+1), (i+2,j+2), (i+3,j+3)),
                        self._valid(grid, (i-1,j-1), (i-2,j-2), (i-3,j-3)),
                        self._valid(grid, (i+1,j-1), (i+2,j-2), (i+3,j-3)),
                        self._valid(grid, (i-1,j+1), (i-2,j+2), (i-3,j+3)),
                    ].count(True)
        return result

    def part2(self):
        result = 0
        grid = self._readfile()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 'A':
                    if (self._valid(grid, (i+1,j+1), (i,j), (i-1,j-1)) or self._valid(grid, (i-1,j-1), (i,j), (i+1,j+1))) and \
                       (self._valid(grid, (i+1,j-1), (i,j), (i-1,j+1)) or self._valid(grid, (i-1,j+1), (i,j), (i+1,j-1))):
                        result += 1
        return result


    def _readfile(self):
        with open('./input.txt', 'r') as f:
            return f.read().strip().split('\n')

    def _valid(self, grid, m, a, s):
        for (i, j) in [m, a, s]:
            if i < 0 or j < 0:
                return False
            if i >= len(grid) or j >= len(grid[i]):
                return False
        return grid[m[0]][m[1]] + grid[a[0]][a[1]] + grid[s[0]][s[1]] == 'MAS'


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
