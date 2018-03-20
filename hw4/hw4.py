import numpy

def q2(a, mn, mx):
    n = len(a)
    d = dict()
    sorted_a = []
    for val in a:
        if d.get(val):
            d[val] += 1
        else:
            d[val] = 1
    for i in range(mn, mx+1):
        if d.get(i):
            sorted_a.extend([i]*d[i])
    return sorted_a

if __name__ == "__main__":
    a = []
    n = 20
    for i in range(0, n):
        a.append(numpy.random.randint(0, n))
    print((a, min(a), max(a)))
    print(q2(a, min(a), max(a)))
