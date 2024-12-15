#!/usr/bin/env python3
"""
Solution to day 15.
"""

from functools import cache
from typing import *
from re import sub, search
from functools import reduce
from operator import mul, concat
from collections import deque

class Solution:
    moves = {
        '<': (0, -1),
        'v': (1, 0),
        '>': (0, 1),
        '^': (-1, 0),
    }

    def part1(self):
        result = 0
        grid, moves, robot = self._readfile()
        grid[robot[0]][robot[1]] = '.'

        def freeposition(i, j, di, dj):
            while grid[i][j] != '#' and grid[i][j] != '.':
                i += di
                j += dj
            return i, j

        for m in moves:
            (di, dj) = self.moves[m]
            (ni, nj) = robot[0]+di, robot[1]+dj

            match grid[ni][nj]:
                case '#':
                    pass
                case '.':
                    robot = (ni, nj)
                case 'O':
                    fi, fj = freeposition(ni, nj, di, dj)
                    if grid[fi][fj] == '.':
                        robot = (ni, nj)
                        grid[ni][nj], grid[fi][fj] = '.', 'O'

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 'O':
                    result += 100 * i + j

        return result

    def part2(self):
        result = 0

        _grid, moves, robot = self._readfile()
        grid = []
        for x in _grid:
            grid.append([])
            for y in x:
                if y == 'O':
                    grid[-1] += '[]'
                elif y == '@':
                    grid[-1] += '@.'
                else:
                    grid[-1] += y * 2

        robot = (robot[0], grid[robot[0]].index('@'))
        grid[robot[0]][robot[1]] = '.'

        def colidedblocks(i, j, di, dj):
            current = (i, j, j+1) if grid[i][j] == '[' else (i, j-1, j)
            blocks = {current}
            q = deque()
            q.append(current)
            while len(q) > 0:
                i, jl, jr = q.pop()
                ni, njl, njr = i+di, jl+dj, jr+dj
                ls, rs = grid[ni][njl], grid[ni][njr]
                if ls == '#' or rs == '#':
                    return [], False
                if ls == '.' and rs == '.':
                    continue
                if ls == '[':
                    if (ni, njl, njl+1) not in blocks:
                        blocks.add((ni, njl, njl+1))
                        q.append((ni, njl, njl+1))
                elif ls == ']':
                    if (ni, njl-1, njl) not in blocks:
                        blocks.add((ni, njl-1, njl))
                        q.append((ni, njl-1, njl))
                if rs == '[':
                    if (ni, njr, njr+1) not in blocks:
                        blocks.add((ni, njr, njr+1))
                        q.append((ni, njr, njr+1))
                elif rs == ']':
                    if (ni, njr-1, njr) not in blocks:
                        blocks.add((ni, njr-1, njr))
                        q.append((ni, njr-1, njr))
            return blocks, True

        for m in moves:
            (di, dj) = self.moves[m]
            (ni, nj) = robot[0]+di, robot[1]+dj

            match grid[ni][nj]:
                case '#':
                    pass
                case '.':
                    robot = (ni, nj)
                case '[' | ']':
                    blocks, canmove = colidedblocks(ni, nj, di, dj)
                    if canmove:
                        for (i, jl, jr) in blocks:
                            grid[i][jl], grid[i][jr] = '.', '.'
                        for (i, jl, jr) in blocks:
                            grid[i+di][jl+dj], grid[i+di][jr+dj] = '[', ']'
                        robot = (ni, nj)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '[':
                    result += 100 * i + j

        for g in grid:
            print(reduce(concat, g))

        return result

    def _readfile(self):
        with open('./input.txt', 'r') as f:
            gridstr, moves = f.read().strip().split('\n\n')
            grid = []
            moves = sum([list(m) for m in moves.strip().split('\n')], [])

            start = None
            for g in gridstr.strip().split('\n'):
                grid.append(list(g))
                if '@' in grid[-1]:
                    start = (len(grid)-1, grid[-1].index('@'))

            return grid, moves, start


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
