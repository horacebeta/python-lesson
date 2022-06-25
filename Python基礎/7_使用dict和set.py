# 字典dict，使用键-值（key-value）存储，具有极快的查找速度
## dict内部存放的顺序和key放入的顺序是没有关系的
### dict的key必须是不可变对象
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

#通過key放入數據
d['Michael'] = 88
print(d)

##避免key不存在的錯誤
#一是通过in判断key是否存在
print('Horace' in d)

#二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
print(d.get('Horace','no this key'))

#删除一个key，用pop(key)方法
d.pop('Michael')
print(d)

#增加一個key
d.update({'Horace':100})
print(d)

###################################################

#set，和dict相似，一組key的集合，不能存儲value。set中，沒有重復的key
s = set([1,1,1,2,2,3,3,3,4])
print(s)

#增加key
s.add(5)
print(s)

#刪除
s.remove(1)
print(s)

#set之間可運算集中的交集、并集
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2
s1 | s2