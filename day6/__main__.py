#!/usr/bin/env python3
"""
Solution to day 6.
"""

from functools import cache
from typing import *
from re import sub, search

class Solution:
    def part1(self):
        with open('./input.txt', 'r') as f:
            result = 1
            for (time, target) in zip(
                self.parseline(f.readline()),
                self.parseline(f.readline()),
            ):
                count = 0
                for i in range(1, time, 1):
                    r = (time-i)*i
                    if r > target:
                        count += 1
                result *= count
        return result

    def part2(self):
        count = 0
        with open('./input.txt', 'r') as f:
            time   = int(''.join([str(n) for n in self.parseline(f.readline())]))
            target = int(''.join([str(n) for n in self.parseline(f.readline())]))
            t = time//2
            count = 0
            while (time-t)*t > target:
                count += 1
                t -= 1
        return count*2 if time % 2 != 0 else count*2-1

    def parseline(self, l: str) -> List[int]:
        return [int(n) for n in filter(lambda n: n.strip() != '', l.split(':')[1].strip().split(' '))]


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
