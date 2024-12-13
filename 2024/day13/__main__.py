#!/usr/bin/env python3
"""
Solution to day 13.
"""

from functools import cache
from typing import *
from re import sub, search
import math

class Solution:
    def part1(self):
        result = 0
        for a, b, prize in self._readfile():
            costs = dict()
            def find(x, y, counts):
                if counts[0] > 100 or counts[1] > 100:
                    return False
                if x > prize[0] or y > prize[1]:
                    return False
                if (x, y) in costs:
                    return costs[(x, y)]
                if (x, y) == prize:
                    costs[(x, y)] = 0
                    return True
                costs[(x, y)] = math.inf
                if find(x+a[0], y+a[1], (counts[0]+1, counts[1])):
                    costs[(x, y)] = min(costs[(x, y)], costs[(x+a[0], y+a[1])] + 3)
                if find(x+b[0], y+b[1], (counts[0], counts[1]+1)):
                    costs[(x, y)] = min(costs[(x, y)], costs[x+b[0], y+b[1]] + 1)
                return costs[(x, y)] != math.inf
            if find(0, 0, (0, 0)):
                result += costs[(0, 0)]
        return result

    def part2(self):
        result = 0
        for a, b, prize in self._readfile():
            prize = (10000000000000+prize[0], 10000000000000+prize[1])
            acnt = (prize[0]*b[1] - prize[1]*b[0]) / (a[0]*b[1] - a[1]*b[0])
            bcnt = (a[0]*prize[1] - a[1]*prize[0]) / (a[0]*b[1] - a[1]*b[0])
            if int(acnt) == acnt and int(bcnt) == bcnt:
                result += int((acnt*3) + bcnt)
        return result

    def _readfile(self):
        def parsebutton(b):
            return tuple([int(i.split('+')[1].strip()) for i in b.split(':')[1].split(',')])

        def parseprize(b):
            return tuple([int(i.split('=')[1].strip()) for i in b.split(':')[1].split(',')])

        with open('./input.txt', 'r') as f:
            for block in f.read().strip().split('\n\n'):
                a, b, prize = block.split('\n')
                yield(
                    parsebutton(a),
                    parsebutton(b),
                    parseprize(prize)
                )

if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
