'''
#私有化属性表示方法(不能进行访问)
class student:
    def __init__(self):
        self.__number=30

banji=student()
print(banji.__number)
'''
#私有化属性访问方法
class student:
    def __init__(self,num):
        self.__num=num
    def print_age(self):
        print('your age is %d'%self.__num)

age=student(30)
age.print_age()
