#!/usr/bin/env python3
"""
Solution to day 3.
"""

from functools import cache
from typing import *
from re import sub, search, findall, compile

class Solution:
    MUL_RE = r'mul\([0-9]{1,3},[0-9]{1,3}\)'
    COND_RE = r'do(?:n\'t)?\(\)'

    def part1(self):
        result = 0
        with open('./input.txt', 'r') as f:
            inp = f.read()
            for m in findall(self.MUL_RE, inp):
                n1, n2 = m[4:-1].split(',')
                result += int(n1) * int(n2)
        return result

    def part2(self):
        result = 0
        with open('./input.txt', 'r') as f:
            inp = f.read()
            skip = False
            for m in findall(f'{self.MUL_RE}|{self.COND_RE}', inp):
                if m == "don't()":
                    skip = True
                elif m == 'do()':
                    skip = False
                elif not skip:
                    n1, n2 = m[4:-1].split(',')
                    result += int(n1) * int(n2)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
