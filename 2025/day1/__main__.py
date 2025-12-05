#!/usr/bin/env python3
"""
Solution to day 1.
"""

from functools import cache
from typing import *
from re import sub, search

class Solution:
    def part1(self):
        result = 0
        current = 50
        with open('./input.txt', 'r') as f:
            while True:
                l = f.readline().strip()
                if not l:
                    break
                shift = int(l[1:])
                if l[0] == 'R':
                    current += shift
                else:
                    current -= shift
                current = current % 100
                if current == 0:
                    result += 1
        return result

    def part2(self):
        result = 0
        current = 50
        with open('./input.txt', 'r') as f:
            while True:
                l = f.readline().strip()
                if not l:
                    break
                shift = int(l[1:])
                if l[0] == 'R':
                    current += shift
                    result += current // 100
                    current %= 100
                else:
                    if current - shift <= 0:
                        if current:
                            result += 1
                        tmp = shift - (current % 100)
                        result += tmp // 100
                        current = -tmp % 100
                    else:
                        current -= shift
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
