#!/usr/bin/env python3
"""
Solution to day 10.
"""

from __future__ import annotations
from collections import deque
from functools import cache
from typing import *
from re import sub, search


class Solution:
    directions = {
        (-1, 0): {'7', 'F', '|'},
        (1, 0): {'J', 'L', '|'},
        (0, -1): {'-', 'L', 'F'},
        (0, 1): {'-', 'J', '7'},
    }
    connections = {
        '|': {(-1, 0), (1, 0)},
        '-': {(0, -1), (0, 1)},
        'L': {(-1, 0), (0, 1)},
        'J': {(-1, 0), (0, -1)},
        '7': {(1, 0), (0, -1)},
        'F': {(1, 0), (0, 1)},
    }

    def part1(self):
        result = 0
        with open('./input.txt', 'r') as f:
            (_, seen, _, last) = self.parsefield(f)
            result = (seen[last]+1) // 2
        return result

    def part2(self):
        result = 0
        with open('./input.txt', 'r') as f:
            (field, loop, start, _) = self.parsefield(f)

            # replace tiles which do not belong to loop
            for i in range(len(field)):
                for j in range(len(field[i])):
                    if (i, j) not in loop:
                        field[i] = field[i][:j] + '.' + field[i][j+1:]

            # double scale field
            newfield = self.scale(field)

            # collect border positions for flood fill
            borders = [(0, j) for j in range(len(newfield[0]))]
            borders.extend([(i, len(newfield[i])-1) for i in range(1, len(newfield), 1)])
            borders.extend([(len(newfield)-1, j) for j in range(len(newfield[-1])-1)])
            borders.extend([(i, 0) for i in range(1, len(newfield)-1, 1)])

            # flood fill outter space
            seen = {}
            for (i, j) in borders:
                if newfield[i][j] not in {'.', '0'}:
                    continue
                q = deque()
                q.append((i, j))
                while len(q) > 0:
                    (i, j) = q.popleft()
                    for (_i, _j) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                        if _i < 0 or _i >= len(newfield) or _j < 0 or _j >= len(newfield[_i]):
                            continue
                        if newfield[_i][_j] not in {'.', '0'}:
                            continue
                        if (_i, _j) in seen:
                            continue
                        newfield[_i] = str(newfield[_i][:_j] + '0' + newfield[_i][_j+1:])
                        seen[(_i, _j)] = True
                        q.append((_i, _j))

            # count result
            for i in range(len(newfield)):
                print(newfield[i])
                for j in range(len(newfield[i])):
                    if newfield[i][j] == '.':
                        result += 1

        return result

    def parsefield(self, f: file) -> (List[str], dict[tuple[int, int], int], tuple[int, int], tuple[int, int]):
        field = []
        start = None
        last = None
        seen = dict()
        for l in f:
            field.append(l.strip())
            sj = field[-1].find('S')
            if sj >= 0:
                start = (len(field)-1, sj)
        for (i, j) in self.adjacent(*start):
            if i < 0 or i >= len(field) or j < 0 or j >= len(field[i]):
                continue
            if field[i][j] == '.':
                continue
            seen = {start: 0, (i, j): 1}
            last = self.traverse(field, seen, i, j)
            if last != (i, j) and last in self.adjacent(*start):
                for c in self.connections.keys():
                    if self.validconnection(c, field[i][j], (i-start[0], j-start[1])) and self.validconnection(field[last[0]][last[1]], c, (start[0]-last[0], start[1]-last[1])):
                        field[start[0]].replace('S', c)
                        break
                if field[start[0]][start[1]] != 'S':
                    break
        return (field, seen, start, last)

    def traverse(self, field: List[str], seen: dict[tuple[int, int], int], i: int, j: int) -> int:
        q = deque()
        q.append((i, j))
        last = None
        while len(q) > 0:
            (ri, rj) = q.popleft()
            for (i, j) in self.adjacent(ri, rj):
                if i < 0 or i >= len(field) or j < 0 or j >= len(field[i]):
                    continue
                if (i, j) in seen:
                    continue
                if field[i][j] == '.':
                    continue
                if self.validconnection(field[ri][rj], field[i][j], (i-ri, j-rj)):
                    q.append((i, j))
                    seen[(i, j)] = seen[(ri, rj)] + 1
                    last = (i, j)
        return last

    def adjacent(self, i: int, j: int) -> List[tuple[int, int]]:
        return [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]

    def validconnection(self, c1: str, c2: str, delta: tuple[int, int]) -> bool:
        return delta in self.connections[c1] and c2 in self.directions[delta]

    def scale(self, field: List[str]) -> List[str]:
        scaled = []
        # scale horizontaly
        for i in range(len(field)):
            scaled.append(field[i])
            row = []
            for k in range(len(field[i])):
                if field[i][k] in {'|', 'F', '7'}:
                    row.append('|')
                elif field[i][k] == '.':
                    row.append('0')
                else:
                    row.append('0')
            scaled.append(''.join(row))
        # scale vertically
        for j in range(0, len(scaled[0])*2, 2):
            for k in range(len(scaled)):
                if scaled[k][j] in {'J', '7', '|'} and scaled[k][j+1] in {'F', 'L', '|'}:
                    scaled[k] = scaled[k][:j+1] + '0' + scaled[k][j+1:]
                elif scaled[k][j] in {'F', '-', 'L'}:
                    scaled[k] = scaled[k][:j+1] + '-' + scaled[k][j+1:]
                else:
                    scaled[k] = scaled[k][:j+1] + '0' + scaled[k][j+1:]
        return scaled

    def descale(self, field: List[str]) -> List[str]:
        descaled = field[0::2]
        for i in range(len(descaled)):
            descaled[i] = ''.join(descaled[i][0::2])
        return descaled


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
