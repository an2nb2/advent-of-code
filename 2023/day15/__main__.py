#!/usr/bin/env python3
"""
Solution to day 15.
"""

from functools import cache
from typing import *
from re import sub, search

class Hashmap:
    buckets = [[] for _ in range(256)]

    def add(self, key: str, val: int):
        h = self.hash(key)
        exists = False
        for i in range(len(self.buckets[h])):
            if self.buckets[h][i][0] == key:
                self.buckets[h][i] = (key, val)
                exists = True
                break
        if not exists:
            self.buckets[h].append((key, val))

    def remove(self, key: str):
        h = self.hash(key)
        self.buckets[h] = list(filter(lambda x: x[0] != key, self.buckets[h]))

    def hash(self, p: str) -> int:
        v = 0
        for ch in p:
            v += ord(ch)
            v *= 17
            v %= 256
        return v

    def power(self) -> int:
        r = 0
        for i in range(len(self.buckets)):
            for j in range(len(self.buckets[i])):
                r += (i+1) * (j+1) * self.buckets[i][j][1]
        return r


class Solution:
    def part1(self):
        result = 0
        with open('./input.txt', 'r') as f:
            plain = f.read().strip().split(',')
            h = Hashmap()
            for p in plain:
                result += h.hash(p)
        return result

    def part2(self):
        result = 0
        with open('./input.txt', 'r') as f:
            plain = f.read().strip().split(',')
            h = Hashmap()
            for p in plain:
                (label, instr, length) = self.parse_instruction(p)
                if instr == '-':
                    h.remove(label)
                else:
                    h.add(label, length)
            result = h.power()
        return result

    def parse_instruction(self, s: str) -> tuple[str, str, int]:
        if s[-1] == '-':
            return (s[:-1], '-', 0)
        else:
            label, length = s.split('=')
            return (label, '=', int(length))


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
