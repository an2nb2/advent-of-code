#!/usr/bin/env python3
"""
Solution to day 17.
"""

from functools import cache
from typing import *
from re import sub, search

class Solution:
    def part1(self):
        (a, b, c), program = self._readfile()
        registers = {
            'a': a,
            'b': b,
            'c': c,
        }
        output = self.run(registers, program)
        return ','.join([str(n) for n in output])

    def part2(self):
        (_, b, c), program = self._readfile()
        out = []
        result = 0
        a = -1
        i, j = len(program)-1, -1
        while program != out:
            cond = lambda: program[i:] != out[j:] if i > 1 else program != out
            while cond():
                a += 1
                registers = {
                    'a': a,
                    'b': b,
                    'c': c,
                }
                out = self.run(registers, program)
                result = a
            a *= 2**3
            i -= 1
            j -= 1
        return result

    def _readfile(self):
        with open('./input.txt', 'r') as f:
            registers, program = f.read().strip().split('\n\n')
            a, b, c = [int(r.split(':')[1].strip()) for r in registers.split('\n')]
            program = [int(op) for op in program.split(':')[1].strip().split(',')]
            return (a, b, c), program

    def run(self, registers, program):
        def combo(operand):
            match operand:
                case num if num <= 3:
                    return num
                case 4:
                    return registers['a']
                case 5:
                    return registers['b']
                case 6:
                    return registers['c']
                case 7:
                    raise('invalid operand 7')
        i = 0
        program = list(zip(program[0::2], program[1::2]))
        output = []
        while i < len(program):
            (opcode, operand) = program[i]
            match opcode:
                case 0:
                    registers['a'] = int(registers['a'] / 2**combo(operand))
                case 1:
                    registers['b'] = registers['b'] ^ operand
                case 2:
                    registers['b'] = combo(operand) % 8
                case 3:
                    if registers['a']:
                        i = operand // 2
                        continue
                case 4:
                    registers['b'] = registers['b'] ^ registers['c']
                case 5:
                    output.append(combo(operand)%8)
                case 6:
                    registers['b'] = int(registers['a'] / 2**combo(operand))
                case 7:
                    registers['c'] = int(registers['a'] / 2**combo(operand))
            i += 1
        return output


if __name__ == '__main__':
    s = Solution()
    print(s.part1())
    print(s.part2())
