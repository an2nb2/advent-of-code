#!/usr/bin/env python3
"""
Solution to day 19.
"""

from functools import cache
from typing import *
from re import sub, search
from collections import deque
from heapq import heappop, heappush

class Solution:
    def part1(self):
        result = 0
        grid, start, end = self._readfile()
        visits, path = self._best(grid, start, end)
        for i, j in path:
            for di, dj in self._moves(2):
                ii = i + di
                jj = j + dj
                if (ii, jj) in visits and (visits[(ii, jj)] - visits[(i, j)] - 2) >= 100:
                    result += 1
        return result

    def part2(self):
        result = 0
        grid, start, end = self._readfile()
        visits, path = self._best(grid, start, end)
        for i, j in path:
            for di, dj in self._moves(20):
                ii = i + di
                jj = j + dj
                dist = abs(di) + abs(dj)
                if (ii, jj) in visits and (visits[(ii, jj)] - visits[(i, j)] - dist) >= 100:
                    result += 1
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
            return (grid, start, end)

    def _best(self, grid, start, end):
        q, visits, bestpath = deque(), {start: 0}, []
        q.append((start, [start]))
        while len(q) > 0:
            (i, j), path = q.popleft()
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ii = i + di
                jj = j + dj
                if grid[ii][jj] == '#' or (ii, jj) in visits:
                    continue
                visits[(ii, jj)] = visits[(i, j)] + 1
                if (ii, jj) != end:
                    q.append(((ii, jj), path + [(ii, jj)]))
                else:
                    bestpath = path
        return visits, bestpath

    def _moves(self, cheats):
        moves = set()
        for di in range(-cheats, cheats+1):
            for dj in range(-cheats, cheats+1):
                if (abs(di)+abs(dj)) > cheats or (di, dj) in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]:
                    continue
                moves.add((di, dj))
        return moves



if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
