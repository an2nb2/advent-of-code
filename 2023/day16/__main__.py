#!/usr/bin/env python3
"""
Solution to day 16.
"""

from typing import *
from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4

    def next(self) -> tuple[int, int]:
        match self:
            case self.UP:
                return (-1, 0)
            case self.DOWN:
                return (1, 0)
            case self.RIGHT:
                return (0, 1)
            case self.LEFT:
                return (0, -1)


reflections = {
    '/': {
        Direction.UP: Direction.RIGHT,
        Direction.DOWN: Direction.LEFT,
        Direction.LEFT: Direction.DOWN,
        Direction.RIGHT: Direction.UP,
    },
    '\\': {
        Direction.UP: Direction.LEFT,
        Direction.DOWN: Direction.RIGHT,
        Direction.LEFT: Direction.UP,
        Direction.RIGHT: Direction.DOWN,
    },
}


class Solution:
    def part1(self):
        result = 0
        with open('./input.txt', 'r') as f:
            field = [list(l) for l in f.read().strip().split('\n')]
            visited = self.emulate(field, [(0, 0, Direction.RIGHT)])
            result = len(visited)
        return result

    def part2(self):
        result = 0
        with open('./input.txt', 'r') as f:
            field = [list(l) for l in f.read().strip().split('\n')]
            n = len(field)
            beams = sum([
                [(0, j, Direction.DOWN) for j in range(n)],
                [(i, 0, Direction.RIGHT) for i in range(n)],
                [(n-1, j, Direction.UP) for j in range(n)],
                [(i, n-1, Direction.LEFT) for i in range(n)],
            ], [])
            for (i, j, d) in beams:
                v = self.emulate(field, [(i, j, d)])
                result = max(result, len(v))
        return result

    def emulate(self, field: List[List[str]], beams: List[tuple[int, int, Direction]]) -> dict[tuple[int, int], Direction]:
        n = len(field)
        visited = dict()
        while True:
            moving = False
            for k in range(len(beams)):
                (i, j, d) = beams[k]
                if i >= n or j >= n or i < 0 or j < 0:
                    continue
                if (i, j) in visited and visited[(i, j)] == d:
                    continue
                moving = True
                visited[(i, j)] = d
                match field[i][j]:
                    case '/' | '\\':
                        d = Direction(reflections[field[i][j]][d])
                    case '-':
                        if d is Direction.UP or d is Direction.DOWN:
                            d = Direction.LEFT
                            beams.append((i, j+1, Direction.RIGHT))
                    case '|':
                        if d is Direction.LEFT or d is Direction.RIGHT:
                            d = Direction.UP
                            beams.append((i+1, j, Direction.DOWN))
                (di, dj) = d.next()
                beams[k] = (i+di, j+dj, d)
            if not moving:
                break
        return visited

    def print(self, n: int, visited: dict[tuple[int, int], Direction]):
        for i in range(n):
            l = ''
            for j in range(n):
                if (i, j) in visited:
                    l += '#'
                else:
                    l += '.'
            print(l)

if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
