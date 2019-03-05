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
