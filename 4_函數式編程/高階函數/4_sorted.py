# 內置函數 sorted() 
# sorted(iterable, cmp=None, key=None, reverse=False)
r = [36, 5, -12, 9, -21]
print(sorted(r))

# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
print(sorted(r,key=abs))

n = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(n,key=str.lower))

print(sorted(n,key=str.lower,reverse = True))

# practice
# 對下表按名字排列
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]

print(sorted(L,key = by_name))
# 對下表按成績排列
def by_score(t):
    return t[1]

print(sorted(L,key = by_score,reverse = True))