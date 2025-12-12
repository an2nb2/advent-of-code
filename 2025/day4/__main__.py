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
        with open('./input.txt', 'r') as f:
            grid = self.parse(f)
            for i, j in self.traverse(grid):
                result += 1
        return result

    def part2(self):
        result = 0
        with open('./input.txt', 'r') as f:
            grid = self.parse(f)
            changed = True
            while changed:
                changed = False
                for i, j in self.traverse(grid):
                    result += 1
                    grid[i][j] = '.'
                    changed = True
            self.print(grid)
        return result

    def parse(self, f):
        l = f.readline().strip()
        grid = []
        while l:
            grid.append(list(l))
            l = f.readline().strip()
        return grid

    def traverse(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != '@':
                    continue
                total = 0
                dp = [
                    (-1, -1),
                    (-1, 0),
                    (-1, 1),
                    (0, 1),
                    (0, -1),
                    (1, -1),
                    (1, 0),
                    (1, 1),
                ]
                total = 0
                for di, dj in dp:
                    ii = i + di
                    jj = j + dj
                    if ii < 0 or ii >= len(grid) or jj < 0 or jj >= len(grid[ii]):
                        continue
                    if grid[ii][jj] == '@':
                        total += 1
                if total < 4:
                    yield(i, j)

    def print(self, grid):
        for l in grid:
            print(''.join(l))


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
