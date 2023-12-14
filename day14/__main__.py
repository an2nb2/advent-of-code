#!/usr/bin/env python3
"""
Solution to day 14.
"""

from functools import cache
from typing import *
from re import sub, search

class Solution:
    def part1(self):
        result = 0
        with open('./input.txt', 'r') as f:
            field = [list(s) for s in f.read().strip().split('\n')]
            field = self.tilt(field)
            result = self.count(field)
        return result

    def part2(self):
        result = 0
        with open('./input.txt', 'r') as f:
            field = [list(s) for s in f.read().strip().split('\n')]
            cycles = dict()
            k = 0
            until = 1000000000
            cycle = 0
            while k < until:
                # nord
                field = self.tilt(field)
                # west
                field = zip(*field)
                field = self.tilt(field)
                field = list(zip(*field))
                # south
                field = field[::-1]
                field = self.tilt(field)
                field = field[::-1]
                # east
                field = list(zip(*field))[::-1]
                field = self.tilt(field)
                field = list(zip(*field[::-1]))
                if not cycle:
                    key = ':'.join(''.join(l) for l in field)
                    if key not in cycles:
                        cycles[key] = k
                    else:
                        cycle = k - cycles[key]
                        until = (until - k) % cycle
                        k = 0
                k += 1

            result = self.count(field)
        return result

    def tilt(self, field: List[List[str]]):
        positions = dict()
        field = [list(f) for f in field]

        for i in range(len(field)):
            for j in range(len(field[i])):
                if field[i][j] == '.':
                    continue

                if field[i][j] == '#':
                    positions[(i, j)] = field[i][j]
                    continue

                k = i-1
                while k >= 0:
                    if (k, j) in positions:
                        break
                    k -= 1

                positions[(k+1, j)] = field[i][j]
                if k+1 != i:
                    field[k+1][j] = field[i][j]
                    field[i][j] = '.'
        return field

    def count(self, field: List[List[str]]) -> int:
        result = 0
        for i in range(len(field)):
            for j in range(len(field[i])):
                if field[i][j] == 'O':
                    result += len(field)-i
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
