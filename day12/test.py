def test(l):
    l = l.copy()
    l[0] -= 1
    print(l)

x = [2, 2, 2]
test(x)
print(x)
