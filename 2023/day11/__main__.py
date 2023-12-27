#!/usr/bin/env python3
"""
Solution to day 11.
"""

from functools import cache
from typing import *
from re import sub, search
from collections import deque

class Solution:
    def part1(self):
        result = 0
        with open('./input.txt', 'r') as f:
            field = f.read().strip().split('\n')
            expansions = self.expansions(field)
            galaxies = []
            for i in range(len(field)):
                for j in range(len(field[i])):
                    if field[i][j] == '#':
                        galaxies.append((i, j))
            for i in range(len(galaxies)):
                for j in range(i+1, len(galaxies), 1):
                    result += self.shortest(galaxies[i], galaxies[j], expansions, 2)
        return result

    def part2(self):
        result = 0
        with open('./input.txt', 'r') as f:
            field = f.read().strip().split('\n')
            expansions = self.expansions(field)
            galaxies = []
            for i in range(len(field)):
                for j in range(len(field[i])):
                    if field[i][j] == '#':
                        galaxies.append((i, j))
            for i in range(len(galaxies)):
                for j in range(i+1, len(galaxies), 1):
                    result += self.shortest(galaxies[i], galaxies[j], expansions, 1000000)
        return result

    def expansions(self, field: List[str]) -> tuple[set[int], set[int]]:
        h, v = set(), set()
        for i in range(len(field)):
            if field[i].find('#') < 0:
                h.add(i)
        for j in range(len(field[0])):
            if all([field[i][j] == '.' for i in range(len(field))]):
                v.add(j)
        return (h, v)

    def shortest(self, source: tuple[int, int], target: tuple[int, int], expansions: tuple[set[int], set[int]], scale: int) -> int:
        dimax = max(source[0], target[0])
        dimin = min(source[0], target[0])
        di = dimax - dimin

        djmax = max(source[1], target[1])
        djmin = min(source[1], target[1])
        dj = djmax - djmin

        iscale = len(expansions[0].intersection({i for i in range(dimin, dimax, 1)}))
        di += iscale * (scale-1)

        jscale = len(expansions[1].intersection({j for j in range(djmin, djmax, 1)}))
        dj += jscale * (scale-1)

        return di + dj


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
