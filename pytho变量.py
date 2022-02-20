'''
1 什么是变量
变量是指各种类型的值的名字
变量的命名规则：
变量由字母数字下划线组成，开头不能写数字，变量名最好见名知意

'''
'''
Hello='hello word'
print(Hello)
'''
'''
Hello 是创建的变量，=是赋值语， 和hello word 是变量值
'''
'''
同一变量可以多次赋值

'''
'''
a=666
print(a)
a='hello'
print(a)
'''
'''
print(type('hello'))
print(type(123))
print(type('123'))
'''
'''
还可以照一下方法定义变量：
'''
'''
a='xianchao'
b=a
a='hello word'
print(b)
print(a)
'''
'''
import keyword
print(keyword.kwlist)
'''
'''
上面的执行结果会把关键字显示出来
'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

'''
