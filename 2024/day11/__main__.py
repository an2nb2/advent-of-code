#!/usr/bin/env python3
"""
Solution to day 11.
"""

from functools import cache
from typing import *
from re import sub, search
from collections import Counter

class Solution:
    def part1(self):
        with open('./input.txt', 'r') as f:
            stones = f.read().strip().split(' ')
            for _ in range(25):
                _stones = []
                for s in stones:
                    _stones += self._change(s)
                stones = _stones
        return len(stones)

    def part2(self):
        result = 0

        @cache
        def compute(stone, i):
            if i == 0:
                return 1
            stones = self._change(stone)
            result = 0
            for s in stones:
                result += compute(s, i-1)
            return result

        with open('./input.txt', 'r') as f:
            stones = f.read().strip().split(' ')
            for s in stones:
                result += compute(s, 75)

        return result

    def _change(self, s):
        if s == '0':
            return ['1']
        elif not len(s) % 2:
            return [str(s[:len(s)//2]), str(int(str(s[len(s)//2:])))]
        else:
            return [str(int(s)*2024)]


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
