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
        for nums in self._readfile():
            if self._valid(nums):
                result += 1
        return result

    def part2(self):
        result = 0
        for nums in self._readfile():
            for i in range(len(nums)):
                if self._valid(nums[:i] + nums[i+1:len(nums)]):
                    result += 1
                    break
        return result

    def _readfile(self):
        with open('./input.txt', 'r') as f:
            while True:
                l = f.readline()
                if not l:
                    break
                nums = l.strip().split(' ')
                yield([int(n) for n in nums])

    def _valid(self, nums):
        descending = nums[0] > nums[1]
        for i in range(1, len(nums)):
            if (descending and nums[i] >= nums[i-1]) or (not descending and nums[i] <= nums[i-1]) or (abs(nums[i-1] - nums[i]) > 3):
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
