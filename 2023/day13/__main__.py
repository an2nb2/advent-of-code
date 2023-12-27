#!/usr/bin/env python3
"""
Solution to day 13.
"""

from functools import cache
from typing import *
from re import sub, search

class Solution:
    def part1(self):
        result = 0
        with open('./input.txt', 'r') as f:
            patterns = f.read().strip().split('\n\n')

            for p in patterns:
                (rows, cols) = self.parsePattern(p)
                result += self.reflection(cols)
                result += self.reflection(rows) * 100
        return result

    def part2(self):
        result = 0
        with open('./input.txt', 'r') as f:
            patterns = f.read().strip().split('\n\n')

            for p in patterns:
                (rows, cols) = self.parsePattern(p)
                result += self.smudgereflection(cols) * 100
                result += self.smudgereflection(rows)
        return result

    def parsePattern(self, p: str) -> (List[str], List[str]):
        rows = p.strip().split('\n')
        cols = []
        for j in range(len(rows[0])):
            cols.append(''.join([rows[i][j] for i in range(len(rows))]))
        return (rows, cols)

    def reflection(self, data: List[str]) -> int:
        for i in range(1, len(data), 1):
            if data[i] != data[i-1]:
                continue
            x, y = i, i-1
            valid = True
            for j in range(min(i, len(data)-i)-1):
                x += 1
                y -= 1
                if data[x] != data[y]:
                    valid = False
                    break
            if valid:
                return i
        return 0

    def smudgereflection(self, data: List[str]) -> int:
        for j in range(1, len(data[0])):
            diffs = 0
            for i in range(len(data)):
                x, y = j, j-1
                for _ in range(min(j, len(data[i])-j)):
                    if data[i][x] != data[i][y]:
                        diffs += 1
                        break
                    x += 1
                    y -= 1
            if diffs == 1:
                return j
        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
