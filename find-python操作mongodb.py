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

