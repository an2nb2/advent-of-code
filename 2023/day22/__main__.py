#!/usr/bin/env python3
"""
Solution to day 22.
"""

from __future__ import annotations
from functools import cache
from typing import *
from re import sub, search


class Point:
    x: int
    y: int
    z: int

    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z


class Brick:
    a: Point
    b: Point

    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b

    def bottom(self) -> int:
        return min(self.a.z, self.b.z)

    def top(self) -> int:
        return max(self.a.z, self.b.z)

    def length(self) -> int:
        return self.top() - self.bottom()

    def xyvals(self) -> tuple[int, int]:
        fx, tx = min(self.a.x, self.b.x), max(self.a.x, self.b.x)
        fy, ty = min(self.a.y, self.b.y), max(self.a.y, self.b.y)
        x, y = 0, 0
        for i in range(fx, tx+1, 1):
            x |= 1<<i
        for i in range(fy, ty+1, 1):
            y |= 1<<i
        return (x, y)


class Grid:
    levels: List[List[tuple[int, int]]]
    z: int

    def __init__(self, z: int):
        self.levels = []
        for _ in range(z):
            self.levels.append([])
        self.z = z

    def finalize(self, bricks: List[Brick]):
        bricks.sort(key = lambda b: b.bottom())
        for b in bricks:
            x, y = b.xyvals()
            while b.bottom() > 1 and all([not (x & _x and y & _y) for (_x, _y, _) in self.levels[b.bottom()-1]]):
                b.a.z -= 1
                b.b.z -= 1
            for i in range(b.bottom(), b.top()+1, 1):
                self.levels[i].append((x, y, b))

    def countFallen(self, dropped: set[tuple[int, int]], z: int) -> int:
        if not dropped:
            return 0
        _dropped = set()
        result = 0
        for (tx, ty, tb) in self.levels[z+1]:
            if all([not (tx & cx and ty & cy) for (cx, cy, cb) in self.levels[z] if id(cb) not in dropped]):
                if id(tb) not in dropped:
                    result += 1
                _dropped.add(id(tb))
        return result + self.countFallen(_dropped, z+1)

    def print(self):
        print('X:')
        for x in self.x[::-1]:
            print(format(x, f'#012b'))
        print('Y:')
        for y in self.y[::-1]:
            print(format(y, f'#012b'))


class Solution:
    def part1(self):
        result = 0
        with open('./input.txt', 'r') as f:
            grid, bricks = self.prepare(f)
            for i in range(len(bricks)):
                b = bricks[i]
                if b.top() >= grid.z-1 or not grid.levels[b.top()+1]:
                    result += 1
                else:
                    # This can definitely can be optimized and collisions can be
                    # calculated in grid finalize method.
                    valid = True
                    for (x, y, _) in grid.levels[b.top()+1]:
                        if all([not (x & _x and y & _y) for (_x, _y, _) in grid.levels[b.top()] if (_x, _y) != b.xyvals()]):
                            valid = False
                            break
                    if valid:
                        result += 1
        return result

    def part2(self):
        result = 0
        with open('./input.txt', 'r') as f:
            grid, bricks = self.prepare(f)
            bricksmap = {id(b): b for b in bricks}
            for b in bricks:
                if b.top() >= grid.z-1 or not grid.levels[b.top()+1]:
                    continue
                x, y = b.xyvals()
                result += grid.countFallen({id(b)}, b.top())
        return result

    def prepare(self, f: file) -> tuple[Grid, List[Brick]]:
        bricks = []
        zmax = 0
        n, m = 0, 0
        for l in f:
            l, r = l.strip().split('~')
            ln = [int(n) for n in l.split(',')]
            rn = [int(n) for n in r.split(',')]
            zmax = max(zmax, ln[2], rn[2])
            n, m = max(n, ln[0], rn[0]), max(m, ln[1], rn[1])
            bricks.append(Brick(Point(*ln), Point(*rn)))
        grid = Grid(zmax+1)
        grid.finalize(bricks)
        return (grid, bricks)


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
