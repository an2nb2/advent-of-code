#!/usr/bin/env python3
"""
Solution to day 1.
"""

from functools import cache
from typing import *
from re import sub, search

class Solution:
    wdigits = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }

    def part1(self) -> int:
        s = 0
        with open('./input.txt', 'r') as f:
            while True:
                l = f.readline().strip()
                if not l:
                    break
                digits = sub(r'[^0-9]+', '', l)
                s += int(digits[0] + digits[-1])
        return s

    def part2(self) -> int:
        s = 0
        with open('./input.txt', 'r') as f:
            while True:
                l = f.readline().strip()
                if not l:
                    break
                first = ""
                digit = ""
                for i in range(len(l)):
                    if search(r'^[0-9]$', l[i]):
                        first = l[i]
                        break
                    else:
                        digit += l[i]
                        r = search(r'one|two|three|four|five|six|seven|eight|nine', digit)
                        if r:
                            first = str(self.wdigits[r.group(0)])
                            break
                last  = ""
                digit = ""
                for i in range(len(l)-1, -1, -1):
                    if search(r'^[0-9]$', l[i]):
                        last = l[i]
                        break
                    else:
                        digit = l[i] + digit
                        r = search(r'one|two|three|four|five|six|seven|eight|nine', digit)
                        if r:
                            last = str(self.wdigits[r.group(0)])
                            break
                s += int(first + last)
        return s


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
