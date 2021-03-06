课程目标
掌握函数定义和调用的方法

课程内容
a.什么是函数
b.python中函数的定义
c.函数的调用


a.什么是函数
做开发时候需要使用指定的代码多次，为了提高代码的效率和重用性，所以把具有多利功能的代码组织为一个模块，给这个功能一个名字，就是函数
函数可以使用系统自带函数，也可以使用自定义函数

例子：登录网站
1.打开网页
2.点击用户名输入框
3.清空用户名输入框
4.输入用户名信息
5.点击密码输入框
6.清空密码输入框
7.输入密码信息
8.点击登录


[1]
1.打开网页
2.输入用户名信息
	点击xx
	清空xx
	填写xx
3.输入密码信息
	点击xx
	清空xx
	填写xx
4.登录

[2]
定义函数
函数实现的功能：输入信息(信息类型，信息)
信息类型： 用户名  密码
信息：     填写的用户名信息  填写的密码信息

定义函数
输入信息(信息类型，信息)
	点击  信息类型 输入框
	清空  信息类型 输入框
	填写  信息

1.打开网页
2.调用函数 输入信息(用户名,chui)
3.调用函数 输入信息(密码,123456)
4.点击登录


b.python中函数的定义
语法：
	def 函数名字():
		函数的主体
例子:
	def print_name():
		print('its big chui!')

c.函数的调用
	函数名
	print_name()

内置函数可以直接使用，调用一个函数需要函数名字和参数，函数名字是一个函数对象的引用，也可以把函数赋值给变量
l=[1,2,3,4]
b=len
num=b(l)
print('列表中的元素数量为:',num)

××××××××例子**********************************************
#coding=utf-8
def print_name():
	print('its big chui!')

print_name()

l=[1,2,3,4]
b=len
num=b(l)
print('列表中的元素数量为:',num)

================函数的常用格式======return语句=================================================================================================
学习目标
掌握函数的常用格式

课程内容
a.函数的常用类型
b.常用类型实例

a.函数的常用类型
	1.无参数，无返回值(自己工作，散养)
	2.无参数，有返回值(主动发周报)
	3.有参数，无返回值(领导安排任务，不管效果)
	4.有参数，右返回值(领导安排任务，要求汇报完成情况)

b.常用的类型实例
	1.无参数，无返回值
	def print_hello():
	        print('hello!')
	2.无参数，有返回值
	def sleep():
		return 'im sleeping'
	3.有参数，无返回值
	def sub(x,y):
	        print('x+y=',x+y)
	4.有参数，有返回值
	def sub(x,y):
return x+y

学习目标
掌握函数返回值的用法

课程内容
a.返回值的定义
b.return和print区别
c.return语句

a.返回值的定义
函数定义时候是直接输出，有时候需要处理一些函数，根据参数进行一系列操作，需要返回值

b.return和print区别
return作用是返回计算的值(结果)，需要print才能打印出来
print作用是输出数据到控制端

c.return语句
一般来说用于退出函数，return下面的语句是不会执行的
一个返回值
def sum(a,b):
        jisuan=a+b
        return jisuan



a=sum(20,30)
print(a)
~            
多个返回值
def ret(a,b):
        a*=10
        b*=10
        return a,b
num=ret(5,7)
print(num)
print(type(num))

num1,num2=ret(30,50)
print(num1,num2)

*************例子××××××××××××××××××××××××××××××××××××××××××
#coding=utf-8
def sum(a,b):
	jisuan=a+b
	return jisuan

a=sum(20,30)
print(a)

def ret(a,b):
	a*=10
	b*=10
	return a,b
num=ret(5,7)
print(num)
print(type(num))

num1,num2=ret(30,50)
print(num1,num2)
#coding=utf-8
def print_hello():
	print('hello!')

print_hello()


def sleep():
	return 'im sleeping!'

s=sleep()
print(s)

def sub(x,y):
	print('x+y=',x+y)
sub(2,3)

def sub(x,y):
	return x+y
b=sub(20,30)
print(b)

=====================函数的传参======================================================================

学习目标
掌握函数的参数传递的方法

课程内容
a.函数的形参和实参
b.参数传递-实参位置
c.参数传递-关键字参数
d.参数传递-参数默认值
e.参数传递-不定长参数



a.函数的形参和实参
def print_name(name):
	print('your name is %s'% name)

print_name('o8ma!')
例子中形参为定义函数时候括号中的name，实参是调用函数时候传入的'o8ma!'
定义在函数体内参数是形参，调用时候传入参数是实参

b.参数传递-实参位置
函数允许定义多个形参，也可以包含多个实参，通过形参和实参对应顺序就是参数位置，只有位置一致才能匹配
def animal(pet1,pet2):
        print(pet1+'wang!'+pet2+'miao')

#调用函数时候传入2个参数
animal('dog','cat')
animal('cat','dog')

c.参数传递-关键字参数
关键字传递函数名称-值对，直接在形参中把名称和值对应起来就不会混淆
def animal(pet1,pet2):
        print(pet1+'  wang!!  '+pet2+'  miao!')

animal(pet2='cat',pet1='2ha')

d.参数的默认值
函数定义时候设置函数形参，每个形参有默认值，当函数在调用时候，如果没有实参，就是形参默认值

def animal(pet2,pet1='2ha'):
        print(pet1+'  wang!!  '+pet2+'  miao!')

animal('bosi')
animal('jiafei','taidi')


e.参数传递-不定长参数
有时函数处理比当初声明更多的参数叫做不定长参数
*args位置参数传入数据装配成元组类型
def test(x,y,*args):
        print(x,y,args)

test(1,2,'heogr','song')

**args位置参数传入数据装配为字典类型
def test1(x,y,**args):
        print(x,y,args)

test1(1,2,a=10,b='heygor')

********例子**********************************************************

#coding=utf-8
def animal(pet1,pet2):
	print(pet1+'wang!'+pet2+'miao')

#调用函数时候传入2个参数
animal('dog','cat')
animal('cat','dog')


def animal(pet1,pet2):
	print(pet1+'  wang!!  '+pet2+'  miao!')

animal(pet2='cat',pet1='2ha')

def animal(pet2,pet1='2ha'):
	print(pet1+'  wang!!  '+pet2+'  miao!')

animal('bosi')
animal('jiafei','taidi')


print('************')
def test(x,y,*args):
	print(x,y,args)

test(1,2,'heogr','song')

def test1(x,y,**args):
	print(x,y,args)

test1(1,2,a=10,b='heygor')

==========================变量作用域===============================================================

学习目标
掌握变量作用域概念及用法

课程内容
a.全局变量和局部变量
b.局部变量
c.全局变量

a.全局变量和局部变量
全局变量:定义在函数外的变量
局部变量:定义在函数内部的变量
获取变量值的时候，先获取当前作用域名称和变量值，如果没有找到，到上一层变量作用域搜索变量的值，再没有就报错

b.局部变量
def test1():
        a=10
        print('修改前a的值是',a)
        a=20
        print('修改后a的值是',a)

def test():
        a=40
        print('我是test中的a',a)

test1()
test()
注意：不同函数可以定义相同变量的名字(局部变量)，互相不影响

c.全局变量
声明在函数外的变量
a=100
print('a的值是',a)

def test1():
        a=20
        print('tes1中a的值是',a)

def test2():
        print('test2中a的值是',a)

test1()
test2()
补充：当全局变量和局部变量同名时，优先使用局部变量

修改全局变量

a=100
print('a的值是',a)

def test1():
        global a
        a=200
        print('test1中修改全局变量为a',a)

def test2():
        print('test2中使用全局变量a',a)

test1()
test2()

*******例子*********************************************

#coding=utf-8

'''
def test1():
	a=10
	print('修改前a的值是',a)
	a=20
	print('修改后a的值是',a)
def test():
	a=40
	print('我是test中的a',a)
test1()
test()
'''
'''
a=100
print('a的值是',a)
def test1():
	a=20
	print('tes1中a的值是',a)
def test2():
	print('test2中a的值是',a)
test1()
test2()
'''

a=100
print('a的值是',a)

def test1():
	global a
	a=200
	print('test1中修改全局变量为a',a)

def test2():
	print('test2中使用全局变量a',a)

test1()
test2()


================================函数的递归=============================================================

学习目标
掌握函数递归的定义和实例

课程内容
a.什么是递归
b.递归函数操作

a.什么是递归
递归函数就是子程序(或者函数)直接调用自己或者通过一系列语句间接调用自己描述问题和解决问题办法(自己调用自己)

递归函数特性
1.必须有一个明确结束的条件
2.每次进入到更深一层递归时候，问题规模比上次递归有减少
3.相邻2次重复间有紧密联系，前一次为后一次准备(通常前一次的输出作为后一次的输入)
4.递归的效率不高，递归层次过多会导致栈溢出(最大递归层数997)

b.递归函数操作

×××××××××××××例子×××××××××××××××××××××××××××××××××××××××××××××××××××××××××××

#coding=utf-8
#嵌套函数
'''
def t1():
	print('im t1!')
def t2():
	t1()
	print('im t2')
def t3():
	t2()
	print('im t3')
t3()
'''
#例子:阶乘   n!=1*2*3*.....

def func(n):
	if n==1:
		return n
	elif n>1:
		return n*func(n-1)
	else:
		return '请传递大于0的参数'

print(func(5))
#相当于5的阶乘  1*2*3*4*5=120
'''
==(5)
	==(5*func(4))
		==(4*func(3))
			...
'''

#例子：盗梦空间
def func(n):
	print('进入到%d层梦'%n)
	if n==3:
		print('进入到潜意识区')
	else:
		func(n+1)
	print('从第%d层梦中醒来'%n)

func(1)




========================匿名函数===========================================================================

学习目标
掌握匿名函数的用法

课程内容
a.什么是匿名函数
b.匿名函数的用法


a.什么是匿名函数
函数在定义过程中，没有给定函数名，python中使用lambda来创建匿名函数
lambda只是表达式，函数体比def简单
lambda主体是表达式不是代码块，仅能在lambda表达式中封装有限逻辑进去
lambda有自己的命名空间，不能访问自己参数列表外或者全局命名空间的参数

b.匿名函数的用法
lambda 参数列表:变量[表达式]

加法
sum=lambda a1,a2:a1+a2
print(sum(10,20))

字典排序
stu=[{'name':'tom','age':18},{'name':'jerry','age':20},{'name':'snoopy','age':6}]
stu.sort(key=lambda x:x['age'])
print(stu)

把lambda当作变量使用
def operation(a,b,opt):
        re=opt(a,b)
        return re

num1=int(input('num1'))
num2=int(input('num2'))
res=operation(num1,num2,lambda a,b:a+b)
print(res)

×××××××××××××××××××××例子×××××××××××××××××××××××××××××××××××××××××××××××××××××××××××88××

#coding=utf-8

sum=lambda a1,a2:a1+a2
print(sum(10,20))

stu=[{'name':'tom','age':18},{'name':'jerry','age':20},{'name':'snoopy','age':6}]
stu.sort(key=lambda x:x['age'])
print(stu)

def operation(a,b,opt):
	re=opt(a,b)
	return re

num1=int(input('num1'))
num2=int(input('num2'))
res=operation(num1,num2,lambda a,b:a+b)
print(res)
