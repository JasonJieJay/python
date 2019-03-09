#coding=utf-8
import csv

def 存在():
    name=input('请输入名字:')
    with open('/home/jason/python/test1.csv','r') as f:
        reader=f.readlines()
        while True:
            a = [x for x in reader if x[0]==name]
            if len(a)==0:
                print('名字不存在，请重新输入！')
                name=input('请输入名字:')
            else:
                break
    return name

def 不存在():
    name=input('请输入名字:')
    with open('/home/jason/python/test1.csv','r') as f:
        reader=f.readlines()
        while True:
            a = [x for x in reader if x[0]==name]
            if len(a)!=0:
                print('名字存在，请重新输入！')
                name=input('请输入名字:')
            else:
                break
    return name

def 查询(): 
    name=存在()
    with open('/home/jason/python/test1.csv','r') as f:
        reader=f.readlines()
        for i in reader:
            i=i.strip('\n')
            if i[0] == name:
                print(i)
def 修改():
    name=存在()
    with open('/home/jason/python/test1.csv','r') as f:
        reader=f.readlines()
    with open('/home/jason/python/test1.csv','w') as x:
        file=csv.writer(x,dialect='excel')
        for l in reader:
            if l[0] != name:
                l=l.strip('\n')
                l=l.split(',')
                file.writerow(l)
            else:
                num=input('请输入tel:')
                um1=[name,num]
                file.writerow(um1)
                print('修改成功！')

def 删除():
    name=存在()
    with open('/home/jason/python/test1.csv','r') as f:
        reader=f.readlines()
    with open('/home/jason/python/test1.csv','w') as d:
        for a in reader:
            if name != a[0]:
                d.write(a)
        print('删除成功')

def 新增():
    name=不存在()
    num=input('请输入tel:')
    with open('/home/jason/python/test1.csv','a') as x:
        file=csv.writer(x,dialect='excel')
        list1=[name,num]
        file.writerow(list1)
    print('新增成功')

def fun1():
    while True:
        type1=int(input('新增输入:1；删除输入:2；修改输入:3；查询输入:4\n'))
        if type1==4:
            查询()
        elif type1==3:
            修改()
        elif type1==2:
            删除()
        elif type1==1:
            新增()
        else:
            print('输入有误！重新输入！')

if __name__=="__main__":
    fun1()
