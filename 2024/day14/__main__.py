#!/usr/bin/env python3
"""
Solution to day 14.
"""

from functools import cache
from typing import *
from re import sub, search
from functools import reduce
from operator import mul, concat
from math import inf

class Solution:
    def part1(self):
        xsize, ysize = 101, 103
        iterations = 100
        q = {(0, 0): 0, (0, 1): 0, (1, 0): 0, (1, 1): 0}
        for (px, py), (vx, vy) in self._readfile():
            px = (px + iterations * vx) % xsize
            py = (py + iterations * vy) % ysize
            if px == xsize // 2:
                continue
            if py == ysize // 2:
                continue
            qx = 0 if (xsize // 2) < px else 1
            qy = 0 if (ysize // 2) < py else 1
            q[(qx, qy)] += 1
        return reduce(mul, q.values())

    def part2(self):
        result = 0
        xsize, ysize = 101, 103
        points = []

        for p, v in self._readfile():
            points.append([list(p), list(v)])

        treepoints = None
        minlevel = (inf, 0)
        for _ in range(50000):
            q = {(0, 0): 0, (0, 1): 0, (1, 0): 0, (1, 1): 0}
            for i in range(len(points)):
                (px, py), (vx, vy) = points[i][0], points[i][1]
                px = (px + vx) % xsize
                py = (py + vy) % ysize
                points[i][0] = [px, py]
                qx = 0 if (xsize // 2) < px else 1
                qy = 0 if (ysize // 2) < py else 1
                q[(qx, qy)] += 1
            result += 1
            level = reduce(mul, q.values())
            if level < minlevel[0]:
                minlevel = (level, result)
                treepoints = [(p[0][0], p[0][1]) for p in points]

        tree = [[0]*ysize for _ in range(xsize)]
        for (px, py) in treepoints:
            tree[px][py] += 1
        for x in tree:
            print(reduce(concat, ['.' if not y else '#' for y in x]))

        return minlevel[1]

    def _readfile(self):
        with open('./input.txt', 'r') as f:
            while True:
                l = f.readline()
                if not l:
                    break
                p, v = l.strip().split(' ')
                px, py = p.split('=')[1].split(',')
                vx, vy = v.split('=')[1].split(',')
                yield((int(px), int(py)), (int(vx), int(vy)))


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
