#!/usr/bin/env python3
"""
Solution to day 18.
"""

from __future__ import annotations
from typing import *
from collections import deque

class Solution:
    def part1(self):
        result = 0
        with open('./input.txt', 'r') as f:
            grid = self.buildgrid(self.parsefile(f))
            self.flood_fill(grid)
            for r in grid:
                for v in r:
                    if v in {'.', '#'}:
                        result += 1
        return result

    def part2(self):
        result = 0
        dmap = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
        with open('./input.txt', 'r') as f:
            data = self.parsefile(f)
            i, j = 0, 0
            coordinates = []
            border = 0
            for k in range(len(data)):
                (_, _, h) = data[k]
                s = int(h[1:-1], 16)
                (di, dj) = self.nextdir(dmap[h[-1]])
                i += di * s
                j += dj * s
                coordinates.append((i, j))
                border += s
            result = self.shoelace(coordinates) + border // 2 + 1
        return result

    def parsefile(self, f: file) -> List[[str, int, str]]:
        r = []
        for l in f:
            d, s, c = l.strip().split(' ')
            r.append((d, int(s), str(c[1:-1])))
        return r

    def buildgrid(self, data: List[tuple[str, int, str]]) -> List[List[str]]:
        grid = [['.'] * 1000 for _ in range(1000)]
        i, j = 500, 500
        imin, imax, jmin, jmax = 5, 5, 5, 5
        for (d, s, _) in data:
            (di, dj) = self.nextdir(d)
            for _ in range(s):
                i += di
                j += dj
                imin = min(imin, i)
                imax = max(imax, i)
                jmin = min(jmin, j)
                jmax = max(jmax, j)
                grid[i][j] = '#'
        grid = grid[imin:imax+1]
        for i in range(len(grid)):
            grid[i] = grid[i][jmin:jmax+1]
        return grid

    def nextdir(self, d: str) -> (int, int):
        match d:
            case 'R':
                return (0, 1)
            case 'L':
                return (0, -1)
            case 'D':
                return (1, 0)
            case 'U':
                return (-1, 0)

    def flood_fill(self, grid: List[List[str]]):
        borders = sum([
            [(0, j) for j in range(len(grid[0]))],
            [(i, len(grid[i])-1) for i in range(1, len(grid), 1)],
            [(len(grid)-1, j) for j in range(len(grid[-1])-1)],
            [(i, 0) for i in range(1, len(grid)-1, 1)],

        ], [])
        for (i, j) in borders:
            if grid[i][j] in {'#', '0'}:
                continue
            q = deque()
            q.append((i, j))
            while len(q) > 0:
                (i, j) = q.popleft()
                for (ii, jj) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if ii < 0 or ii >= len(grid) or jj < 0 or jj >= len(grid[ii]):
                        continue
                    if grid[ii][jj] in {'#', '0'}:
                        continue
                    grid[ii][jj] = '0'
                    q.append((ii, jj))

    def shoelace(self, coordinates: List[tuple[int, int]]) -> int:
        r = 0
        for i in range(len(coordinates)-1):
            r += (coordinates[i][0] * coordinates[i+1][1]) - (coordinates[i][1] * coordinates[i+1][0])
        return abs(r) // 2


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
