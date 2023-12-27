#!/usr/bin/env python3
"""
Solution to day 5.
"""

from functools import cache
from typing import *
from re import sub, search
from sys import maxsize

class Solution:
    def part1(self):
        result = maxsize
        with open('./input.txt', 'r') as f:
            (seeds, maps) = self.parsefile(f)
            for s in seeds:
                for lists in maps:
                    for l in lists:
                        if s >= l[1] and s <= (l[1]+l[2]):
                            s = l[0] + (s-l[1])
                            break
                result = min(result, s)
        return result

    def part2(self):
        result = maxsize
        with open('./input.txt', 'r') as f:
            (seeds, maps) = self.parsefile(f)
            seeds = zip(seeds[0::2], seeds[1::2])
            for (start, length) in seeds:
                options = [[] for _ in range(len(maps)+1)]
                options[0] = [(start, start+length-1)]
                for i in range(len(maps)):
                    for (start, end) in options[i]:
                        intervaloptions = []
                        for l in maps[i]:
                            if (l[1]+l[2]-1) < start or end < l[1]:
                                continue
                            if start < l[1]:
                                options[i].append((start, l[1]-1))
                            if end > l[1]+l[2]:
                                options[i].append((l[1]+l[2], end))
                            start = max(start, l[1])
                            end = min(end, l[1]+l[2]-1)
                            intervaloptions.append((l[0] + start - l[1], l[0] + end - l[1]))
                        if not intervaloptions:
                            intervaloptions.append((start, end))
                        options[i+1].extend(intervaloptions)
                        options[i+1] = self.merge(options[i+1])
                for (s, _) in options[-1]:
                    result = min(result, s)
        return result

    def merge(self, intervals: set[tuple[int, int]]) -> set[tuple[int, int]]:
        intervals = sorted(intervals, key = lambda i : i[0])
        i = 1
        j = 0
        while i < len(intervals):
            if intervals[j][1] >= intervals[i][0]:
                intervals[j] = (intervals[j][0], max(intervals[j][1], intervals[i][1]))
                intervals.remove(intervals[i])
            else:
                j = i
                i += 1
        return intervals

    def parsefile(self, f) -> tuple[List[int], List[List[List[int]]]]:
        seeds = []
        maps = {
            'seed-to-soil': [],
            'soil-to-fertilizer': [],
            'fertilizer-to-water': [],
            'water-to-light': [],
            'light-to-temperature': [],
            'temperature-to-humidity': [],
            'humidity-to-location': [],
        }
        with open('./input.txt', 'r') as f:
            readto = None
            while True:
                l = f.readline()
                if not l:
                    break
                if l == '\n':
                    readto = None
                    continue
                l = l.strip().replace(' map:', '')
                if l.startswith('seeds'):
                    seeds = [int(n) for n in l.split(':')[1].strip().split(' ')]
                elif l in maps:
                    readto = l
                else:
                    maps[readto].append([int(n) for n in l.split(' ')])
        return (seeds, list(maps.values()))


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
