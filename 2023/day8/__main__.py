#!/usr/bin/env python3
"""
Solution to day 8.
"""

from __future__ import annotations
from typing import *
from math import lcm

class Node:
    name: str
    left: Node
    right: Node

    def __init__(self, name):
        self.name = name


class Solution:
    def part1(self):
        result = 0
        with open('./input.txt', 'r') as f:
            (instructions, begin) = self.parsefile(f)
            node = begin[0]
            i = 0
            while node.name != 'ZZZ':
                if instructions[i] == 'L':
                    node = node.left
                else:
                    node = node.right
                i += 1
                if i == len(instructions):
                    i = 0
                result += 1
        return result

    def part2(self):
        result = 0
        with open('./input.txt', 'r') as f:
            (instructions, nodes) = self.parsefile(f, True)
            cycles = []
            for n in nodes:
                count = 0
                i = 0
                while n.name[-1] != 'Z':
                    if instructions[i] == 'L':
                        n = n.left
                    else:
                        n = n.right
                    i = 0 if i == len(instructions)-1 else i + 1
                    count += 1
                cycles.append(count)
            result = lcm(*cycles)
        return result

    def parsefile(self, f: file, part2: bool = False) -> tuple[List[str], List[Node]]:
        instructions = list(f.readline().strip())
        nodes = dict()
        f.readline()
        for l in f:
            root = l[0:3]
            left = l[7:10]
            right = l[12:15]
            for n in [root, left, right]:
                if n not in nodes:
                    nodes[n] = Node(n)
            nodes[root].left = nodes[left]
            nodes[root].right = nodes[right]
        if part2:
            return (instructions, [nodes[n] for n in filter(lambda n: n[-1] == 'A', nodes.keys())])
        else:
            return (instructions, [nodes['AAA']])


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
