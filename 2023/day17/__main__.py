#!/usr/bin/env python3
"""
Solution to day 17.
"""

from __future__ import annotations
from functools import cache
from typing import *
from re import sub, search
from collections import deque
from enum import Enum
import heapq


class Direction(Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4


class Solution:
    def part1(self):
        with open('./input.txt', 'r') as f:
            grid = self.parse_grid(f)
            return self.mindist(grid)

    def part2(self):
        with open('./input.txt', 'r') as f:
            grid = self.parse_grid(f)
            return self.mindist(grid, True)

    def mindist(self, grid: List[List[int]], part2: bool = False) -> int:
        maxblocks = 10 if part2 else 3
        minblocks = 4 if part2 else 0

        target = (len(grid)-1, len(grid[-1])-1)
        dists = {}

        q = [(0, 0, 0, Direction.RIGHT.value, 0)]

        while len(q) > 0:
            (dist, i, j, d, r) = heapq.heappop(q)
            d = Direction(d)

            if (i, j, d, r) in dists:
                continue

            dists[(i, j, d, r)] = dist
            for (di, dj, dd, rr) in self.adjusted(d, r):
                ii = i+di
                jj = j+dj

                if ii < 0 or ii >= len(grid) or jj < 0 or jj >= len(grid[ii]):
                    continue
                if rr > maxblocks:
                    continue
                if dd != d and r < minblocks:
                    continue
                if (ii, jj, dd, rr) in dists:
                    continue

                heapq.heappush(q, (dist + grid[ii][jj], ii, jj, dd.value, rr))

        result = 2**64-1
        for (i, j, d, r) in dists.keys():
            if (i, j) == target and r >= minblocks:
                result = min(result, dists[(i, j, d, r)])
        return result

    def adjusted(self, d: Direction, r: int) -> List[tuple[int, int, Direction, int]]:
        match d:
            case Direction.UP:
                return [
                    (0, -1, Direction.LEFT, 1),
                    (0, 1, Direction.RIGHT, 1),
                    (-1, 0, d, r+1),
                ]
            case Direction.DOWN:
                return [
                    (0, -1, Direction.LEFT, 1),
                    (0, 1, Direction.RIGHT, 1),
                    (1, 0, d, r+1),
                ]
            case Direction.LEFT:
                return [
                    (-1, 0, Direction.UP, 1),
                    (1, 0, Direction.DOWN, 1),
                    (0, -1, d, r+1),
                ]
            case Direction.RIGHT:
                return [
                    (-1, 0, Direction.UP, 1),
                    (1, 0, Direction.DOWN, 1),
                    (0, 1, d, r+1),
                ]

    def parse_grid(self, f: file) -> List[List[int]]:
        return [[int(v) for v in l] for l in f.read().strip().split('\n')]


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
