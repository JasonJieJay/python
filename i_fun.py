def he():
    import pymysql
    global conn,cur
    conn=pymysql.connect(host='localhost',user='root',passwd='jiejay',db='project',port=3306,charset='utf8')
    cur=conn.cursor()


def wen1(a):
    print('''
===========
%s
===========





'''%a)

def leix(b):
    while 1:
            try:
                a=int(input('''劳驾输入%s:'''%b))
            except ValueError as v:
                print(''' 

%s应为数字类型Y(^_^)Y
'''%b)
            else:
                return a
                break

def In_T():
    while 1:
        a=leix('电话号码')
        sql1 = "select tel from person where tel='%d'"%a
        cur.execute(sql1)
        fl=cur.fetchall()
        if fl!=():
            print('电话号码已存在，请重新输入哦')
        else:
            return a


def rq(a):
    import datetime
    while 1:
        y=leix('%s年份(如:1996)'%a)
        m=leix('%s月份(1-12)'%a)
        d=leix('%s日期(1-30)'%a)
        try:
            a=datetime.date(y,m,d)
        except ValueError as v1:
            print('''
--------------------------------
不要调皮哦，请如实填写年、月、日~
''')
        else:
            return a


def SaN(t,q):
    z='%'
    #sql1 = "select name from %s where name like '%s%s'"%(t,q,z)
    sql1 = '''SELECT name FROM %s WHERE (name='%s') or (name like '%s_' and name REGEXP "[0-9]") or (name like '%s__' and name REGEXP "10") or (name like '%s__' and name REGEXP "11") or (name like '%s__' and name REGEXP "12") or (name like '%s__' and name REGEXP "13") or (name like '%s__' and name REGEXP "14") or (name like '%s__' and name REGEXP "15") or (name like '%s__' and name REGEXP "16") or (name like '%s__' and name REGEXP "17") or (name like '%s__' and name REGEXP "18") or (name like '%s__' and name REGEXP "19") or (name like '%s__' and name REGEXP "20") or (name like '%s__' and name REGEXP "21") or (name like '%s__' and name REGEXP "22") or (name like '%s__' and name REGEXP "23") or (name like '%s__' and name REGEXP "24") or (name like '%s__' and name REGEXP "25") or (name like '%s__' and name REGEXP "26") or (name like '%s__' and name REGEXP "27") or (name like '%s__' and name REGEXP "28") or (name like '%s__' and name REGEXP "29") or (name like '%s__' and name REGEXP "30") or (name like '%s__' and name REGEXP "31") or (name like '%s__' and name REGEXP "32") or (name like '%s__' and name REGEXP "33") or (name like '%s__' and name REGEXP "34") or (name like '%s__' and name REGEXP "35") or (name like '%s__' and name REGEXP "36") or (name like '%s__' and name REGEXP "37") or (name like '%s__' and name REGEXP "38") or (name like '%s__' and name REGEXP "39") or (name like '%s__' and name REGEXP "40") or (name like '%s__' and name REGEXP "41") or (name like '%s__' and name REGEXP "42") or (name like '%s__' and name REGEXP "43") or (name like '%s__' and name REGEXP "44") or (name like '%s__' and name REGEXP "45") or (name like '%s__' and name REGEXP "46") or (name like '%s__' and name REGEXP "47") or (name like '%s__' and name REGEXP "48") or (name like '%s__' and name REGEXP "49") or (name like '%s__' and name REGEXP "50") or (name like '%s__' and name REGEXP "51") or (name like '%s__' and name REGEXP "52") or (name like '%s__' and name REGEXP "53") or (name like '%s__' and name REGEXP "54") or (name like '%s__' and name REGEXP "55") or (name like '%s__' and name REGEXP "56") or (name like '%s__' and name REGEXP "57") or (name like '%s__' and name REGEXP "58") or (name like '%s__' and name REGEXP "59") or (name like '%s__' and name REGEXP "60") or (name like '%s__' and name REGEXP "61") or (name like '%s__' and name REGEXP "62") or (name like '%s__' and name REGEXP "63") or (name like '%s__' and name REGEXP "64") or (name like '%s__' and name REGEXP "65") or (name like '%s__' and name REGEXP "66") or (name like '%s__' and name REGEXP "67") or (name like '%s__' and name REGEXP "68") or (name like '%s__' and name REGEXP "69") or (name like '%s__' and name REGEXP "70") or (name like '%s__' and name REGEXP "71") or (name like '%s__' and name REGEXP "72") or (name like '%s__' and name REGEXP "73") or (name like '%s__' and name REGEXP "74") or (name like '%s__' and name REGEXP "75") or (name like '%s__' and name REGEXP "76") or (name like '%s__' and name REGEXP "77") or (name like '%s__' and name REGEXP "78") or (name like '%s__' and name REGEXP "79") or (name like '%s__' and name REGEXP "80") or (name like '%s__' and name REGEXP "81") or (name like '%s__' and name REGEXP "82") or (name like '%s__' and name REGEXP "83") or (name like '%s__' and name REGEXP "84") or (name like '%s__' and name REGEXP "85") or (name like '%s__' and name REGEXP "86") or (name like '%s__' and name REGEXP "87") or (name like '%s__' and name REGEXP "88") or (name like '%s__' and name REGEXP "89") or (name like '%s__' and name REGEXP "90") or (name like '%s__' and name REGEXP "91") or (name like '%s__' and name REGEXP "92") or (name like '%s__' and name REGEXP "93") or (name like '%s__' and name REGEXP "94") or (name like '%s__' and name REGEXP "95") or (name like '%s__' and name REGEXP "96") or (name like '%s__' and name REGEXP "97") or (name like '%s__' and name REGEXP "98") or (name like '%s__' and name REGEXP "99");'''%(t,q ,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q,q)
    cur.execute(sql1)
    fl=cur.fetchall()
    #print(fl)
    if len(fl)!=0:
        p=q+'%d'%(len(fl)+1)
        print('该学生是系统内第%d个%s,姓名将被显示为%s'%(len(fl)+1,q,p))  
        return p  
    else:
        return q

def SaT(t,q):
    sql1 = "select tel from person where name='%s'"%q
    cur.execute(sql1)
    fl=cur.fetchall()
    if len(fl)!=0:
        p=q+'%d'%(len(fl)+1)
        print('该电话已存在，请重新输入')
        return p 



def Nav():
    print('''
    
----------------------------------------------------------------------         
    
    按1新增个人信息
    **************
    按2新增班级信息
    **************
    按3新增学习情况
    **************
    按4新增就业情况
    **************  
    按5新增跳槽情况
    **************  

						按任意键返回主菜单
					        **********************
----------------------------------------------------------------------
    ''')  
    global i
    i=input('在此键入:')







def ge():
    while 1:
        na=input('新增学员信息,姓名:')
        na=SaN('person',na)
        se=input('请输入性别:')
        co=input('请输入大学:')
        te=In_T()        
        cd=leix('班级id')
        print('''

刚才输入的学员信息是:
  姓名:%s    性别:%s   大学:%s
  电话:%s    班级id:%s 

'''%(na,se,co,te,cd))
        sql = "INSERT INTO `person`  VALUES ('0','%s','%s','%s','%d','%d');"%(na,se,co,te,cd)
        v=input('按1写入信息，按2重新新增学员信息，按其他任意键返回上一层')
        if v=='1':
            cur.execute(sql)
            conn.commit()
            vv=input('写入成功，按1继续增加 ,按任意键返回上一层')
            if vv=='1':
                continue
            else:
                break
        elif v=='2':
                print('重新新增')
        else:
            break


#2
def ban():
    while 1:
        wen1('新增班级信息')
        id1=leix('学生id')
        na=input('劳驾输入班名:')
        js=input('劳驾输入教室:')
        ke=input('劳驾输入课程:')
        print('''

刚才输入的班级信息是:
    学生id:   班名:%s   教室:%s   课程:%s  

'''%(na,js,ke))
        sql = "INSERT INTO `class`  VALUES (%d,'0','%s','%s','%s');"%(id1,na,js,ke)
        v=input('按1写入信息，按2重新新增学员信息，按其他任意键返回上一层')
        if v=='1':
            cur.execute(sql)
            conn.commit()
            vv=input('写入成功，按1继续增加 ,按任意键返回上一层')
            if vv=='1':
                continue
            else:
                break
        elif v=='2':
                print('重新新增')
        else:
            break



#3
def st():
    while 1:
        wen1('新增学习情况')
        id1=leix('学生id')
        na=input('''请输入学生姓名:''')
        na=SaN('study',na)
        cid=leix('班级id')
        
        gr=leix('学生成绩')
        la=leix('迟到几次？')
        vod=leix('调皮了几次呢')


        print('''

刚才输入的学习情况:
   学生id:%d     学生姓名:%s    班级:%d  
   学生成绩:%d   迟到次数:%d    违纪次数:%d  

'''%(id1,na,cid,gr,la,vod) )
        sql = "INSERT INTO `study`  VALUES (%d,'%s',%d,%d,%d,%d);"%(id1,na,cid,gr,la,vod)
        v=input('按1写入信息，按2重新新增学员信息，按其他任意键返回上一层')
        if v=='1':
            cur.execute(sql)
            conn.commit()
            vv=input('写入成功，按1继续增加 ,按任意键返回上一层')
            if vv=='1':
                continue
            else:
                break
        elif v=='2':
                print('重新新增')
        else:
            break



#4
def oe():
    while 1:
        wen1('新增就业情况')
        print('''

做好心理准备，您将要输入 id、姓名、毕业时间、工作时间和就业公司 ^_^
''')
        id1=leix('学生id哈~')
        na=input('学生姓名:')
        na=SaN('oe',na)
        gt=rq('毕业')
        print('得嘞 ～ 接下来输入工作时间')
        ot=rq('工作')
        sa=leix('每月拿多少钱？')
        com=input('公司:')


        print('''

刚才输入的就业情况:
   学生id:%d   学生姓名:%s   毕业时间:%s 
 
   工作时间:%s  薪水:%d  公司:%s  

'''%(id1,na,gt,ot,sa,com) )
        sql = "INSERT INTO `oe`  VALUES (%d,'%s','%s','%s',%d,'%s');"%(id1,na,gt,ot,sa,com) 
        v=input('按1写入信息，按2重新新增学员信息，按其他任意键返回上一层')
        if v=='1':
            cur.execute(sql)
            conn.commit()
            vv=input('写入成功，按1继续增加 ,按任意键返回上一层')
            if vv=='1':
                continue
            else:
                break
        elif v=='2':
                print('重新新增')
        else:
            break


#5
def jh():
    while 1:
        wen1('新增跳槽情况')
        id1=leix('朋友的id')
        na=input('请输入学生姓名:')
        na=SaN('jh',na)
        jc=input('跳槽至公司:')
        
        jt=rq('跳槽')
        sa=leix('跳槽后工资')
        print('''

刚才输入的的跳槽情况:
   学生id:%d    学生姓名:%s   跳槽至公司:%s 
   跳槽时间:%s  薪水:%d  

'''%(id1,na,jc,jt,sa) )
        sql = "INSERT INTO `jh`  VALUES (%d,'%s','%s',%d,'%s');"%(id1,na,jc,sa,jt)
        v=input('按1写入信息，按2重新新增学员信息，按其他任意键返回上一层')
        if v=='1':
            cur.execute(sql)
            conn.commit()
            vv=input('写入成功，按1继续增加 ,按任意键返回上一层')
            if vv=='1':
                continue
            else:
                break
        elif v=='2':
                print('重新新增')
        else:
            break

