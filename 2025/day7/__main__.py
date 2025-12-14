#!/usr/bin/env python3
"""
Solution to day 7.
"""

from functools import cache
from typing import *
from re import sub, search

class Solution:
    def part1(self):
        result = 0
        with open('./input.txt', 'r') as f:
            start, grid = self.parse(f)
            positions = [0] * len(grid[0])
            positions[start] = 1
            for i in range(1, len(grid), 1):
                for j in range(len(grid[i])):
                    if grid[i][j] == '^' and positions[j]:
                        if j-1 >= 0:
                            positions[j-1] = 1
                        if j+1 < len(positions):
                            positions[j+1] = 1
                        positions[j] = 0
                        result += 1
        return result

    def part2(self):
        with open('./input.txt', 'r') as f:
            start, grid = self.parse(f)

            @cache
            def traverse(i, j):
                if j < 0 or j >= len(grid[i]):
                    return 0
                while i < len(grid):
                    if grid[i][j] == '^':
                        return traverse(i+1, j+1) + traverse(i+1,j-1)
                    i += 1
                return 1

            return traverse(1, start)

    def parse(self, f):
        grid = f.read().strip().split('\n')
        start = len(grid[0])//2
        return (start, grid)

if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
