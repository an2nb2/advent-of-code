#!/usr/bin/env python3
"""
Solution to day 8.
"""

from functools import cache
from typing import *
from re import sub, search

class Solution:
    def part1(self):
        grid, anthenas = self._readfile()
        antinodes = set()
        for key, positions in anthenas.items():
            for i in range(len(positions)-1):
                for j in range(i+1, len(positions)):
                    antinodes |= self._countAntinodes(grid, positions[i], positions[j], False)
        return len(antinodes)

    def part2(self):
        grid, anthenas = self._readfile()
        antinodes = set()
        for key, positions in anthenas.items():
            for i in range(len(positions)-1):
                for j in range(i+1, len(positions)):
                    antinodes |= self._countAntinodes(grid, positions[i], positions[j], True)
                    antinodes.add(positions[i])
                    antinodes.add(positions[j])
        return len(antinodes)

    def _readfile(self):
        with open('./input.txt', 'r') as f:
            grid = []
            anthenas = dict()
            while True:
                l = f.readline()
                if not l:
                    break
                grid.append(list(l.strip()))
                for j in range(len(grid[-1])):
                    if grid[-1][j] != '.':
                        if grid[-1][j] not in anthenas:
                            anthenas[grid[-1][j]] = []
                        anthenas[grid[-1][j]].append((len(grid)-1, j))
            return grid, anthenas

    def _countAntinodes(self, grid, p1, p2, part2):
        antinodes = set()
        di = abs(p1[0]-p2[0])
        dj = p1[1]-p2[1]

        for (i, di), (j, dj) in [
                ((min(p1[0], p2[0]), -di), (min(p1[1], p2[1]) if dj < 0 else max(p1[1], p2[1]), dj)),
                ((max(p1[0], p2[0]), di), (max(p1[1], p2[1]), -dj) if dj < 0 else (min(p1[1], p2[1]), -dj)),
        ]:
            i += di
            j += dj
            while 0 <= i < len(grid) and 0 <= j < len(grid[i]):
                antinodes.add((i, j))
                i += di
                j += dj
                if not part2:
                    break
        return antinodes

    def _print(self, grid, antinodes):
        for i in range(len(grid)):
            l = ''
            for j in range(len(grid[i])):
                if (i, j) in antinodes:
                    l += '#'
                else:
                    l += grid[i][j]
            print(l)


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
