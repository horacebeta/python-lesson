# filter()
# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

from xml.etree.ElementTree import TreeBuilder


def is_odd(n):
    return n % 2 ==1

r = [1, 2, 4, 5, 6, 9, 10, 15]
print(list(filter(is_odd,r)))

def not_empty(s):
    return s and s.strip()

r = ['A', '', 'B', None, 'C', '  ']
print(list(filter(not_empty,r)))

# 生成質數
def _odd_iter():
    n = 1
    while True:
        n = n+1
        yield n

def _not_divisible(n):
    return lambda x: x% n > 0

def primes():
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)
        
for n in primes():
    if n < 1000:
        print(n)
    else:
        break

# practice
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909
def is_pailndrome(n):
    num = str(n)
    return num == num[::-1]

print(list(filter(is_pailndrome,range(1000))))