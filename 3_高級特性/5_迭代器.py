# 直接作用于for循环的对象统称为可迭代对象：Iterable
# 一类是集合数据类型，如list、tuple、dict、set、str等
# 一类是generator，包括生成器和带yield的generator function
# isinstance()可判斷一個對象是否為Iterable
from collections.abc import Iterable
print (isinstance([],Iterable))
print (isinstance((),Iterable))
print (isinstance({},Iterable))
print (isinstance((x for x in range(10)),Iterable))
print (isinstance(123,Iterable))

# 可以被next()調用并不斷返回下一個值的對象稱為迭代器 Iterator
from collections.abc import Iterator
print (isinstance((x for x in range(10)),Iterator))
print (isinstance({},Iterator))
print (isinstance(iter({}),Iterator)) # 可使用 Iter() 把Iterable 變成 Iterator

