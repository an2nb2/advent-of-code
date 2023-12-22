#!/usr/bin/env python3
"""
Solution to day 21.
"""

from functools import cache
from typing import *
import numpy as np


def evaluate_quadratic_equation(points, x):
    # Fit a quadratic polynomial (degree=2) through the points
    coefficients = np.polyfit(*zip(*points), 2)

    # Evaluate the quadratic equation at the given x value
    result = np.polyval(coefficients, x)
    return round(result)


class Solution:
    def part1(self):
        result = 0
        with open('./input.txt', 'r') as f:
            grid = []
            start = (0, 0)
            for l in f:
                grid.append(list(l))
                sj = l.find('S')
                if sj > 0:
                    start = (len(grid)-1, sj)
            points = {start}
            steps = 64
            for i in range(steps):
                stops = set()
                for (i, j) in points:
                    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        ii = i + di
                        jj = j + dj
                        if not (0<=ii<len(grid) and 0<=jj<len(grid[ii])):
                            continue
                        if grid[ii][jj] == '#':
                            continue
                        stops.add((ii, jj))
                points = stops
            result = len(points)
        return result

    def part2(self):
        result = 0
        with open('./input.txt', 'r') as f:
            grid = []
            start = (0, 0)
            for l in f:
                grid.append(list(l.strip()))
                sj = l.find('S')
                if sj > 0:
                    start = (len(grid)-1, sj)
            points = {start}
            target = 26501365
            ivalues = []
            n, m = len(grid), len(grid[0])
            for k in range(1, n//2 + 2*n + 1):
                stops = set()
                for (i, j) in points:
                    for (di, dj) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        ii = i + di
                        jj = j + dj
                        if grid[ii%n][jj%m] == '#':
                            continue
                        stops.add((ii, jj))
                points = stops
                if k == (n//2) or k == (n//2 + n) or k == (n//2 + 2*n):
                    ivalues.append(len(points))
            def gauss_legendre():
                assert(len(ivalues) == 3)
                a0, a1, a2 = ivalues
                b0 = a0
                b1 = a1-a0
                b2 = a2-a1
                x = target // n
                return b0 + b1*x + (x*(x-1)//2)*(b2-b1)
            result = gl()
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
