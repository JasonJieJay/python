#coding=utf-8
import pymongo
conn=pymongo.MongoClient(host='127.0.0.1',port=27017)
db=conn.简历
def find1():
        while 1:
                print('*'*40)
                print('''
        查看已经录入的简历信息：
        输入a，按照名字进行查询
        输入b，按照电话进行查询
        输入c, 按照经历进行查询
        输入d, 查询全部简历信息
        输入q, 退出查询
                ''')
                print('*'*40)
                shuru=input('请输入您的选择: ')
                if shuru=='a':
                        while 1:
                                a=[]
                                name1=input('请输入您查询的名字:')
                                data1=db.简历.find({'name':name1},{'_id':0})
                                a = [x for x in data1 if name1 == x['name']]
                                if len(a) != 0:
                                        for i in a:
                                                print('名字:'+str(i['name'])+';         电话:'+str(i['tel'])+';         经历:'+str(i['jingli']))
                                        jx=input('输入任意键继续/退出本次查询输入q：')
                                        if jx == 'q':
                                                print('退出本次查询成功！')
                                                break
                                        else:
                                                print('请继续查询!')
                                else:
                                        jx=input('名字不存在！输入任意键继续/退出本次查询输入q：')
                                        if jx == 'q':
                                                print('退出本次查询成功！')
                                                break
                                        else:
                                                print('请继续查询!')
                elif shuru=='b':
                        while 1:
                                a=[]
                                tel1=input('请输入您查询的电话:')
                                data1=db.简历.find({'tel':tel1},{'_id':0})
                                a = [x for x in data1 if tel1 == x['tel']]
                                if len(a) != 0:
                                        for i in a:
                                                print('名字:'+str(i['name'])+';         电话:'+str(i['tel'])+';         经历:'+str(i['jingli']))
                                        jx=input('输入任意键继续/退出本次查询输入q：')
                                        if jx == 'q':
                                                print('退出本次查询成功！')
                                                break
                                        else:
                                                print('请继续查询!')
                                else:
                                        jx=input('电话不存在！输入任意键继续/退出本次查询输入q：')
                                        if jx == 'q':
                                                print('退出本次查询成功！')
                                                break
                                        else:
                                                print('请继续查询!')
                elif shuru=='c':
                        while 1:
                                a=[]
                                jingli1=input('请输入您查询的经历:')
                                data1=db.简历.find({'jingli':jingli1},{'_id':0})
                                a = [x for x in data1 if jingli1 == x['jingli']]
                                if len(a) != 0:
                                        for i in a:
                                                print('名字:'+str(i['name'])+';         电话:'+str(i['tel'])+';         经历:'+str(i['jingli']))
                                        jx=input('输入任意键继续/退出本次查询输入q：')
                                        if jx == 'q':
                                                print('退出本次查询成功！')
                                                break
                                        else:
                                                print('请继续查询!')
                                else:
                                        jx=input('经历不存在！输入任意键继续/退出本次查询输入q：')
                                        if jx == 'q':
                                                print('退出本次查询成功！')
                                                break
                                        else:
                                                print('请继续查询!')
                elif shuru=='d':
                        data=db.简历.find()
                        for i in data:
                                print('名字:'+str(i['name'])+';         电话:'+str(i['tel'])+';         经历:'+str(i['jingli']))
                elif shuru=='q':
                        print('退出查询成功！')
                        break
                else:
                        print('您的输入有误!请重新输入！')
if __name__ == '__main__':
        find1()
=============================================================================================
#coding=utf-8
import pymongo
conn=pymongo.MongoClient(host='127.0.0.1',port=27017)
db=conn.简历
def insert1():
        while 1:
                name1=input('请输入要添加的名字：')
                data=db.简历.find({'name':name1},{'_id':0})
                a = [x for x in data if name1 == x['name']]
                if len(a) == 0:
                        tel=input('请输入您要添加的电话：')
                        jingli=input('请输入添加的工作经历：')
                        su=input('确信信息无误输入yes/输入任意键放弃此次添加且退出：')
                        if su=='yes':
                                db.简历.insert({'name':name1,'tel':tel,'jingli':jingli})
                                print('添加成功!')
                                jixu=input('退出按q/其他任意键继续添加：')
                                if jixu == 'q':
                                        print('退出添加成功！')
                                        break
                        else:
                                print('放弃添加且退出！')
                                break
                else:
                        print('名字已存在！')
                        for i in a:
                                print('名字:'+str(i['name'])+';         电话:'+str(i['tel'])+';         经历:'+str(i['jingli']))
                        jixu=input('退出按q/其他任意键继续添加：')
                        if jixu == 'q':
                                print('退出添加成功！')
                                break
                        else:
                                tel=input('请输入要添加的电话：')
                                jingli=input('请输入要添加的经历：')
                                su=input('确信信息无误输入yes/输入任意键放弃此次添加且退出：')
                                if su=='yes':
                                        db.简历.insert({'name':name1,'tel':tel,'jingli':jingli})
                                        print('添加成功!')
                                        jixu=input('退出按q/其他任意键继续添加：')
                                        if jixu == 'q':
                                                print('退出添加成功！')
                                                break
                                else:
                                        print('放弃添加且退出！')
                                        break
if __name__=='__main__':
        insert1()
====================================================================================================
#coding=utf-8
import pymongo
conn=pymongo.MongoClient(host='127.0.0.1',port=27017)
db=conn.简历
def update1():
        while 1:
                print('*'*40)
                print('''
        修改已经录入的简历信息：
        输入a，查询名字进入修改
        输入b，查询电话进入修改
        输入q, 退出修改
                ''')
                print('*'*40)
                shuru=input('请输入您的选择: ')
                if shuru=='a':
                        while 1:
                                name1=input('请输入要修改的名字：')
                                data=db.简历.find({'name':name1},{'_id':0})
                                a = [x for x in data if name1 == x['name']]
                                if len(a) == 0:
                                        print('名字不存在！')
                                        jixu=input('退出按q/其他任意键继续：')
                                        if jixu == 'q':
                                                print('退出修改成功！')
                                                break
                                        else:
                                                print('继续修改')
                                else:
                                        for i in a:
                                                print('名字:'+str(i['name'])+';         电话:'+str(i['tel'])+';         经历:'+str(i['jingli']))
                                        tel1=input('请输入要修改的新电话：')
                                        jingli1=input('请输入要修改的新经历：')
                                        su=input('确认信息无误输入y/按任意键放弃修改：')
                                        if su=='y':
                                                data=db.简历.update({'name':name1},{'$set':{'tel':tel1,'jingli':jingli1}})
                                                print('修改成功！')
                                        else:
                                                print('放弃修改！')
                                                break
                elif shuru=='b':
                        while 1:
                                tel1=input('请输入要修改的电话：')
                                data=db.简历.find()
                                a = [x for x in data if tel1 == x['tel']]
                                if len(a) == 0:
                                        print('电话不存在！')
                                        jixu=input('退出按q/其他任意键继续：')
                                        if jixu == 'q':
                                                print('退出修改成功！')
                                                break
                                        else:
                                                print('继续修改')
                                else:
                                        for i in a:
                                                print('名字:'+str(i['name'])+';         电话:'+str(i['tel'])+';         经历:'+str(i['jingli']))
                                        name1=input('请输入要修改的新姓名：')
                                        jingli1=input('请输入要修改的新经历：')
                                        su=input('确认信息无误输入y/按任意键放弃修改：')
                                        if su=='y':
                                                data=db.简历.update({'tel':tel1},{'$set':{'name':name1,'jingli':jingli1}})
                                                print('修改成功！')
                                        else:
                                                print('放弃修改！')
                                                break
                elif shuru=='q':
                        print('退出修改成功！')
                        break
                else:
                        print('您的输入有误,请重新输入！')
if __name__=='__main__':
        update1()
=====================================================================================================
#coding=utf-8
import pymongo
conn=pymongo.MongoClient(host='127.0.0.1',port=27017)
db=conn.简历
def remove1():
        while 1:
                print('*'*40)
                print('''
        删除已经录入的简历信息：
        输入a，按照名字进行删除
        输入b，按照电话进行删除
        输入c, 按照经历进行删除
        输入d, 删除全部简历
        输入q, 退出删除
        ''')
                print('*'*40)
                shuru=input('请输入您的选择: ')
                if shuru=='a':
                        name1=input('请输入您删除的名字：')
                        data1=db.简历.find({'name':name1},{'_id':0})
                        a = [x for x in data1 if name1 == x['name']]
                        if len(a) != 0:
                                for i in a:
                                        print('名字:'+str(i['name'])+';         电话:'+str(i['tel'])+';         经历:'+str(i['jingli']))
                                su=input('确认删除输入y/按任意键放弃删除：')
                                if su=='y':
                                        data=db.简历.remove({'name':name1})
                                        print('删除成功！')
                                        jx=input('输入任意键继续删除/退出删除输入q：')
                                        if jx == 'q':
                                                print('退出删除成功！')
                                                break
                                else:
                                        print('放弃本次删除!')
                                        break
                        else:
                                print('名字不存在！')
                                jx=input('输入任意键继续删除/退出删除输入q：')
                                if jx == 'q':
                                        print('退出删除成功！')
                                        break
                                else:
                                        print('请继续删除!')
                elif shuru=='b':
                        tel1=input('请输入您删除的号码：')
                        data1=db.简历.find({'tel':tel1},{'_id':0})
                        a = [x for x in data1 if tel1 == x['tel']]
                        if len(a) != 0:
                                for i in a:
                                        print('名字:'+str(i['name'])+';         电话:'+str(i['tel'])+';         经历:'+str(i['jingli']))
                                su=input('确认删除输入y/按任意键放弃删除：')
                                if su=='y':
                                        data=db.简历.remove({'tel':tel1})
                                        print('删除成功！')
                                        jx=input('输入任意键继续删除/退出删除输入q：')
                                        if jx == 'q':
                                                print('退出删除成功！')
                                                break
                                else:
                                        print('放弃本次删除!')
                                        break
                        else:
                                print('名字不存在！')
                                jx=input('输入任意键继续删除/退出删除输入q：')
                                if jx == 'q':
                                        print('退出删除成功！')
                                        break
                                else:
                                        print('请继续删除!')
                elif shuru=='c':
                        jingli1=input('请输入您删除的经历：')
                        data1=db.简历.find({'jingli':jingli1},{'_id':0})
                        a = [x for x in data1 if jingli1 == x['jingli']]
                        if len(a) != 0:
                                for i in a:
                                        print('名字:'+str(i['name'])+';         电话:'+str(i['tel'])+';         经历:'+str(i['jingli']))
                                su=input('确认删除输入y/按任意键放弃删除：')
                                if su=='y':
                                        data=db.简历.remove({'jingli':jingli1})
                                        print('删除成功！')
                                        jx=input('输入任意键继续删除/退出删除输入q：')
                                        if jx == 'q':
                                                print('退出删除成功！')
                                                break
                                else:
                                        print('放弃本次删除!')
                                        break
                        else:
                                print('名字不存在！')
                                jx=input('输入任意键继续删除/退出删除输入q：')
                                if jx == 'q':
                                        print('退出删除成功！')
                                        break
                                else:
                                        print('请继续删除!')
                elif shuru=='d':
                        su=input('确认删除全部简历输入y/按任意键退出：')
                        if su=='y':
                                data=db.简历.remove()
                                print('全部简历删除成功！')
                        else:
                                print('请继续删除!')
                elif shuru=='q':
                        print('退出删除成功！')
                        break
                else:
                        print('您的输入有误,请重新输入！')
if __name__=='__main__':
        remove1()
