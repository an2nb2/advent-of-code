#!/usr/bin/env python3
"""
Solution to day 19.
"""

from __future__ import annotations
from functools import cache
from typing import *
from re import sub, search

class Solution:
    def part1(self):
        result = 0
        with open('./input.txt', 'r') as f:
            workflows, parts = self.parsefile(f)
            for part in parts:
                if self.run_workflow(part, workflows):
                    result += sum(part.values())
        return result

    def part2(self):
        result = 0
        with open('./input.txt', 'r') as f:
            workflows, _ = self.parsefile(f)
            pass
        return result

    def parsefile(self, f: file):
        raw_workflows, raw_parts = f.read().strip().split('\n\n')
        workflows, parts = {}, []

        for w in raw_workflows.split():
            data = search(r'(.+)\{(.+)\}', w)
            workflows[data.group(1)] = data.group(2).split(',')

        for p in raw_parts.split():
            data = search(r'\{(.+)\}', p)
            part = {}
            for item in data.group(1).split(','):
                part[item[0]] = int(item[2:])
            parts.append(part)

        return (workflows, parts)

    def run_workflows(self, part: dict[str, int], workflows: dict[str, List[str]]) -> bool:
        name = 'in'
        while name:
            for w in workflows[name]:
                target = None
                if w == workflows[name][-1]:
                    target = w
                else:
                    rule, t = w.split(':')
                    val = int(rule[2:])
                    valid = part[rule[0]] > val if rule[1] == '>' else part[rule[0]] < val
                    if valid:
                        target = t
                if target == 'A':
                    return True
                elif target == 'R':
                    return False
                elif target:
                    name = target
                    break
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
