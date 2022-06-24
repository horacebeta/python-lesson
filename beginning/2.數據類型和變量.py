#\n表示换行，字符\本身也要转义，所以\\表示的字符就是\
print('I\'m learning\nPython.\\') 

#\t表示制表符，r''表示''內部的字符串默認不轉義
print('\\\t\\') 
print(r'\\\t\\')

##布爾值
print(3>2)
print(3<2 and 4>2)
print(3<2 or 4>2)
print (not 1>2)