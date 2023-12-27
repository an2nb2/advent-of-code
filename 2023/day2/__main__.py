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
        with open('./input.txt', 'r') as f:
            while True:
                l = f.readline()
                if not l:
                    break
                (game, colors) = self.parse(l)
                if all([red <= 12 and green <= 13 and blue <= 14 for (red, green, blue) in colors]):
                    result += game
        return result

    def part2(self):
        result = 0
        with open('./input.txt', 'r') as f:
            while True:
                l = f.readline()
                if not l:
                    break
                (game, colors) = self.parse(l)
                red, green, blue = 0, 0, 0
                for (r, g, b) in colors:
                    red = max(red, r)
                    green = max(green, g)
                    blue = max(blue, b)
                result += red * green * blue
        return result

    def parse(self, line: str) -> tuple[int, List[tuple[int, int, int]]]:
        game = int(line.split(":")[0].split(" ")[1])
        groups = line.split(":")[1].split(";")
        colors = []
        for g in groups:
            red, green, blue = 0, 0, 0
            for c in g.split(","):
                cl = c.strip().split(" ")
                color = cl[1].strip()
                if color == "red":
                    red += int(cl[0].strip())
                elif color == "blue":
                    blue += int(cl[0].strip())
                elif color == "green":
                    green += int(cl[0].strip())
            colors.append((red, green, blue))
        return (game, colors)


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
