#!/usr/bin/env python3
"""
Solution to day 6.
"""

from functools import cache, reduce
from typing import *
from re import sub, search

class Solution:
    def part1(self):
        with open('./input.txt', 'r') as f:
            lines = f.read().strip().split('\n')
            grid = []
            for i in range(len(lines)):
                line = list(filter(lambda x: x != '', lines[i].strip().split(' ')))
                for j in range(len(line)):
                    if j == len(grid):
                        grid.append([])
                    if line[j] in ['+', '*']:
                        grid[j].insert(0, line[j])
                    else:
                        grid[j].append(int(line[j]))
            return self.reduce(grid)

    def part2(self):
        with open('./input.txt', 'r') as f:
            lines = f.read().strip().split('\n')
            grid = [[]]
            k = 0
            for j in range(max([len(l) for l in lines])):
                line = ''
                for i in range(len(lines)):
                    if j < len(lines[i]):
                        line += lines[i][j]
                line = line.strip()
                if line:
                    if line[-1] in ['*', '+']:
                        grid[k].append(line[-1])
                        line = line[:-1]
                    grid[k].append(int(line.strip()))
                else:
                    k += 1
                    grid.append([])
            return self.reduce(grid)

    def reduce(self, grid):
        result = 0
        for r in grid:
            result += reduce(lambda x, y: x * y if r[0] == '*' else x + y, r[1:])
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
