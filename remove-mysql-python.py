==========建表加入自增student_id and class_id=============================================================================================
person
create table person (student_id  int primary key auto_increment,
name varchar(20),
sex  varchar(10),
college varchar(20),
tel  int,
class_id  int) charset=utf8;
insert into person values(0,'gaga','female','shenzhen university', 198,01),(0,'lily','female','nanjing university', 168,02),(0,'bobo','male','peking university', 133,03),(0,'yoyo','female','HK university', 136,04),(0,'jack','male','guangzhou university', 158,05);

class
create table class (class_id int primary key auto_increment, 
class_name varchar(20), 
classroom varchar(20),
coursetyppe varchar(20),student_id int) charset=utf8;
insert into class values(0,'java开发班','13c','java',1),(0,'测试班','13d','test',2),(0,'web开发班','13b','web',3),(0,'ui班','13e','ui',4),(0:,'ps班','13f','ps',5);

study
create table study (student_id int,
name varchar(20),
class_id int,
grade int,
late int,
vod int)charset=utf8;
insert into study values(1,'gaga',101,90,3,1),(2,'lily',102,92,4,3),(3,'bobo',103,93,2,2),(4,'yoyo',104,95,6,2),(5,'jack',105,96,5,2);

oe
create table oe (student_id int,
name varchar(20),
gr_time date,
occ_time date,
salary int,
occ_company varchar(20))charset=utf8;
insert into oe values(1,'gaga','2018-10-03','2018-10-28',10000,'tcl'),(2,'lily','2017-10-03','2017-10-28',16000,'huawei'),(3,'bobo','2016-10-03','2016-11-05',15000,'zhongxing'),(4,'yoyo','2016-08-22','2016-09-12',20000,'tencent'),(5,'jack','2019-01-20','2016-03-12',13000,'chuangwei');


jh
create table jh(student_id int,
name  varchar(20),
jh_company varchar(20),
jh_salary int,
jh_time date)charset=utf8;
insert into jh values(1,'gaga','fushikang',13000,'2019-10-01'),(2,'lily','huawei',17000,'2018-10-01'),(3,'bobo','tencent',22000,'2017-10-01'),(4,'yoyo','huawei',25000,'2017-08-02'),(5,'jack','tcl',14000,'2019-03-02');
=========3remove-mysql.py============================================================================================
#coding=utf-8
import pymysql
conn=pymysql.connect(host='localhost',user='root',passwd='jiejay',db='project',port=3306,charset='utf8') #设置链接参数
cur=conn.cursor() #获取游标
def remove_person_num(num1):
	while 1:
		try:
			num2=int(input('请输入您删除的%s：'%num1))
			cur.execute('select * from person where %s=%d'%(num1,num2)) #所需要执行的命令
			data=cur.fetchall() #获取执行语句的执行结果
			if len(data) != 0:
				for i in data:
					print('student_id:',i[0],'	名字:',i[1],'	性别:',i[2],'	大学:',i[3],'	电话:',i[4],'	班级:',i[5])
				su=input('确认删除输入y/按任意键放弃删除：')
				if su=='y':
					cur.execute('delete from person where %s=%d'%(num1,num2))
					print('删除成功！')
					conn.commit()
					jx=input('输入任意键继续删除/退出删除输入q：')
					if jx == 'q':
						print('退出删除成功！')
						break
					else:
						print('请继续删除!')	
				else:
					print('放弃本次删除!')
					break
			else:
				print('%s不存在！'%num1)
				jx=input('输入任意键继续删除/退出删除输入q：')
				if jx == 'q':
					print('退出删除成功！')
					break
				else:
					print('请继续删除!')
		except ValueError as e:
			print('输入有误，请重新输入！')
def remove_person_name():
	while 1:
		name1=input('请输入您删除的名字：')
		cur.execute('select * from person where name="%s"'%name1) #所需要执行的命令
		data=cur.fetchall() #获取执行语句的执行结果
		if len(data) != 0:
			for i in data:
				print('student_id:',i[0],'	名字:',i[1],'	性别:',i[2],'	大学:',i[3],'	电话:',i[4],'	班级:',i[5])
			su=input('确认删除输入y/按任意键放弃删除：')
			if su=='y':
				cur.execute('delete from person where name="%s"'%name1)
				print('删除成功！')
				conn.commit()
				jx=input('输入任意键继续删除/退出删除输入q：')
				if jx == 'q':
					print('退出删除成功！')
					break
				else:
					print('请继续删除!')	
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
def remove_class():
	while 1:
		try:
			num2=int(input('请输入您删除的class_id：'))
			cur.execute('select * from class where class_id=%d'%num2) #所需要执行的命令
			data=cur.fetchall() #获取执行语句的执行结果
			if len(data) != 0:
				for i in data:
					print('class_id:',i[0],'	班级名:',i[1],'	教室:',i[2],'	课程:',i[3],'	student_id:',i[4])
				su=input('确认删除输入y/按任意键放弃删除：')
				if su=='y':
					cur.execute('delete from class where class_id=%d'%num2)
					print('删除成功！')
					conn.commit()
					jx=input('输入任意键继续删除/退出删除输入q：')
					if jx == 'q':
						print('退出删除成功！')
						break
					else:
						print('请继续删除!')	
				else:
					print('放弃本次删除!')
					break
			else:
				print('class_id不存在！')
				jx=input('输入任意键继续删除/退出删除输入q：')
				if jx == 'q':
					print('退出删除成功！')
					break
				else:
					print('请继续删除!')
		except ValueError as e:
			print('输入有误，请重新输入！')
def remove_study():
	while 1:
		try:
			num2=int(input('请输入您删除的student_id：'))
			cur.execute('select * from study where student_id=%d'%num2) #所需要执行的命令
			data=cur.fetchall() #获取执行语句的执行结果
			if len(data) != 0:
				for i in data:
					print('student_id:',i[0],'	名字:',i[1],'	class_id:',i[2],'	成绩:',i[3],'	迟到:',i[4],'	违纪:',i[5])
				su=input('确认删除输入y/按任意键放弃删除：')
				if su=='y':
					cur.execute('delete from study where student_id=%d'%num2)
					print('删除成功！')
					conn.commit()
					jx=input('输入任意键继续删除/退出删除输入q：')
					if jx == 'q':
						print('退出删除成功！')
						break
					else:
						print('请继续删除!')	
				else:
					print('放弃本次删除!')
					break
			else:
				print('student_id不存在！')
				jx=input('输入任意键继续删除/退出删除输入q：')
				if jx == 'q':
					print('退出删除成功！')
					break
				else:
					print('请继续删除!')
		except ValueError as e:
			print('输入有误，请重新输入！')
def remove_study_name():
	while 1:
		name1=input('请输入您删除的名字：')
		cur.execute('select * from study where name="%s"'%name1) #所需要执行的命令
		data=cur.fetchall() #获取执行语句的执行结果
		if len(data) != 0:
			for i in data:
				print('student_id:',i[0],'	名字:',i[1],'	class_id:',i[2],'	成绩:',i[3],'	迟到:',i[4],'	违纪:',i[5])
			su=input('确认删除输入y/按任意键放弃删除：')
			if su=='y':
				cur.execute('delete from study where name="%s"'%name1)
				print('删除成功！')
				conn.commit()
				jx=input('输入任意键继续删除/退出删除输入q：')
				if jx == 'q':
					print('退出删除成功！')
					break
				else:
					print('请继续删除!')	
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
def remove_oe():
	while 1:
		try:
			num2=int(input('请输入您删除的student_id：'))
			cur.execute('select * from oe where student_id=%d'%num2) #所需要执行的命令
			data=cur.fetchall() #获取执行语句的执行结果
			if len(data) != 0:
				for i in data:
					print('student_id:',i[0],'	名字:',i[1],'	毕业时间:',i[2],'	就业时间:',i[3],'	就业资薪:',i[4],'	就业公司:',i[5])
				su=input('确认删除输入y/按任意键放弃删除：')
				if su=='y':
					cur.execute('delete from oe where student_id=%d'%num2)
					print('删除成功！')
					conn.commit()
					jx=input('输入任意键继续删除/退出删除输入q：')
					if jx == 'q':
						print('退出删除成功！')
						break
					else:
						print('请继续删除!')	
				else:
					print('放弃本次删除!')
					break
			else:
				print('student_id不存在！')
				jx=input('输入任意键继续删除/退出删除输入q：')
				if jx == 'q':
					print('退出删除成功！')
					break
				else:
					print('请继续删除!')
		except ValueError as e:
			print('输入有误，请重新输入！')
def remove_oe_name():
	while 1:
		name1=input('请输入您删除的名字：')
		cur.execute('select * from oe where name="%s"'%name1) #所需要执行的命令
		data=cur.fetchall() #获取执行语句的执行结果
		if len(data) != 0:
			for i in data:
				print('student_id:',i[0],'	名字:',i[1],'	毕业时间:',i[2],'	就业时间:',i[3],'	就业资薪:',i[4],'	就业公司:',i[5])
			su=input('确认删除输入y/按任意键放弃删除：')
			if su=='y':
				cur.execute('delete from oe where name="%s"'%name1)
				print('删除成功！')
				conn.commit()
				jx=input('输入任意键继续删除/退出删除输入q：')
				if jx == 'q':
					print('退出删除成功！')
					break
				else:
					print('请继续删除!')	
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
def remove_jh():
	while 1:
		try:
			num2=int(input('请输入您删除的student_id：'))
			cur.execute('select * from jh where student_id=%d'%num2) #所需要执行的命令
			data=cur.fetchall() #获取执行语句的执行结果
			if len(data) != 0:
				for i in data:
					print('student_id:',i[0],'	名字:',i[1],'	跳槽后公司:',i[2],'	跳槽后资薪:',i[3],'	跳槽时间:',i[4])
				su=input('确认删除输入y/按任意键放弃删除：')
				if su=='y':
					cur.execute('delete from jh where student_id=%d'%num2)
					print('删除成功！')
					conn.commit()
					jx=input('输入任意键继续删除/退出删除输入q：')
					if jx == 'q':
						print('退出删除成功！')
						break
					else:
						print('请继续删除!')	
				else:
					print('放弃本次删除!')
					break
			else:
				print('student_id不存在！')
				jx=input('输入任意键继续删除/退出删除输入q：')
				if jx == 'q':
					print('退出删除成功！')
					break
				else:
					print('请继续删除!')
		except ValueError as e:
			print('输入有误，请重新输入！')
def remove_jh_name():
	while 1:
		name1=input('请输入您删除的名字：')
		cur.execute('select * from jh where name="%s"'%name1) #所需要执行的命令
		data=cur.fetchall() #获取执行语句的执行结果
		if len(data) != 0:
			for i in data:
				print('student_id:',i[0],'	名字:',i[1],'	跳槽后公司:',i[2],'	跳槽后资薪:',i[3],'	跳槽时间:',i[4])
			su=input('确认删除输入y/按任意键放弃删除：')
			if su=='y':
				cur.execute('delete from jh where name="%s"'%name1)
				print('删除成功！')
				conn.commit()
				jx=input('输入任意键继续删除/退出删除输入q：')
				if jx == 'q':
					print('退出删除成功！')
					break
				else:
					print('请继续删除!')	
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
def remove1():
	while 1:
		print('*'*35)
		print('''
	    选删除表
	输入p，删除person表
	输入c，删除class表
	输入s, 删除study表
	输入o, 删除oe表
	输入j，删除jh表
	输入q, 退出删除
		''')
		print('*'*35)
		shuru=input('请输入您的选择: ')
		if shuru=='p':
			while 1:
				print('*'*35)
				print('''
	    删除方式
	输入i，进行id删除
	输入t，进行tel删除
	输入n, 进行name删除
	输入a，删person全表
	输入q, 退出删除方式
				''')
				print('*'*35)
				ch=input('请输入您的删除方式: ')
				if ch == 'i':
					remove_person_num('student_id')
				elif ch == 't':
					remove_person_num('tel')
				elif ch == 'n':
					remove_person_name()
				elif ch == 'a':
					su=input('确认删除person表全部信输入y/按任意键放弃删除：')
					if su=='y':
						cur.execute('delete from person')
						print('person表全部删除成功！')
						conn.commit()
						jx=input('输入任意键继续删除/退出删除输入q：')
						if jx == 'q':
							print('退出删除成功！')
							break
						else:
							print('请继续删除!')	
					else:
						print('放弃本次删除!')
						break
				elif ch == 'q':
					print('退出选择成功！')
					break
				else:
					print('选择有误，请重新选择！')
		elif shuru=='c':
			while 1:
				print('*'*35)
				print('''
	    删除方式
	输入i，进行id删除
	输入a，删class全表
	输入q, 退出删除方式
				''')
				print('*'*35)
				ch=input('请输入您的删除方式: ')
				if ch == 'i':
					remove_class()
				elif ch == 'a':
					su=input('确认删除class表全部信输入y/按任意键放弃删除：')
					if su=='y':
						cur.execute('delete from class')
						print('class表全部删除成功！')
						conn.commit()
						jx=input('输入任意键继续删除/退出删除输入q：')
						if jx == 'q':
							print('退出删除成功！')
							break
						else:
							print('请继续删除!')	
					else:
						print('放弃本次删除!')
						break
				elif ch == 'q':
					print('退出选择成功！')
					break
				else:
					print('选择有误，请重新选择！')
		elif shuru=='s':
			while 1:
				print('*'*35)
				print('''
	    删除方式
	输入i，进行id删除
	输入n，进行name删除
	输入a，删study全表
	输入q, 退出删除方式
				''')
				print('*'*35)
				ch=input('请输入您的删除方式: ')
				if ch == 'i':
					remove_study()
				elif ch == 'n':
					remove_study_name()
				elif ch == 'a':
					su=input('确认删除class表全部信输入y/按任意键放弃删除：')
					if su=='y':
						cur.execute('delete from study')
						print('study表全部删除成功！')
						conn.commit()
						jx=input('输入任意键继续删除/退出删除输入q：')
						if jx == 'q':
							print('退出删除成功！')
							break
						else:
							print('请继续删除!')	
					else:
						print('放弃本次删除!')
						break
				
				elif ch == 'q':
					print('退出选择成功！')
					break
				else:
					print('选择有误，请重新选择！')
		elif shuru=='o':
			while 1:
				print('*'*35)
				print('''
	    删除方式
	输入i，进行id删除
	输入n，进行name删除
	输入a，删oe全表
	输入q, 退出删除方式
				''')
				print('*'*35)
				ch=input('请输入您的删除方式: ')
				if ch == 'i':
					remove_oe()
				elif ch == 'n':
					remove_oe_name()
				elif ch == 'a':
					su=input('确认删除oe表全部信输入y/按任意键放弃删除：')
					if su=='y':
						cur.execute('delete from oe')
						print('oe表全部删除成功！')
						conn.commit()
						jx=input('输入任意键继续删除/退出删除输入q：')
						if jx == 'q':
							print('退出删除成功！')
							break
						else:
							print('请继续删除!')	
					else:
						print('放弃本次删除!')
						break
				elif ch == 'q':
					print('退出选择成功！')
					break
				else:
					print('选择有误，请重新选择！')
		elif shuru=='j':
			while 1:
				print('*'*35)
				print('''
	    删除方式
	输入i，进行id删除
	输入n，进行name删除
	输入a，删jh全表
	输入q, 退出删除方式
				''')
				print('*'*35)
				ch=input('请输入您的删除方式: ')
				if ch == 'i':
					remove_jh()
				elif ch == 'n':
					remove_jh_name()
				elif ch == 'a':
					su=input('确认删除jh表全部信输入y/按任意键放弃删除：')
					if su=='y':
						cur.execute('delete from jh')
						print('jh表全部删除成功！')
						conn.commit()
						jx=input('输入任意键继续删除/退出删除输入q：')
						if jx == 'q':
							print('退出删除成功！')
							break
						else:
							print('请继续删除!')	
					else:
						print('放弃本次删除!')
						break
				elif ch == 'q':
					print('退出选择成功！')
					break
				else:
					print('选择有误，请重新选择！')
		elif shuru=='q':
			print('退出程序成功！')
			break
		else:
			print('选择有误，请重新选择！')
	cur.close()  #关闭游标
	conn.close() #关闭链接，释放数据库资源
if __name__=='__main__':
	remove1()
==========2remove-mysql-python.py=============================================================================================
  #coding=utf-8
import pymysql
conn=pymysql.connect(host='localhost',user='root',passwd='jiejay',db='project',port=3306,charset='utf8') #设置链接参数
cur=conn.cursor() #获取游标
def remove_id(choice1):
	while True:
		try:
			student_id1=int(input('请输入您删除的student_id：'))
			cur.execute('select * from %s where student_id=%d'%(choice1,student_id1)) #所需要执行的命令
			data=cur.fetchall() #获取执行语句的执行结果
			if len(data) != 0:
				for i in data:
					print(i)
				su=input('确认删除输入y/按任意键放弃删除：')
				if su=='y':
					cur.execute('delete from %s where student_id=%d'%(choice1,student_id1))
					print('删除成功！')
					conn.commit()
					jx=input('输入任意键继续删除/退出删除输入q：')
					if jx == 'q':
						print('退出删除成功！')
						break
					else:
						print('请继续删除!')	
				else:
					print('放弃本次删除!')
					break
			else:
				print('student_id不存在！')
				jx=input('输入任意键继续删除/退出删除输入q：')
				if jx == 'q':
					print('退出删除成功！')
					break
				else:
					print('请继续删除!')
		except ValueError as e:
			print('输入有误，请重新输入！')
def remove_tel(choice1):
	while True:
		try:
			tel1=int(input('请输入您删除的tel：'))
			cur.execute('select * from %s where tel=%d'%(choice1,tel1)) #所需要执行的命令
			data=cur.fetchall() #获取执行语句的执行结果
			if len(data) != 0:
				for i in data:
					print(i)
				su=input('确认删除输入y/按任意键放弃删除：')
				if su=='y':
					cur.execute('delete from %s where tel=%d'%(choice1,tel1))
					print('删除成功！')
					conn.commit()
					jx=input('输入任意键继续删除/退出删除输入q：')
					if jx == 'q':
						print('退出删除成功！')
						break
					else:
						print('请继续删除!')	
				else:
					print('放弃本次删除!')
					break
			else:
				print('tel不存在！')
				jx=input('输入任意键继续删除/退出删除输入q：')
				if jx == 'q':
					print('退出删除成功！')
					break
				else:
					print('请继续删除!')
		except ValueError as e:
			print('输入有误，请重新输入！')
def remove_name(choice1):
	while True:
		name1=input('请输入您删除的名字：')
		cur.execute('select * from %s where name="%s"'%(choice1,name1)) #所需要执行的命令
		data=cur.fetchall() #获取执行语句的执行结果
		if len(data) != 0:
			for i in data:
				print(i)
			su=input('确认删除输入y/按任意键放弃删除：')
			if su=='y':
				cur.execute('delete from %s where name="%s"'%(choice1,name1))
				print('删除成功！')
				conn.commit()
				jx=input('输入任意键继续删除/退出删除输入q：')
				if jx == 'q':
					print('退出删除成功！')
					break
				else:
					print('请继续删除!')	
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

def remove1():
	while True:
		print('*'*35)
		print('''
	    选删除表
	输入p，删除person表
	输入c，删除class表
	输入s, 删除study表
	输入o, 删除oe表
	输入j，删除jh表
	输入q, 退出删除
		''')
		print('*'*35)
		shuru=input('请输入您的选择: ')
		if shuru=='p':
			while True:
				print('*'*35)
				print('''
	    删除方式
	输入i，进行id删除
	输入t，进行tel删除
	输入n, 进行name删除
	输入q, 退出删除方式
				''')
				print('*'*35)
				ch=input('请输入您的删除方式: ')
				if ch == 'i':
					remove_id('person')
				elif ch == 't':
					remove_tel('person')
				elif ch == 'n':
					remove_name('person')
				elif ch == 'q':
					print('退出选择成功！')
					break
				else:
					print('选择有误，请重新选择！')
		elif shuru=='c':
			remove_id('class')
		elif shuru=='s':
			while True:
				print('*'*35)
				print('''
	    删除方式
	输入i，进行id删除
	输入n，进行name删除
	输入q, 退出删除方式
				''')
				print('*'*35)
				ch=input('请输入您的删除方式: ')
				if ch == 'i':
					remove_id('study')
				elif ch == 'n':
					remove_name('study')
				elif ch == 'q':
					print('退出选择成功！')
					break
				else:
					print('选择有误，请重新选择！')
		elif shuru=='o':
			while True:
				print('*'*35)
				print('''
	    删除方式
	输入i，进行id删除
	输入n，进行name删除
	输入q, 退出删除方式
				''')
				print('*'*35)
				ch=input('请输入您的删除方式: ')
				if ch == 'i':
					remove_id('oe')
				elif ch == 'n':
					remove_name('oe')
				elif ch == 'q':
					print('退出选择成功！')
					break
				else:
					print('选择有误，请重新选择！')
		elif shuru=='j':
			while True:
				print('*'*35)
				print('''
	    删除方式
	输入i，进行id删除
	输入n，进行name删除
	输入q, 退出删除方式
				''')
				print('*'*35)
				ch=input('请输入您的删除方式: ')
				if ch == 'i':
					remove_id('jh')
				elif ch == 'n':
					remove_name('jh')
				elif ch == 'q':
					print('退出选择成功！')
					break
				else:
					print('选择有误，请重新选择！')
		elif shuru=='q':
			print('退出程序成功！')
			break
		else:
			print('选择有误，请重新选择！')
	cur.close()  #关闭游标
	conn.close() #关闭链接，释放数据库资源
if __name__=='__main__':
	remove1()
  ============1remove-mysql.py========================================================================================
  #coding=utf-8
import pymysql
conn=pymysql.connect(host='localhost',user='root',passwd='jiejay',db='project',port=3306,charset='utf8') #设置链接参数
cur=conn.cursor() #获取游标
def remove0(choice1):
	while True:
		try:
			student_id1=int(input('请输入您删除的student_id：'))
			cur.execute('select * from %s where student_id=%d'%(choice1,student_id1)) #所需要执行的命令
			data=cur.fetchall() #获取执行语句的执行结果
			if len(data) != 0:
				for i in data:
					print(i)
				su=input('确认删除输入y/按任意键放弃删除：')
				if su=='y':
					cur.execute('delete from %s where student_id=%d'%(choice1,student_id1))
					print('删除成功！')
					conn.commit()
					jx=input('输入任意键继续删除/退出删除输入q：')
					if jx == 'q':
						print('退出删除成功！')
						break
					else:
						print('请继续删除!')	
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
		except ValueError as e:
			print('输入有误，请重新输入！')

def remove1():
	while True:
		print('*'*40)
		print('''
	    删除信息
	输入a，删除person表
	输入b，删除class表
	输入c, 删除study表
	输入d, 删除oe表
	输入e，删除jh表
	输入q, 退出删除
		''')
		print('*'*40)
		shuru=input('请输入您的选择: ')
		if shuru=='a':
			remove0('person')
		elif shuru=='b':
			remove0('class')
		elif shuru=='c':
			remove0('study')
		elif shuru=='d':
			remove0('oe')
		elif shuru=='e':
			remove0('jh')
		elif shuru=='q':
			print('退出程序成功！')
			break
		else:
			print('选择有误，请重新选择！')
	cur.close()  #关闭游标
	conn.close() #关闭链接，释放数据库资源
if __name__=='__main__':
	remove1()
