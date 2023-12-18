#!/usr/bin/env python3
"""
Solution to day 12.
"""

from typing import *

class Solution:
    def part1(self):
        result = 0
        with open('./input.txt', 'r') as f:
            for l in f:
                (conditions, groups) = l.strip().split(' ')
                result += self.arrangments(conditions, groups)
        return result

    def part2(self):
        result = 0
        with open('./input.txt', 'r') as f:
            for l in f:
                (conditions, groups) = l.strip().split(' ')
                conditions = '?'.join([conditions] * 5)
                groups = ','.join([groups] * 5)
                result += self.arrangments(conditions, groups)
        return result

    def arrangments(self, conditions: str, groups: str) -> int:
        cache = dict()

        def count(i: int, j: int, conditions: List[str], groups: List[int]) -> int:
            cachekey = (i, j, ''.join(conditions[i:]), ','.join([str(g) for g in groups]))
            if cachekey in cache:
                return cache[cachekey]

            if i >= len(conditions):
                if i >= len(conditions) and sum(groups) == 0:
                    return 1
                else:
                    return 0

            result = 0
            if conditions[i] == '#':
                if j < len(groups) and groups[j] > 0:
                    groups = groups.copy()
                    conditions = conditions.copy()

                    while groups[j] != 0:
                        if i >= len(conditions) or conditions[i] == '.':
                            return 0
                        conditions[i] = '#'
                        i += 1
                        groups[j] -= 1
                    result += count(i, j, conditions, groups)
            elif conditions[i] == '.':
                if j < len(groups) and groups[j] == 0:
                    result += count(i+1, j+1, conditions, groups)
                else:
                    result += count(i+1, j, conditions, groups)
            else:
                conditions[i] = '#'
                result += count(i, j, conditions, groups)

                conditions[i] = '.'
                result += count(i, j, conditions, groups)

                conditions[i] = '?'

            cache[cachekey] = result
            return result

        conditions = list(conditions)
        groups = [int(g) for g in groups.split(',')]

        return count(0, 0, conditions, groups)


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
