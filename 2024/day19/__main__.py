#!/usr/bin/env python3
"""
Solution to day 19.
"""

from functools import cache
from typing import *
from re import sub, search

class Solution:
    def part1(self):
        result = 0
        patterns, designs = self._readfile()

        @cache
        def valid(design):
            if not design:
                return True
            for i in range(len(design)):
                if design[:i+1] in patterns and valid(design[i+1:]):
                    return True
            return False

        for d in designs:
            if valid(d):
                result += 1
        return result

    def part2(self):
        result = 0
        patterns, designs = self._readfile()

        @cache
        def arrangements(design):
            if not design:
                return 1
            count = 0
            for i in range(len(design)):
                if design[:i+1] in patterns:
                    count += arrangements(design[i+1:])
            return count

        for d in designs:
            result += arrangements(d)
        return result

    def _readfile(self):
        with open('./input.txt', 'r') as f:
            patterns, designs = f.read().strip().split('\n\n')
            return (
                {p.strip() for p in patterns.strip().split(',')},
                designs.strip().split('\n'),
            )


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
