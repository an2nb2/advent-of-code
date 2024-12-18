#!/usr/bin/env python3
"""
Solution to day 18.
"""

from functools import cache
from typing import *
from re import sub, search
from collections import deque

class Solution:
    width = 71
    firstBytes = 1024

    def part1(self):
        corrbytes = self._readfile()
        dists = self._calculateDists(corrbytes[:self.firstBytes])
        return dists[(self.width-1, self.width-1)]

    def part2(self):
        corrbytes = self._readfile()
        i = self.firstBytes
        dists = self._calculateDists(corrbytes[:i])
        while (self.width-1, self.width-1) in dists:
            i += 1
            dists = self._calculateDists(corrbytes[:i])
        return corrbytes[i-1]

    def _readfile(self):
        with open('./input.txt', 'r') as f:
            return [tuple([(int(c)) for c in cs.split(',')]) for cs in f.read().strip().split()]

    def _calculateDists(self, corrbytes):
        grid = [[0] * self.width for _ in range(self.width)]
        for (x, y) in corrbytes:
            grid[y][x] = 1
        q = deque()
        q.append((0, 0))
        dists = {(0, 0): 0}
        while len(q) > 0:
            i, j = q.popleft()
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ii = i + di
                jj = j + dj
                if 0 <= ii < len(grid) and 0 <= jj < len(grid[ii]):
                    if grid[ii][jj] == 1:
                        continue
                    if (ii, jj) in dists:
                        continue
                    dists[(ii, jj)] = dists[(i, j)] + 1
                    q.append((ii, jj))
        return dists


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
