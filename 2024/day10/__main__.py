#!/usr/bin/env python3
"""
Solution to day 10.
"""

from functools import cache
from typing import *
from re import sub, search

class Solution:
    def part1(self):
        result = 0
        grid, heads = self._readfile()

        @cache
        def traverse(i, j):
            value = grid[i][j]
            if value == 9:
                return {(i, j)}
            tails = set()
            for i, j in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= i < len(grid) and 0 <= j < len(grid[i]):
                    if grid[i][j] == value+1:
                        tails |= traverse(i, j)
            return tails

        for i, j in heads:
            result += len(traverse(i, j))

        return result

    def part2(self):
        result = 0
        grid, heads = self._readfile()

        @cache
        def traverse(i, j):
            value = grid[i][j]
            if value == 9:
                return 1
            rating = 0
            for i, j in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= i < len(grid) and 0 <= j < len(grid[i]):
                    if grid[i][j] == value+1:
                        rating += traverse(i, j)
            return rating

        for i, j in heads:
            result += traverse(i, j)

        return result

    def _readfile(self):
        with open('./input.txt', 'r') as f:
            grid = []
            heads = []
            while True:
                l = f.readline()
                if not l:
                    break
                l = l.strip()
                grid.append([int(n) for n in list(l)])
                for j in range(len(grid[-1])):
                    if not grid[-1][j]:
                        heads.append((len(grid)-1, j))
            return grid, heads


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
