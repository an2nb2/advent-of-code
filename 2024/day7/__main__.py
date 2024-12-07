#!/usr/bin/env python3
"""
Solution to day 7.
"""

from functools import cache
from typing import *
from re import sub, search

class Solution:
    def part1(self):
        result = 0
        for target, nums in self._readfile():
            def valid(curr, i):
                if curr > target:
                    return False
                if i == len(nums):
                    return target == curr
                return valid(curr+nums[i], i+1) or valid(curr*nums[i], i+1)
            if valid(nums[0], 1):
                result += target
        return result

    def part2(self):
        result = 0
        for target, nums in self._readfile():
            def valid(curr, i):
                if curr > target:
                    return False
                if i == len(nums):
                    return target == curr
                return valid(curr+nums[i], i+1) or \
                    valid(curr*nums[i], i+1) or \
                    valid(int(str(curr) + str(nums[i])), i+1)
            if valid(nums[0], 1):
                result += target
        return result

    def _readfile(self):
        with open('./input.txt', 'r') as f:
            while True:
                l = f.readline()
                if not l:
                    break
                t, nums = l.strip().split(':')
                nums = [int(n) for n in nums.strip().split(' ')]
                yield(int(t), nums)


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
