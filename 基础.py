'''
python3中有6种常见的数据类型
一：number（数字）
二：string（字符串）
三：list（列表）
四：tuple（元组）
五：sets（集合）
六：dictionary（字典）
'''

'''
不可变的数据类型有三种：number  tuple  string 
可变的数据类型有三种：list  sets  dictionary

'''

'''
一：number(数字)
number有四种类型：
int（整型） float（浮点型） complex（负数） bool（布尔）
1  int
    int常被称为整型或者整数  整数指正负整数不带小数点整数表示方法有四种：
    十进制     二进制     八进制     十六进制
    
'''
'''
print("66")
print(0b110110)
print(0o66)
print(0x66)
'''
'''
print(bin(66))
print(oct(66))
print(hex(66))
'''

'''
创造一个int类型的数
'''
'''
print(12)
print(int(12.1))
'''

'''
float浮点型，由整数和小数部分组成
11.2323
16.1
21.345
'''
'''
print(12.3)
print(float(12))
print(float('12'))
print(type(22))
print(type(12.33))
'''


'''
complex（复数）
复数有整数和虚 数组成，可以用a+bj或者complex（a+b）表示，复数的实部和虚部都是浮点型
'''
'''
print(complex(5,6))
'''
'''
变量：
'''
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

'''
运算符：
'''
'''
1  什么是python运算符？
    运算符是一种特殊符号的集合，通过运算符可以对各种数据类型的运算数进行计算
2  常见的运算符有那些？
    算数运算符  布尔运算符  赋值运算符  位运算符  身份运算符  成员运算符

'''

'''
1 算数运算符：
    常见的算数运算：  + -  *  %  /   **
    
'''
'''
a=20
b=10

c=a+b
print(c)

c=a-b
print(c)
c=a*b
print(c)
c=a/b
print(c)
c=a//b
print(c)
c=a%b
print(c)
c=a**b
print(c)
'''

'''
2  比较运算符：
    常见的比较运算符有那些：
     >   <   ==   >=  <=  !=  
     比较运算符比较的结果为真，返回true  比较结果为假，返回false
     
'''
'''
a=20
b=10

print(a>b)
print(a<b)
print(a==b)
print(a>=b)
print(a<=b)
print(a!=b)
'''

'''
3 f赋值运算符
    常见的赋值运算符：
    =  +=  -=   *=   /=   %=   **=   //=   
    ：=  海象运算符，可在表达式内部为变量赋值  在python3.8新增的运算符
    
'''
'''
a=20
b=10
c=a+b
print(c)

c==a    # 等同于c=c+a
print(c)

c*=a   #等同于c=c*a
print(c)


a=20
b=10
c/=a  # c/=a 等同于c=c/a
print(c)
'''

'''
a=20
b=10
c=30
c%=a    #等同于c=c%a
print(c)
'''


'''
a=20
b=10
c=30
c//=a    #等同于c=c//a
print(c)
'''

'''
4   位运算符
    按位运算符是吧数字看作二进制来计算， python中按位运算符有那些
    &   #按位与运算符
    |   #按位或运算符
    ^   #按位异或运算符
    ~   #按位取反运算符
    <<  #左移运算符
    >>  #有移运算符
    
'''
'''
a=60
b=13
print(bin(60))
print(bin(13))
'''
'''
60的二进制是 00111100
13的二进制是 00001101

00111100
00001101
----------
00001100    #计算的是 &参与运算的两个值，如果两个值为1,则为1,否则为0.
00111101    #计算的是| 运算，只要对应的位有一个为1,结果就是1
00110001    #计算^运算，当两个相对应的二进制位相异时，结果是1           
～00111100反 11000011    #计算～运算，对数据的每个二进制取反，吧1变成0 ，把0变成1
00111100    <<2  11110000#计算<< 运算 ，运算的各个二进制全部左移若干位数，由“<<”右边的数值指定位数，高位丢弃，低位补0
00111100    >>2  00001111#计算>> 运算 ，运算的各个二进制全部右移若干位数，由“>>”右边的数值指定移动的位数，低位丢弃，高位补0
'''
'''
a=60
b=13

print(bin(a&b))
print(bin(a|b))
print(bin(a^b))
print(bin(60<<2))
print(bin(60>>2))
'''

'''
5 逻辑运算符
    and     #布尔与 如果x为false ， x and y 返回false  否则返回y的计算值
    or      #布尔或 如果x为true, 它返回x的值 ，否则返回y的计算值
    not     #布尔非 如果x为true ，返回false,如果x为false,则返回true
    
'''
'''
x=True
y=False
print(x and y)

x=False
y=True
print(x and y)

x=False
y=False

print(x and y)


x=True
y=True
print(x and y)

x=True
y=False
print(x or y)

x=False
y=False
print(x or y)


x=True
print(not  x)

x=False

print(not x)
'''

'''
6   成员运算符
    测i试示例中是否包含某个成员，包括字符窜，列表  元组
    in  #如果在指定的序列中找到赋值返回true否则返回false  x在y序列中  ， 如果x在y序列中则返回true
    not in  #如果在指定的序列中没有找到赋值则返回true,否则返回false x不再y序列中
    
    
'''
'''
x=10
y=[1,2,3,4,5]
print(x in y)
print(x not in y)

x=1
y=[1,2,3,4,5]
print(x in y)
print(x not in y)
'''


'''
7 身份运算符
    is #判断两个标识符是否引用同一个对象  X IS Y ，类似于i的（x） == id（y） 如果引用的是同一个对象则返回true 否则返回false
    
    is not  #判断两个标识符是否引用来自不同对象  X is not Y ，类似于i的（x） ！= id（y） 如果引用的不是同一个对象则返回true 否则返回false
    
    id （）函数适用于获取对象夫人内存地址
    

'''

'''
x=20
y=10
print(id(x))
print(id(y))
print(x is y)
print(x is not  y)

y=20
print(x is y)
print(x is not y)
print(id(x))
print(id(y))

'''
'''
8 布尔运算符
    布尔运算符用于对布尔值进行运算，运算结果是一个布尔值
    and #当两个值都是true结果是true
    or  #只要有一个运算符是true,结果就是true
    not    #如果运算数是true not true就是false 如果运算符是false 则 not false就是true
'''

'''
python中的序列都可以进行一些特定的操作
包括：
索引（indexing）
分片（slicing）
序列相加（adding）
乘法（mutiplying）
成员资格
长度
最大值最小值


'''
'''
1 索引
    序列是python中最基本的数据结构，序列中的每个元素都翻配一个数字，代表它在序列中的位置（索引），第一个索引是0
，第二个索引是1,... 以此类推。序列中所有的元素都有编号，从0开始递增，可以通过编号的序列的元素进行访问，
'''
'''
greeting='hello'
greeting[0]
print(greeting[0])
print(greeting[1])
'''

'''
字符窜是由字符窜组成的序列，索引0指向第一个元素，索引1指向地二个元素。

'''
'''
greeting='hello'
print(greeting[-1])
print(greeting[-2])
'''
'''
通过上面可以看到，python序列也可以从右开始索引，最右边3的索引编号是-1
在python中，从左向右的索引为整数索引，从右向左索引为复数索引，最右边的索引值是-1,从右向左以此递减。

'''