#!/usr/bin/env python3
"""
Solution to day 20.
"""

from __future__ import annotations
from typing import *
from enum import Enum
from collections import deque


class Node:
    name: str
    state: bool | None
    out: List[Node]

    def __init__(self, name: str):
        self.name = name
        self.out = []
        self.state = None

    def write(self, sender: Node, pulse: bool) -> tuple[bool, List[Node]]:
        self.state = pulse
        return (self.state, self.out)

    @classmethod
    def build(cls, name: str) -> Node:
        match name[0]:
            case '%':
                return FF(name[1:])
            case '&':
                return Conj(name[1:])
            case _:
                return Node(name)


class Conj(Node):
    inputs: tuple[str, bool]

    def __init__(self, name: str):
        self.name = name
        self.out = []
        self.state = None
        self.inputs = dict()

    def write(self, sender: Node, pulse: bool):
        self.inputs[sender.name] = pulse
        return (not all(self.inputs.values()), self.out)


class FF(Node):
    closed: bool = False

    def write(self, sender: Node, pulse: bool) -> List[Node]:
        if pulse:
            self.closed = True
            return (self.state, [])
        else:
            self.closed = False
            self.state = not bool(self.state)
            return (self.state, self.out)



class Solution:
    def part1(self):
        result = 0
        with open('./input.txt', 'r') as f:
            nodes = self.parsefile(f)
            stats = {False: 0, True: 0}
            cycles = 0
            while cycles < 1000:
                cycles += 1

                node = Node('button')
                node.out.append(nodes['broadcaster'])

                q = deque()
                q.append((None, False, node))
                stats[False] -= 1

                while len(q) > 0:
                    sender, pulse, node = q.popleft()
                    stats[pulse] += 1
                    (pulse, out) = node.write(sender, pulse)
                    for n in out:
                        # print(f'{node.name} -{"high" if pulse else "low"}- -> {n.name}')
                        q.append((node, pulse, n))
            result = stats[True] * stats[False]
        return result

    def part2(self):
        result = 0
        with open('./input.txt', 'r') as f:
            pass
        return result

    def parsefile(self, f: file) -> dict[str, Node]:
        nodes = {}
        out = {}
        for l in f:
            h, t = l.strip().split(' -> ')
            node = Node.build(h.strip())
            if node not in nodes:
                nodes[node.name] = node
            out[node.name] = t.strip().split(', ')
            for n in out[node.name]:
                if n not in nodes:
                    nodes[n] = Node.build(n)
        for name in out.keys():
            for c in out[name]:
                if isinstance(nodes[c], Conj):
                    nodes[c].inputs[name] = False
                nodes[name].out.append(nodes[c])
        return nodes


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
