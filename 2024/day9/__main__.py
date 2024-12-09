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
            blocks = [int(n) for n in list(f.readline().strip())]
            last = len(blocks)-1 if len(blocks) % 2 else len(blocks)-2
            position = 0
            for i in range(len(blocks)):
                if i > last:
                    break
                if i % 2:
                    while blocks[i] > 0:
                        n = min(blocks[i], blocks[last])
                        blocks[i] -= n
                        blocks[last] -= n
                        for _ in range(n):
                            result += last//2*position
                            position += 1
                        if not blocks[last]:
                            last -= 2
                else:
                    for _ in range(blocks[i]):
                        result += i//2*position
                        position += 1
        return result

    def part2(self):
        result = 0
        with open('./input.txt', 'r') as f:
            blocks = [int(n) for n in list(f.readline().strip())]
            originblocks = blocks.copy()
            last = len(blocks)-1 if len(blocks) % 2 else len(blocks)-2
            fragments = {}

            for i in range(last, -1, -2):
                for j in range(1, i, 2):
                    n = blocks[i]
                    if blocks[j] < n:
                        continue
                    blocks[j] -= n
                    blocks[i] -= n
                    if j not in fragments:
                        fragments[j] = []
                    fragments[j].append((i//2, n))
                    break
            position = 0
            for i in range(len(blocks)):
                if i % 2:
                    if i in fragments:
                        for id, n in fragments[i]:
                            for _ in range(n):
                                result += id*position
                                position += 1
                        position += blocks[i]
                else:
                    if not blocks[i]:
                        position += originblocks[i]
                    for _ in range(blocks[i]):
                        result += i//2*position
                        position += 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
