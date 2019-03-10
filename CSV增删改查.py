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
    while True:
        name=存在()
        with open('/home/jason/python/test1.csv','r') as f:
            reader=f.readlines()
            for i in reader:
                i=i.strip('\n')
                if i[0] == name:
                    print('名字:',i[0],'   电话:',i[2])               
            jx=input('输入任意键继续/输入q退出：')
            if jx!='q':
                print('请继续查询!')
            else:
                print('退出查询！')
                break
def 修改():
    while True:
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
            jx=input('输入任意键继续/输入q退出：')
            if jx!='q':
                print('请继续查询!')
            else:
                print('退出查询！')
                break

def 删除():
    while 1:
        name=存在()
        with open('/home/jason/python/test1.csv','r') as f:
            reader=f.readlines()
        with open('/home/jason/python/test1.csv','w') as d:
            for a in reader:
                if name != a[0]:
                    d.write(a)
            print('删除成功')
            jx=input('输入任意键继续/输入q退出：')
            if jx!='q':
                print('请继续查询!')
            else:
                print('退出查询！')
                break

def 新增():
    while 1:
        name=不存在()
        num=input('请输入tel:')
        with open('/home/jason/python/test1.csv','a') as x:
            file=csv.writer(x,dialect='excel')
            list1=[name,num]
            file.writerow(list1)
        print('新增成功')
        jx=input('输入任意键继续/输入q退出：')
        if jx!='q':
            print('请继续查询!')
        else:
            print('退出查询！')
            break

def fun1():
    while True:
        print('*'*26)
        print('''
        新增输入:z
        删除输入:s
        修改输入:x
        查询输入:c
        退出输入:q
        ''')
        print('*'*26)
        type1=input('请选择操作方式：')
        if type1=='c':
            查询()
        elif type1=='x':
            修改()
        elif type1=='s':
            删除()
        elif type1=='z':
            新增()
        elif type1=='q':
            print('退出程序成功！')
            break
        else:
            print('输入有误！重新输入！')

if __name__=="__main__":
    fun1()
