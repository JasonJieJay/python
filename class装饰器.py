#coding=utf-8
#带有参数的装饰器
import time
def dec(func):
	def jisuan(a,b):
		starttime=time.time()
		func(a,b)
		endtime=time.time()
		sec=endtime-starttime
		print('time is %d s'%sec)
	return jisuan

@dec
def func(a,b):
	print('a+b=?')
	time.sleep(1)
	print('its',a+b)

f=func
f(4,5)

#=====================================================================================

#装饰器例子
import time
def jisuan(func):
	def zsq():
		starttime=time.time()
		func()
		endtime=time.time()
		sec=endtime-starttime
		print('消耗的时间为%d'%sec)
	return zsq
@jisuan
def func():
	print('hello')
	time.sleep(1)
	print('world!')

f=func
f()

#==================================================================================

#私有化属性方法
class student:
	def __init__(self):
		self.__number=30

banji=student()
print(banji.__number)

#=====================================================================================
#私有化属性访问方法
class student:
	def __init__(self,num):
		self.__num=num
	def print_age(self):
		print('your age is %d'%self.__num)

age=student(30)
age.print_age()
