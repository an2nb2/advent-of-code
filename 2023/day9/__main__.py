#!/usr/bin/env python3
"""
Solution to day 9.
"""

from functools import cache
from typing import *
from re import sub, search

class Solution:
    def part1(self):
        result = 0
        with open('./input.txt', 'r') as f:
            for l in f:
                nums = [int(n) for n in l.strip().split(' ')]
                result += self.findnext(nums)
        return result

    def part2(self):
        result = 0
        with open('./input.txt', 'r') as f:
            for l in f:
                nums = [int(n) for n in l.strip().split(' ')]
                result += self.findprev(nums)
        return result

    def findnext(self, nums: List[int]) -> int:
        diffs = self.builddiffs(nums)
        for i in range(len(diffs)-1, 0, -1):
            diffs[i-1].append(diffs[i][-1] + diffs[i-1][-1])
        return diffs[0][-1]

    def findprev(self, nums: List[int]) -> int:
        diffs = self.builddiffs(nums)
        for i in range(len(diffs)-1, 0, -1):
            diffs[i-1] = [diffs[i-1][0] - diffs[i][0]] + diffs[i-1]
        return diffs[0][0]

    def builddiffs(self, nums: List[int]) -> List[List[int]]:
        diffs = [nums]
        k = 0
        while True:
            diff = []
            allzeros = True
            for i in range(0, len(diffs[k])-1, 1):
                d = diffs[k][i+1] - diffs[k][i]
                diff.append(d)
                if d != 0:
                    allzeros = False
            diffs.append(diff)
            k += 1
            if allzeros:
                break
        return diffs


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
