#!/usr/bin/env python3
"""
Solution to day 12.
"""

from functools import cache
from typing import *
from re import sub, search
from collections import deque

class Solution:
    def part1(self):
        result = 0
        grid, plots = self._readfile()
        total = 0
        for plot, subplots in plots.items():
            for positions in subplots:
                result += len(positions) * self._perimeter(grid, positions)
        return result

    def part2(self):
        result = 0
        grid, plots = self._readfile()
        total = 0
        for plot, subplots in plots.items():
            for positions in subplots:
                result += len(positions) * self._sides(grid, positions)
        return result

    def _readfile(self):
        with open('./input.txt', 'r') as f:
            grid = []
            plots = {}
            while True:
                l = f.readline()
                if not l:
                    break
                grid.append(list(l.strip()))
            visits = set()
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if (i, j) in visits:
                        continue
                    q = deque()
                    q.appendleft((i, j))
                    plot = grid[i][j]
                    if plot not in plots:
                        plots[plot] = []
                    plots[plot].append({(i, j)})
                    while len(q) > 0:
                        (ii, jj) = q.pop()
                        if (ii, jj) in visits:
                            continue
                        visits.add((ii, jj))
                        for (di, dj) in [(ii-1, jj), (ii+1, jj), (ii, jj-1), (ii, jj+1)]:
                            if 0 <= di < len(grid) and 0 <= dj < len(grid[di]):
                                if grid[di][dj] == grid[ii][jj]:
                                    q.appendleft((di, dj))
                                    plots[plot][-1].add((di, dj))
            return grid, plots

    def _perimeter(self, grid, positions):
        perimeter = 0
        for (i, j) in positions:
            for (di, dj) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if (di, dj) not in positions:
                    perimeter += 1
        return perimeter

    def _sides(self, grid, positions):
        sides = 0
        for (i, j) in positions:
            checks = [
                ((i-1, j-1), (i-1, j), (i, j-1)),
                ((i+1, j-1), (i+1, j), (i, j-1)),
                ((i+1, j+1), (i+1, j), (i, j+1)),
                ((i-1, j+1), (i-1, j), (i, j+1)),
            ]
            for check in checks:
                if check[1] not in positions and check[2] not in positions:
                    sides += 1
                if check[0] not in positions and check[1] in positions and check[2] in positions:
                    sides += 1
        return sides


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
