#!/usr/bin/env python3
"""
Solution to day 2.
"""

from functools import cache
from typing import *
from re import sub, search

class Solution:
    def part1(self):
        result = 0
        with open('./input.txt', 'r') as f:
            for r in f.read().strip().split(','):
                r1, r2 = [int(_r) for _r in r.split('-')]
                for k in range(r1, r2+1, 1):
                    kstr = str(k)
                    if kstr[len(kstr)//2:] == kstr[:len(kstr)//2]:
                        result += k
        return result

    def part2(self):
        result = 0

        def valid(k):
            if k < 10:
                return False
            s = str(k)
            if (s[0] * len(s)) == s:
                return True
            for n in range(2, (len(s)//2)+1, 1):
                v = True
                i = 0
                while i < len(s) - n:
                    if s[i:i+n] != s[i+n:i+n+n]:
                        v = False
                        break
                    i += n
                if v:
                    return True
            return False

        with open('./input.txt', 'r') as f:
            for r in f.read().strip().split(','):
                r1, r2 = [int(_r) for _r in r.split('-')]
                for k in range(r1, r2+1, 1):
                    if valid(k):
                        result += k
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
