#求ACSII的十進制編碼
print(ord('A'))
print(ord('壕'))

##把ACSII的十進制編碼轉成對應的字符
print(chr(66))

#由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes
##Python对bytes类型的数据用带b前缀的单引号或双引号表示
###以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('ABC'.encode('ascii'))
print('呂少壕'.encode('UTF-8')) #在bytes中，无法显示为ASCII字符的字节，用\x##显示

#把bytes变为str，就需要用decode()方法
print(b'ABC'.decode('ascii'))
print(b'\xe5\x91\x82\xe5\xb0\x91\xe5\xa3\x95'.decode('utf-8'))

#len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
print(len('呂少壕'))
print(len('呂少壕'.encode('UTF-8')))