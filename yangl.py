def Sch():
    import pymysql
    conn=pymysql.connect(host='localhost',user='root',passwd='jiejay',db='project',port=3306,charset='utf8')
    cur=conn.cursor()
    while 1:
    	print('''	
    请输入您想查询信息类别
    
    1:个人信息
    **************
    2:班级信息
    **************
    3:学习情况
    **************
    4:就业情况
    **************
    5:跳槽情况
    **************
    q:退出系统''')
    	choice=input('请输入您想要查询信息的类型:')
    	if choice=='1':
    		while 1:
    	
    			b=input('请选择是否查询全部：yes/no: ')
    			if b=='yes':
    				cur.execute('select * from person')
    				data=cur.fetchall()
    				for i in data:
    					print('ID:',i[0],' 姓名:',i[1],' 性别:',i[2],' 大学:',i[3],' 电话:',i[4],' 班级ID:',i[5])	
    				break
    			elif b=='no':
    	
    				while 1:
    					try:
    						a=int(input('请输入您要查询的学员ID:'))
    						cur.execute('select * from person where student_id=%d'%a)
    						data=cur.fetchall()	
    						if len(data)!=0:
    							for i in data:
    								print(' 姓名:',i[1],' 性别:',i[2],' 大学:',i[3],' 电话:',i[4],' 班级ID:',i[5])
    						else:
    							print('该ID不存在')
    					
    					except ValueError as e:
    						print('输入类型错误')
    					b=input('是否继续执行该模块:(yes继续，no退出:)')
    					if b=='yes':
    						print('--------------继续执行--------------')
    					elif b=='no':
    						print('退出成功!')
    						break
    					else:
    						print('无法识别，默认退出!')
    						break
    				break
    			else:
    				print('无法识别，默认退出!')
    				break
    
    	elif choice=='2':
    		while 1:
    			c=input('请选择是否查询全部：yes/no: ')
    			if c=='yes':
    				cur.execute('select * from class')
    				d=cur.fetchall()
    				for i in d:
    					print('ID:',i[0],'班级ID:',i[1],'班级名字:',i[2],'教室名称:',i[3],'课程类型:',i[4])
    				break
    			elif c=='no':
    				while 1:
    					try:
    						a=int(input('请输入您要查询的学员ID:'))
    						cur.execute('select * from class where student_id=%d'%a)
    						data=cur.fetchall()
    						if len(data)!=0:
    							for d in data:
    								print('班级ID:',d[1],'班级名字:',d[2],'教室名称:',d[3],'课程类型:',d[4])
    						else:
    							 print('该ID不存在')
    					except ValueError as e:
    							print('输入类型错误')
    					b=input('是否继续执行该模块:(yes继续，no退出,): ')
    					if b=='yes':
    						print('--------------继续执行--------------')
    					elif b=='no':
    						print('退出成功!')
    						break
    					
    					else:
    						print('无法识别，默认退出!')
    						break
    				break
    			else:
                                    print('无法识别，默认退出!')
                                    break
    	elif choice=='3':
    		while 1:
    			b=input('请选择是否查询全部：yes/no: ')
    			if b=='yes':
    				cur.execute('select * from study')
    				data=cur.fetchall()
    				for f in data:
    					print('ID:',f[0],'学生名字:',f[1],'班级ID:',f[2],'考试成绩:',f[3],'迟到次数:',f[4],'违纪次数:',f[5])	
    				break
    			if b=='no':
    				while 1:
    					try:
    						a=int(input('请输入您要查询的学员ID:'))
    						cur.execute('select * from study where student_id=%d'%a)
    						e=cur.fetchall()
    						if len(e)!=0:
    							for f in e:
    								print('学生名字:',f[1],'班级ID:',f[2],'考试成绩:',f[3],'迟到次数:',f[4],'违纪次数:',f[5])		
    						else:
    							print('该ID不存在')
    					except ValueError as e:
    						 print('输入类型错误')
    					b=input('是否继续执行该模块:(yes继续，no退出): ')
    					if b=='yes':
    						print('继续执行')
    					elif b=='no':
    						print('退出成功')
    						break
    					else:
    						print('无法识别，默认退出!')
    						break	
    				break
    			else:
    				print('无法识别，默认退出')
    				break
    	elif choice=='4':
    		while 1:
    			b=input('请选择是否查询全部(yes/no): ')
    			if b == 'yes':
    				cur.execute('select * from oe')
    				data=cur.fetchall()
    				for h in data:
    					print('ID:',h[0],'学生名字:',h[1],'毕业时间:',h[2],'就业时间:',h[3],'就业薪资：',h[4],'就业公司：',    h[5])
    				break
    			elif b== 'no':
    				while 1:
    					try:
    						a=int(input('请输入您要查询的学员ID:'))
    						cur.execute('select * from oe where student_id=%d'%a)
    						g=cur.fetchall()
    						if len(g)!=0:
    							for h in g:
    								print('学生名字:',h[1],'毕业时间:',h[2],'就业时间:',h[3],'就业薪资：',h[4],'就业公司：',h[5])
    						else:
    							print('该ID不存在')
    					except ValueError as e:
    						print('输入类型错误')
    					b=input('是否继续执行该模块:(yes继续，no退出): ')
    					if b=='yes':
    						print('继续执行')
    					elif b=='no':
    						print('退出成功')
    						break
    					else:
    						print('无法识别，默认退出!')
    						break
    				break
    	
    			else:
    				print('无法识别，默认退出')
    				break
    	elif choice=='5':
    		while 1:
    			b=input('请选择是否查询全部(yes/no): ')
    			if b == 'yes':
    				cur.execute('select * from oe')
    				data=cur.fetchall()
    				for i in data:
    					print('ID:',i[0],'姓名:',i[1],'跳槽后公司:',i[2],'跳槽后工资:',i[3],'跳槽时间:',i[4])
    				break
    			elif b== 'no':
    				while 1:
    					try:
    						a=int(input('请输入您要查询的学员ID:'))
    						cur.execute('select * from jh where student_id=%d'%a)
    						data=cur.fetchall()
    						if len(data)!=0:
    							for i in data:
    								print('姓名:',i[1],'跳槽后公司:',i[2],'跳槽后工资:',i[3],'跳槽时间:',i[4])
    							
    						else:
    							print('该ID不存在')
    					except ValueError as e:
    						print('输入类型错误')
    					b=input('是否继续执行该模块:(yes继续，no退出): ')
    					if b=='yes':
    						print('继续执行')
    					elif b=='no':
    						print('退出成功')
    						break
    					else:
    						print('无法识别，默认退出!')
    						break
    				break
    			else:
    				print('无法识别，默认退出')
    				break
    	elif choice=='q':
    		print('退出成功')
    		break
    	else:
    		print('无此选项')
    		continue
    cur.close()
    conn.close()   
