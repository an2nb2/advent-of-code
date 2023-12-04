#!/usr/bin/env python3
"""
Solution to day 4.
"""

from functools import cache
from typing import *
from math import factorial
from re import sub, search

class Solution:
    def part1(self):
        result = 0
        with open('./input.txt', 'r') as f:
            for l in f:
                have = set()
                winning = set()
                f, s = l.strip().split(':')[1].split('|')
                for n in f.strip().split(' '):
                    if n.strip() != '':
                        have.add(int(n.strip()))
                for n in s.strip().split(' '):
                    if n.strip() != '':
                        winning.add(int(n.strip()))
                r = have.intersection(winning)
                if len(r) > 0:
                    result += 2**(len(r)-1)
        return result

    def part2(self):
        result = 0
        with open('./input.txt', 'r') as f:
            wins, i = [], 0
            for l in f:
                have = set()
                winning = set()
                f, s = l.strip().split(':')[1].split('|')
                for n in f.strip().split(' '):
                    if n.strip() != '':
                        have.add(int(n.strip()))
                for n in s.strip().split(' '):
                    if n.strip() != '':
                        winning.add(int(n.strip()))
                if i == len(wins):
                    wins.append(1)
                r = have.intersection(winning)
                for k in range(i+1, i+1+len(r), 1):
                    if k == len(wins):
                        wins.append(1)
                    wins[k] += wins[i]
                result += wins[i]
                i += 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())



#
