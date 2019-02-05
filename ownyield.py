
def yeildchar(s):
    for ch in s:
        yield ch


def lst100():
    r = list(range(100))
    print(r)


def runyeild():
    inp = input("Enter some Text :")
    yei = yeildchar(inp)
    try:
        for _ in range(len(inp)):
            print(next(yei))
    except StopIteration as ex:
        print(ex.value)


def iterlst():
    x = iter([1, 2, 3, 4, 5])
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))


iterlst()
