#!/usr/bin/env python3

"""Solution for day13."""

def main():
    f = open("input/test.txt", "r")
    for parts in f.read().split("\n\n"):
        p1, p2 = [eval(p) for p in parts.split("\n") if len(p) > 0]
        deepCompare(p1, p2)


def deepCompare(p1, p2):
    print(p1, p2)

if __name__ == "__main__":
    main()
