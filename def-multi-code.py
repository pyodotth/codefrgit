
import base64
import string
from collections import ChainMap, Counter, deque, namedtuple
from string import ascii_letters, ascii_uppercase


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


def deencode():
    t = base64.b64encode('ฉันมีปากกา'.encode('utf-8'))
    print(t)
    th = base64.b64decode(t).decode('utf-8')
    print(th)
    t = base64.b16encode('ฉันมีปากกา'.encode('utf-8'))
    print(t)
    th = base64.b16decode(t).decode('utf-8')
    print(th)
    t = base64.b32encode('ฉันมีปากกา'.encode('utf-8'))
    print(t)
    th = base64.b32decode(t).decode('utf-8')
    print(th)


# ผูก dict 2 ตัวเข้าด้วยกัน ถ้า key ซ้ำจะเรียกใช้ตัวแรกเป็นหลัก
def uschainmap(keyinp):
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'c': 5, 'e': 6, 'g': 7}

    chaindict = ChainMap(dict1, dict2)
    print(chaindict[keyinp])


def usenametuple():
    lst = ['x', 'y']
    #point = namedtuple('Point', ['x', 'y'])
    # use same
    point = namedtuple('Point', lst)
    p = point(1, 2)
    p2 = point(3, 4)
    print("Point : {}/{}".format(p.x, p.y))
    print("Point : {}/{}".format(p2.x, p2.y))


def appendleft():
    q = deque(['a', 'b', 'c'])
    q.append('x')
    q.appendleft('y')
    print(q)


def countlst():
    c = Counter()
    for ch in ['AAA', 'ABC', 'AAA', 'BCB', 'AAA']:
        c[ch] += 1

    print(c)
    print(c['AAA'])


def makeatoz():
    ch_a = [chr(c) for c in range(65, 91)]
    ch_A = [chr(c) for c in range(97, 123)]
    print(ch_a)
    print(ch_A)
    char_a = list(string.ascii_lowercase)
    char_A = list(string.ascii_uppercase)
    char_L = list(string.ascii_letters)
    print(char_a)
    print(char_A)
    print(char_L)
