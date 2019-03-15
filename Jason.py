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
def remove_biao():
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
					su=input('确认删除person表全部信息输入y/按任意键放弃删除：')
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
					su=input('确认删除class表全部信息输入y/按任意键放弃删除：')
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
					su=input('确认删除class表全部信息输入y/按任意键放弃删除：')
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
					su=input('确认删除oe表全部信息输入y/按任意键放弃删除：')
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
					su=input('确认删除jh表全部信息输入y/按任意键放弃删除：')
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
def remove_school():
	while 1:
		try:
			num2=int(input('请输入您删除的student_id：'))
			cur.execute('''select * from person p,study s,class c,oe o,jh j 
					where s.student_id=p.student_id  
					and s.student_id=c.student_id
					and s.student_id=o.student_id 
					and s.student_id=j.student_id 
					and s.student_id=%d'''%num2) #所需要执行的命令
			data=cur.fetchall() #获取执行语句的执行结果
			if len(data) != 0:
				for i in data:
					print(
'student_id:',i[0],'      	名字:',i[1],'   	性别:',i[2],'   	大学:',i[3],'   	电话:',i[4],'   		班级:',i[5],'\n'
'class_id:',i[12],'       	成绩:',i[9],'   	迟到:',i[10],'   		违纪:',i[11],'        班级名:',i[13],' 	教室:',i[14],'   	课程:',i[15],'\n'
'毕业时间:',i[19])
				su=input('确认删除输入y/按任意键放弃删除：')
				if su=='y':
					biao=['person','study']
					for b in biao:
						cur.execute('delete from %s where student_id=%d'%(b,num2))
						conn.commit()
					print('删除成功！')
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
	
def remove_work():
	while 1:
		try:
			num2=int(input('请输入您删除的student_id：'))
			cur.execute('''select * from person p,study s,class c,oe o,jh j 
					where s.student_id=p.student_id  
					and s.student_id=c.student_id
					and s.student_id=o.student_id 
					and s.student_id=j.student_id 
					and s.student_id=%d'''%num2) #所需要执行的命令
			data=cur.fetchall() #获取执行语句的执行结果
			if len(data) != 0:
				for i in data:
					print(
'student_id:',i[17],'       		就业时间:',i[20],'	就业资薪:',i[21],'      			就业公司:',i[22],'\n'
'名字:',i[18],'     		跳槽后资薪:',i[26],'     	跳槽时间:',i[27])
				su=input('确认删除输入y/按任意键放弃删除：')
				if su=='y':
					biao=['oe','jh']
					for b in biao:
						cur.execute('delete from %s where student_id=%d'%(b,num2))
						conn.commit()
					print('删除成功！')
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
	

def remove_per_all():
	while 1:
		try:
			num2=int(input('请输入您删除的student_id：'))
			cur.execute('''select * from person p,study s,class c,oe o,jh j 
					where s.student_id=p.student_id 
					and s.student_id=c.student_id 
					and s.student_id=o.student_id 
					and s.student_id=j.student_id 
					and s.student_id=%d'''%num2) #所需要执行的命令
			data=cur.fetchall() #获取执行语句的执行结果
			if len(data) != 0:
				for i in data:
					print(
'student_id:',i[0],'      	名字:',i[1],'   	性别:',i[2],'   	大学:',i[3],'   	电话:',i[4],'   		班级:',i[5],'\n'
'class_id:',i[12],'       	成绩:',i[9],'   	迟到:',i[10],'   		违纪:',i[11],'        班级名:',i[13],' 	教室:',i[14],'   	课程:',i[15],'\n'
'毕业时间:',i[19],'       		就业时间:',i[20],'	就业资薪:',i[21],'      			就业公司:',i[22],'\n'
'跳槽后公司:',i[25],'     		跳槽后资薪:',i[26],'     	跳槽时间:',i[27])
				su=input('确认删除输入y/按任意键放弃删除：')
				if su=='y':
					biao=['person','study','oe','jh']
					for b in biao:
						cur.execute('delete from %s where student_id=%d'%(b,num2))
						conn.commit()
					print('删除成功！')
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


def remove_data():
	while 1:
		print('*'*35)
		print('''
	    选删除资料
	输入s，删school资料
	输入w，删work资料
	输入a，删个人全部资料
	输入q, 退出删除
		''')
		print('*'*35)
		ch=input('请输入您的选择: ')
		if ch == 's':
			remove_school()
		elif ch == 'w':
			remove_work()
		elif ch == 'a':
			remove_per_all()
		elif ch == 'q':
			print('退出选择成功！')
			break
		else:
			print('选择有误，请重新选择！')

def remove0():
	while 1:
		print('*'*35)
		print('''
	    选删除方式
	输入d，按个人资料删除
	输入b，按照表删除
	输入q, 退出程序
		''')
		print('*'*35)
		ch=input('请输入您的选择: ')
		if ch == 'd':
			remove_data()
		elif ch == 'b':
			remove_biao()
		elif ch == 'q':
			print('退出选择成功！')
			break
		else:
			print('选择有误，请重新选择！')

	cur.close()  #关闭游标
	conn.close() #关闭链接，释放数据库资源
if __name__=='__main__':
	remove0()
