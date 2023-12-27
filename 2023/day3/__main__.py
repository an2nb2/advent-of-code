#!/usr/bin/env python3
"""
Solution to day 3.
"""

from functools import cache
from typing import *
from re import sub, search, match

class Solution:
    def part1(self):
        result = 0
        with open('./input.txt', 'r') as f:
            data = f.read().strip().split('\n')
            for i in range(len(data)):
                num = ''
                for j in range(len(data[i])):
                    isdigit = match(r'[0-9]+', data[i][j])
                    if isdigit:
                        num += data[i][j]
                    if j == len(data[i])-1 or not isdigit:
                        if num:
                            for k in range(j-len(num), j, 1):
                                if self.adjacent(i, k, data):
                                    result += int(num)
                                    break
                        num = ''
        return result

    def part2(self):
        result = 0
        with open('./input.txt', 'r') as f:
            data = f.read().strip().split('\n')
            for i in range(1, len(data), 1):
                for j in range(len(data[i])):
                    if data[i][j] != '*':
                        continue
                    numbers = self.adjacentnumbers(i, j, data)
                    if len(numbers) == 2:
                        result += numbers[0] * numbers[1]
        return result

    def adjacent(self, i: int, j: int, data: List[str]) -> bool:
        issymbol = (lambda s: match(r'[^0-9\.]+', s))
        return (
            (i+1 < len(data) and issymbol(data[i+1][j])) or
            (i > 0 and issymbol(data[i-1][j])) or
            (j+1 < len(data[i]) and issymbol(data[i][j+1])) or
            (j > 0 and issymbol(data[i][j-1])) or
            (i+1 < len(data) and j+1 < len(data[i]) and issymbol(data[i+1][j+1])) or
            (i+1 < len(data) and j > 0 and issymbol(data[i+1][j-1])) or
            (i > 0 and j+1 < len(data[i]) and issymbol(data[i-1][j+1])) or
            (i > 0 and j > 0 and issymbol(data[i-1][j-1]))
        )

    def adjacentnumbers(self, i: int, j: int, data: List[str]) -> List[int]:
        numbers = []
        seen = dict()
        for (i, j) in [(i-1, j-1), (i-1,j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]:
            if i < 0 or i >= len(data) or j < 0 or j >= len(data[i]):
                continue
            if match(r'[0-9]+', data[i][j]) and (i, j) not in seen:
                num = data[i][j]
                k = j - 1
                while k >= 0 and match(r'[0-9]+', data[i][k]):
                    seen[(i, k)] = True
                    num = data[i][k] + num
                    k -= 1
                k = j + 1
                while k < len(data[i]) and match(r'[0-9]+', data[i][k]):
                    seen[(i, k)] = True
                    num += data[i][k]
                    k += 1
                numbers.append(int(num))
        return numbers


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
