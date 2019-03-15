def Modify():   
    import pymysql
    while 1:
    	print('''
    按1，修改person表中的数据
    按2，修改class 表中的数据
    按3，修改study 表中的数据
    按4，修改  oe  表中的数据
    按5，修改  jh  表中的数据
    按q，退出程序
    ''')
    	xuanzhe=input('请选择一个表进行修改:')
    	if xuanzhe=='1':
    		while 1:
    			conn=pymysql.connect(host='localhost',user='root',passwd='jiejay',db='project',port=3306,charset='utf8')
    			cur=conn.cursor()
    			print('''
    按1，通过学员id进行修改
    按2，通过学员名字进行修改
    按3，通过电话修改
    按q，退出程序
    			''')
    			xuan=input('请输入您的选择:')
    			if xuan=='1':
    				while 1:
    					try:
    						id1=int(input('请输入您要修改的学员id:'))
    						cur.execute('select * from person where student_id=%d'%id1)
    						data=cur.fetchall()
    						if len(data)!=0: 
    							for i in data:
    								print('您要修改的原数据为:')
    								print('学员名字:',i[1],'性别:',i[2],'大学:',i[3],'电话:',i[4])
    							print('''
    	按a，修改名字
    	按b，修改性别
    	按c，修改大学
    	按d，修改电话
    	按e，修改全部
    	按q，退出程序
    							''')
    							xuan1=input('请再次输入您的选择:')
    							if xuan1=='a':
    								name1=input('修改后的名字:')	
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update person set name="%s" where student_id=%d'%(name1,id1))
    									cur.execute('update study set name="%s" where student_id=%d'%(name1,id1))
    									cur.execute('update oe set name="%s" where student_id=%d'%(name1,id1))
    									cur.execute('update jh set name="%s" where student_id=%d'%(name1,id1))
    									conn.commit()
    									cur.execute('select * from person where student_id=%d'%id1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'性别:',i[2],'大学:',i[3],'电话:',i[4])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入id进行修改')
    									print('-------------------------------------------------------')
    								
    							elif xuan1=='b':
    								sex1=input('修改后的性别:')	
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update person set sex="%s" where student_id=%d'%(sex1,id1))
    									conn.commit()
    									cur.execute('select * from person where student_id=%d'%id1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'性别:',i[2],'大学:',i[3],'电话:',i[4])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入id进行修改')
    									print('-------------------------------------------------------')
    						
    							elif xuan1=='c':
    								college1=input('修改后的大学:')	
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update person set college="%s" where student_id=%d'%(college1,id1))
    									conn.commit()
    									cur.execute('select * from person where student_id=%d'%id1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'性别:',i[2],'大学:',i[3],'电话:',i[4])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误，请重新输入id进行修改')
    									print('-------------------------------------------------------')
    
    							elif xuan1=='d':
    								tel1=int(input('修改后的电话:'))	
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update person set tel="%s" where student_id=%d'%(tel1,id1))
    									conn.commit()
    									cur.execute('select * from person where student_id=%d'%id1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'性别:',i[2],'大学:',i[3],'电话:',i[4])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误，请重新输入id进行修改')
    									print('-------------------------------------------------------')
    							elif xuan1=='e':
    								name1=input('修改后的名字为:')
    								sex1=input('修改后的性别为:')
    								college1=input('修改后的大学为:')
    								tel1=int(input('修改后的电话为:'))
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute("update person set name='%s',sex='%s',college='%s',tel=%d where student_id=%d"%(name1,sex1,college1,tel1,id1))
    									cur.execute('update study set name="%s" where student_id=%d'%(name1,id1))
    									cur.execute('update oe set name="%s" where student_id=%d'%(name1,id1))
    									cur.execute('update jh set name="%s" where student_id=%d'%(name1,id1))
    									conn.commit()
    									cur.execute('select * from person where student_id=%d'%id1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'性别:',i[2],'大学:',i[3],'电话:',i[4])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误，请重新输入id进行修改')
    									print('-------------------------------------------------------')
    							elif xuan1=='q':
    								print('退出成功!')
    								print('----------------------下一次运行-----------------------')
    								break
    							else:
    								print('输入错误，请重新输入id进行修改')
    								print('-------------------------------------------------------')
    						else:
    							jixu=input('学员id不存在,按q退出,其他键继续:')
    							if jixu=='q':
    								print('退出成功!')
    								print('----------------------下一次运行-----------------------')
    								break
    							else:
    								print('请重新输入')
    								print('-----------------------------------------------------')
    					except ValueError as e:
    						print('输入类型错误,请输入数字类型')
    						print('------------------------------------------------------')	
    						
    			elif xuan=='2':
    				while 1:
    					try:
    						name=input('请输入您要修改的学员名字:')
    						cur.execute('select * from person where name="%s"'%name)
    						data=cur.fetchall()
    						if len(data)!=0: 
    							for i in data:
    								print('您要修改的原数据为:')
    								print('学员名字:',i[1],'性别:',i[2],'大学:',i[3],'电话:',i[4])
    							print('''
    	按a，修改名字
    	按b，修改性别
    	按c，修改大学
    	按d，修改电话
    	按e，修改全部
    	按q，退出程序
    							''')
    							xuan1=input('请再次输入您的选择:')
    							if xuan1=='a':
    								name1=input('修改后的名字:')	
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update person set name="%s" where name="%s"'%(name1,name))
    									cur.execute('update study set name="%s" where name="%s"'%(name1,name))
    									cur.execute('update oe set name="%s" where name="%s"'%(name1,name))
    									cur.execute('update jh set name="%s" where name="%s"'%(name1,name))
    									conn.commit()
    									cur.execute('select * from person where name="%s"'%name1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'性别:',i[2],'大学:',i[3],'电话:',i[4])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误，请重新输入学员名字进行修改')
    									print('-------------------------------------------------------')
    								
    							elif xuan1=='b':
    								sex1=input('修改后的性别:')	
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update person set sex="%s" where name="%s"'%(sex1,name))
    									conn.commit()
    									cur.execute('select * from person where name="%s"'%name)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'性别:',i[2],'大学:',i[3],'电话:',i[4])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误，请重新输入学员名字进行修改')
    									print('-------------------------------------------------------')
    						
    							elif xuan1=='c':
    								college1=input('修改后的大学:')	
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update person set college="%s" where name="%s"'%(college1,name))
    									conn.commit()
    									cur.execute('select * from person where name="%s"'%name)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'性别:',i[2],'大学:',i[3],'电话:',i[4])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误，请重新输入学员名字进行修改')
    									print('-------------------------------------------------------')
    
    							elif xuan1=='d':
    								tel1=int(input('修改后的电话:'))	
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update person set tel="%s" where name="%s"'%(tel1,name))
    									conn.commit()
    									cur.execute('select * from person where name="%s"'%name)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'性别:',i[2],'大学:',i[3],'电话:',i[4])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误，请重新输入学员名字进行修改')
    									print('-------------------------------------------------------')
    							elif xuan1=='e':
    								name1=input('修改后的名字为:')
    								sex1=input('修改后的性别为:')
    								college1=input('修改后的大学为:')
    								tel1=int(input('修改后的电话为:'))
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute("update person set name='%s',sex='%s',college='%s',tel=%d where name='%s'"%(name1,sex1,college1,tel1,name))
    									cur.execute('update study set name="%s" where name="%s"'%(name1,name))
    									cur.execute('update oe set name="%s" where name="%s"'%(name1,name))
    									cur.execute('update jh set name="%s" where name="%s"'%(name1,name))
    									conn.commit()
    									cur.execute('select * from person where name="%s"'%name1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'性别:',i[2],'大学:',i[3],'电话:',i[4])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误，请重新输入学员名字进行修改')
    									print('-------------------------------------------------------')
    							elif xuan1=='q':
    								print('退出成功!')
    								print('----------------------下一次运行-----------------------')
    								break
    							else:
    								print('输入错误,请重新输入学员名字进行修改')
    								print('-------------------------------------------------------')
    						else:
    							jixu=input('学员姓名不存在,按q退出,其他键继续:')
    							if jixu=='q':
    								print('退出成功!')
    								print('----------------------下一次运行-----------------------')
    								break
    							else:
    								print('请重新输入')
    								print('-------------------------------------------------------')
    					except ValueError as e:
    						print('输入类型错误,请输入数字类型')
    						print('------------------------------------------------------')	
    			elif xuan=='3':
    				while 1:
    					try:
    						tel=int(input('请输入您要修改的电话:'))
    						cur.execute('select * from person where tel=%d'%tel)
    						data=cur.fetchall()
    						if len(data)!=0: 
    							for i in data:
    								print('您要修改的原数据为:')
    								print('学员名字:',i[1],'性别:',i[2],'大学:',i[3],'电话:',i[4])
    							print('''
    	按a，修改名字
    	按b，修改性别
    	按c，修改大学
    	按d，修改电话
    	按e，修改全部
    	按q，退出程序
    							''')
    							xuan1=input('请再次输入您的选择:')
    							if xuan1=='a':
    								name1=input('修改后的名字:')	
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('select * from person where tel=%d'%tel)
    									data=cur.fetchall()
    									for i in data:
    										cur.execute('update study set name="%s" where student_id=%d'%(name1,i[0]))
    										cur.execute('update oe set name="%s" where student_id=%d'%(name1,i[0]))
    										cur.execute('update jh set name="%s" where student_id=%d'%(name1,i[0]))
    									cur.execute('update person set name="%s" where tel=%d'%(name1,tel))
    									conn.commit()
    									cur.execute('select * from person where tel=%d'%tel)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'性别:',i[2],'大学:',i[3],'电话:',i[4])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误，请重新输入学员电话进行修改')
    									print('-------------------------------------------------------')
    								
    							elif xuan1=='b':
    								sex1=input('修改后的性别:')	
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update person set sex="%s" where tel=%d'%(sex1,tel))
    									conn.commit()
    									cur.execute('select * from person where tel=%d'%tel)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'性别:',i[2],'大学:',i[3],'电话:',i[4])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误，请重新输入学员电话进行修改')
    									print('-------------------------------------------------------')
    							elif xuan1=='c':
    								college1=input('修改后的大学:')	
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update person set college="%s" where tel=%d'%(college1,tel))
    									conn.commit()
    									cur.execute('select * from person where tel=%d'%tel)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'性别:',i[2],'大学:',i[3],'电话:',i[4])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误，请重新输入学员电话进行修改')
    									print('-------------------------------------------------------')
    
    							elif xuan1=='d':
    								tel1=int(input('修改后的电话:'))	
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update person set tel=%d where tel=%d'%(tel1,tel))
    									conn.commit()
    									cur.execute('select * from person where tel=%d'%tel1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'性别:',i[2],'大学:',i[3],'电话:',i[4])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误，请重新输入学员电话进行修改')
    									print('-------------------------------------------------------')
    							elif xuan1=='e':
    								name1=input('修改后的名字为:')
    								sex1=input('修改后的性别为:')
    								college1=input('修改后的大学为:')
    								tel1=int(input('修改后的电话为:'))
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute("update person set name='%s',sex='%s',college='%s',tel=%d where tel=%d"%(name1,sex1,college1,tel1,tel))
    									cur.execute('select * from person where tel=%d'%tel)
    									data=cur.fetchall()
    									for i in data:
    										cur.execute('update study set name="%s" where student_id=%d'%(name1,i[0]))
    										cur.execute('update oe set name="%s" where student_id=%d'%(name1,i[0]))
    										cur.execute('update jh set name="%s" where student_id=%d'%(name1,i[0]))
    									conn.commit()
    									cur.execute('select * from person where tel=%d'%tel1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'性别:',i[2],'大学:',i[3],'电话:',i[4])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误，请重新输入学员电话进行修改')
    									print('-------------------------------------------------------')
    							elif xuan1=='q':
    								print('退出成功!')
    								print('----------------------下一次运行-----------------------')
    								break
    							else:
    								print('输入错误,请重新输入学员名字进行修改')
    								print('-------------------------------------------------------')
    						else:
    							jixu=input('学员电话不存在,按q退出,其他键继续:')
    							if jixu=='q':
    								print('退出成功!')
    								print('----------------------下一次运行-----------------------')
    								break
    							else:
    								print('请重新输入')
    								print('-------------------------------------------------------')
    					except ValueError as e:
    						print('输入类型错误,请输入数字类型')
    						print('-------------------------------------------------------')
    			elif xuan=='q':
    				print('退出成功!')
    				print('----------------------返回选表界面-----------------------')	
    				break
    			else:
    				print('输入错误，请重新输入')
    				print('----------------------下一次运行-----------------------')	
    	elif xuanzhe=='2':
    		while 1:
    			conn=pymysql.connect(host='localhost',user='root',passwd='test',db='project',port=3306,charset='utf8')
    			cur=conn.cursor()
    			print('''
    按1，通过学员id进行修改
    按q，退出程序
    			''')
    			xuan=input('请输入您的选择:')
    			if xuan=='1':
    				while 1:
    					try:
    						id1=int(input('请输入您要修改的学员id:'))
    						cur.execute('select * from class where student_id=%d'%id1)
    						data=cur.fetchall()
    						if len(data)!=0: 
    							for i in data:
    								print('您要修改的原数据为:')
    								print('班级名字:',i[2],'教室名称:',i[3],'课程类型:',i[4])
    							print('''
    	按a，修改班级名字
    	按b，修改教室名称
    	按c，修改课程类型
    	按d，修改全部
    	按q，退出程序
    							''')
    							xuan1=input('请再次输入您的选择:')
    							if xuan1=='a':
    								name1=input('修改后的班级名字:')
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update class set class_name="%s" where student_id=%d'%(name1,id1))
    									conn.commit()
    									cur.execute('select * from class where student_id=%d'%id1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('班级名字:',i[2],'教室名称:',i[3],'课程类型:',i[4])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入id进行修改')
    									print('-------------------------------------------------------')
    						
    							elif xuan1=='b':
    								room=input('修改后的教室名称:')
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update class set classroom="%s" where student_id=%d'%(room,id1))
    									conn.commit()
    									cur.execute('select * from class where student_id=%d'%id1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('班级名字:',i[2],'教室名称:',i[3],'课程类型:',i[4])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入id进行修改')
    									print('-------------------------------------------------------')
    						
    							elif xuan1=='c':
    								cour=input('修改后的课程类型:')
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update class set coursetype="%s" where student_id=%d'%(cour,id1))
    									conn.commit()
    									cur.execute('select * from class where student_id=%d'%id1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('班级名字:',i[2],'教室名称:',i[3],'课程类型:',i[4])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入id进行修改')
    									print('-------------------------------------------------------')
    							elif xuan1=='d':
    								name1=input('修改后的班级名字:')
    								room=input('修改后的教室名称:')
    								cour=input('修改后的课程类型:')
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update class set class_name="%s",classroom="%s",coursetype="%s" where student_id=%d'%(name1,room,cour,id1))
    									conn.commit()
    									cur.execute('select * from class where student_id=%d'%id1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('班级名字:',i[2],'教室名称:',i[3],'课程类型:',i[4])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入id进行修改')
    									print('-------------------------------------------------------')
    							elif xuan1=='q':
    								print('退出成功!')
    								print('----------------------下一次运行-----------------------')
    								break
    							else:
    								print('输入错误,请重新输入学员id进行修改')
    								print('-------------------------------------------------------')
    						else:
    							jixu=input('学员id不存在,按q退出,其他键继续:')
    							if jixu=='q':
    								print('退出成功!')
    								print('----------------------下一次运行-----------------------')
    								break
    							else:
    								print('请重新输入')
    								print('-----------------------------------------------------')
    					except ValueError as e:
    						print('输入类型错误,请输入数字类型')
    						print('------------------------------------------------------')	
    			elif xuan=='q':
    				print('退出成功!')
    				print('----------------------返回选表界面-----------------------')
    				break
    			else:
    				print('输入错误，请重新输入')
    				print('----------------------下一次运行-----------------------')
    	elif xuanzhe=='3':
    		while 1:
    			conn=pymysql.connect(host='localhost',user='root',passwd='test',db='project',port=3306,charset='utf8')
    			cur=conn.cursor()
    			print('''
    按1，通过学员id进行修改
    按2，通过学员名字进行修改
    按q，退出程序
    			''')
    			xuan=input('请输入您的选择:')
    			if xuan=='1':
    				while 1:
    					try:
    						id1=int(input('请输入您要修改的学员id:'))
    						cur.execute('select * from study where student_id=%d'%id1)
    						data=cur.fetchall()
    						if len(data)!=0:
    							for i in data:
    								print('您要修改的原数据为:')
    								print('学员名字:',i[1],'考试成绩:',i[3],'迟到次数:',i[4],'违纪次数:',i[5])
    							print('''
    	按a，修改学员名字
    	按b，修改考试成绩
    	按c，修改迟到次数
    	按d，修改违纪次数
    	按e，修改全部
    	按q，退出程序
    							''')
    							xuan1=input('请再次输入您的选择:')
    							if xuan1=='a':
    								name1=input('修改后的学员名字:')
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update study set name="%s" where student_id=%d'%(name1,id1))
    									cur.execute('update person set name="%s" where student_id=%d'%(name1,id1))
    									cur.execute('update oe set name="%s" where student_id=%d'%(name1,id1))
    									cur.execute('update jh set name="%s" where student_id=%d'%(name1,id1))
    									conn.commit()
    									cur.execute('select * from study where student_id=%d'%id1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'考试成绩:',i[3],'迟到次数:',i[4],'违纪次数:',i[5])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入id进行修改')
    									print('-------------------------------------------------------')
    							elif xuan1=='b':
    								grade=int(input('修改后的考试成绩:'))
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update study set grade=%d where student_id=%d'%(grade,id1))
    									conn.commit()
    									cur.execute('select * from study where student_id=%d'%id1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'考试成绩:',i[3],'迟到次数:',i[4],'违纪次数:',i[5])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入id进行修改')
    									print('-------------------------------------------------------')
    							elif xuan1=='c':
    								late=int(input('修改后的迟到次数:'))
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update study set late=%d where student_id=%d'%(late,id1))
    									conn.commit()
    									cur.execute('select * from study where student_id=%d'%id1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'考试成绩:',i[3],'迟到次数:',i[4],'违纪次数:',i[5])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入id进行修改')
    									print('-------------------------------------------------------')
    							
    							elif xuan1=='d':
    								vod=int(input('修改后的违纪次数:'))
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update study set vod=%d where student_id=%d'%(vod,id1))
    									conn.commit()
    									cur.execute('select * from study where student_id=%d'%id1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'考试成绩:',i[3],'迟到次数:',i[4],'违纪次数:',i[5])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入id进行修改')
    									print('-------------------------------------------------------')
    
    							elif xuan1=='e':
    								name1=input('修改后的学员名字:')
    								grade=int(input('修改后的考试成绩:'))
    								late=int(input('修改后的迟到次数:'))
    								vod=int(input('修改后的违纪次数:'))
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute("update study set name='%s',grade=%d,late=%d,vod=%d where student_id=%d"%(name1,grade,late,vod,id1))
    									cur.execute('update person set name="%s" where student_id=%d'%(name1,id1))
    									cur.execute('update oe set name="%s" where student_id=%d'%(name1,id1))
    									cur.execute('update jh set name="%s" where student_id=%d'%(name1,id1))
    						
    									conn.commit()
    									cur.execute('select * from study where student_id=%d'%id1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'考试成绩:',i[3],'迟到次数:',i[4],'违纪次数:',i[5])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入id进行修改')
    									print('-------------------------------------------------------')
    							elif xuan1=='q':
    								print('退出成功!')
    								print('----------------------下一次运行-----------------------')
    								break
    							else:
    								print('输入错误，请重新输入id进行修改')
    								print('-------------------------------------------------------')
    						else:
    							jixu=input('学员id不存在,按q退出,其他键继续:')
    							if jixu=='q':
    								print('退出成功!')
    								print('----------------------下一次运行-----------------------')
    								break
    							else:
    								print('请重新输入')
    								print('-----------------------------------------------------')
    					except ValueError as e:
    						print('输入类型错误,请输入数字类型')
    						print('------------------------------------------------------')	
    			elif xuan=='2':
    				while 1:
    					try:
    						name=input('请输入您要修改的学员名字:')
    						cur.execute('select * from study where name="%s"'%name)
    						data=cur.fetchall()
    						if len(data)!=0:
    							for i in data:
    								print('您要修改的原数据为:')
    								print('学员名字:',i[1],'考试成绩:',i[3],'迟到次数:',i[4],'违纪次数:',i[5])
    							print('''
    	按a，修改学员名字
    	按b，修改考试成绩
    	按c，修改迟到次数
    	按d，修改违纪次数
    	按e，修改全部
    	按q，退出程序
    							''')
    							xuan1=input('请再次输入您的选择:')
    							if xuan1=='a':
    								name1=input('修改后的学员名字:')
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update study set name="%s" where name="%s"'%(name1,name))
    									cur.execute('update person set name="%s" where name="%s"'%(name1,name))
    									cur.execute('update oe set name="%s" where name="%s"'%(name1,name))
    									cur.execute('update jh set name="%s" where name="%s"'%(name1,name))
    									conn.commit()
    									cur.execute('select * from study where name="%s"'%name1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'考试成绩:',i[3],'迟到次数:',i[4],'违纪次数:',i[5])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入学员名字进行修改')
    									print('-------------------------------------------------------')
    							elif xuan1=='b':
    								grade=int(input('修改后的考试成绩:'))
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update study set grade=%d where name="%s"'%(grade,name))
    									conn.commit()
    									cur.execute('select * from study where name="%s"'%name)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'考试成绩:',i[3],'迟到次数:',i[4],'违纪次数:',i[5])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入学员名字进行修改')
    									print('-------------------------------------------------------')
    							elif xuan1=='c':
    								late=int(input('修改后的迟到次数:'))
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update study set late=%d where name="%s"'%(late,name))
    									conn.commit()
    									cur.execute('select * from study where name="%s"'%name)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'考试成绩:',i[3],'迟到次数:',i[4],'违纪次数:',i[5])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入学员名字进行修改')
    									print('-------------------------------------------------------')
    							
    							elif xuan1=='d':
    								vod=int(input('修改后的违纪次数:'))
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update study set vod=%d where name="%s"'%(vod,name))
    									conn.commit()
    									cur.execute('select * from study where name="%s"'%name)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'考试成绩:',i[3],'迟到次数:',i[4],'违纪次数:',i[5])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入学员名字进行修改')
    									print('-------------------------------------------------------')
    
    							elif xuan1=='e':
    								name1=input('修改后的学员名字:')
    								grade=int(input('修改后的考试成绩:'))
    								late=int(input('修改后的迟到次数:'))
    								vod=int(input('修改后的违纪次数:'))
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute("update study set name='%s',grade=%d,late=%d,vod=%d where name='%s'"%(name1,grade,late,vod,name))
    									cur.execute('update person set name="%s" where name="%s"'%(name1,name))
    									cur.execute('update oe set name="%s" where name="%s"'%(name1,name))
    									cur.execute('update jh set name="%s" where name="%s"'%(name1,name))
    						
    									conn.commit()
    									cur.execute('select * from study where name="%s"'%name1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'考试成绩:',i[3],'迟到次数:',i[4],'违纪次数:',i[5])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入学员名字进行修改')
    									print('-------------------------------------------------------')
    							elif xuan1=='q':
    								print('退出成功!')
    								print('----------------------下一次运行-----------------------')
    								break
    							else:
    								print('输入错误，请重新输入学员名字进行修改')
    								print('-------------------------------------------------------')
    						else:
    							jixu=input('学员名字不存在,按q退出,其他键继续:')
    							if jixu=='q':
    								print('退出成功!')
    								print('----------------------下一次运行-----------------------')
    								break
    							else:
    								print('请重新输入')
    					except ValueError as e:
    						print('输入类型错误,请输入数字类型')
    						print('------------------------------------------------------')	
    			elif xuan=='q':
    				print('退出成功!')
    				print('----------------------返回选表界面-----------------------')	
    				break
    			else:
    				print('输入错误，请重新输入')
    				print('----------------------下一次运行-----------------------')
    	elif xuanzhe=='4':
    		while 1:
    			conn=pymysql.connect(host='localhost',user='root',passwd='test',db='project',port=3306,charset='utf8')
    			cur=conn.cursor()
    			print('''
    按1，通过学员id进行修改
    按2，通过学员名字进行修改
    按q，退出程序
    			''')
    			xuan=input('请输入您的选择:')
    			if xuan=='1':
    				while 1:
    					try:
    						id1=int(input('请输入您要修改的学员id:'))
    						cur.execute('select * from oe where student_id=%d'%id1)
    						data=cur.fetchall()
    						if len(data)!=0:
    							for i in data:
    								print('您要修改的原数据为:')
    								print('学员名字:',i[1],'毕业时间:',i[2],'就业时间:',i[3],'就业薪资:',i[4],'就业公司:',i[5])
    							print('''
    	按a，修改学员名字
    	按b，修改毕业时间
    	按c，修改就业时间
    	按d，修改就业薪资
    	按e，修改就业公司
    	按f，修改全部数据
    	按q，退出程序
    								''')
    							xuan1=input('请再次输入您的选择:')
    							if xuan1=='a':
    								name1=input('修改后的学员名字:')
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update study set name="%s" where student_id=%d'%(name1,id1))
    									cur.execute('update person set name="%s" where student_id=%d'%(name1,id1))
    									cur.execute('update oe set name="%s" where student_id=%d'%(name1,id1))
    									cur.execute('update jh set name="%s" where student_id=%d'%(name1,id1))
    									conn.commit()
    									cur.execute('select * from oe where student_id=%d'%id1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'毕业时间:',i[2],'就业时间:',i[3],'就业薪资:',i[4],'就业公司:',i[5])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入id进行修改')
    									print('-------------------------------------------------------')
    							elif xuan1=='b':
    								import datetime
    								print('修改后的毕业时间')
    								year=int(input('请输入年:'))
    								month=int(input('请输入月:'))
    								day=int(input('请输入日:'))
    								aa=datetime.date(year,month,day)
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update oe set gr_time="%s" where student_id=%d'%(aa,id1))
    									conn.commit()
    									cur.execute('select * from oe where student_id=%d'%id1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'毕业时间:',i[2],'就业时间:',i[3],'就业薪资:',i[4],'就业公司:',i[5])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入id进行修改')
    									print('-------------------------------------------------------')
    							elif xuan1=='c':
    								import datetime
    								print('修改后的就业时间')
    								year=int(input('请输入年:'))
    								month=int(input('请输入月:'))
    								day=int(input('请输入日:'))
    								aa=datetime.date(year,month,day)
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update oe set occ_time="%s" where student_id=%d'%(aa,id1))
    									conn.commit()
    									cur.execute('select * from oe where student_id=%d'%id1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'毕业时间:',i[2],'就业时间:',i[3],'就业薪资:',i[4],'就业公司:',i[5])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入id进行修改')
    									print('-------------------------------------------------------')
    							
    							elif xuan1=='d':
    								salary=int(input('修改后的就业薪资:'))
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update oe set salary=%d where student_id=%d'%(salary,id1))
    									conn.commit()
    									cur.execute('select * from oe where student_id=%d'%id1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'毕业时间:',i[2],'就业时间:',i[3],'就业薪资:',i[4],'就业公司:',i[5])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入id进行修改')
    									print('-------------------------------------------------------')
    							
    							elif xuan1=='e':
    								company=input('修改后的就业公司:')
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update oe set occ_company="%s" where student_id=%d'%(company,id1))
    									conn.commit()
    									cur.execute('select * from oe where student_id=%d'%id1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'毕业时间:',i[2],'就业时间:',i[3],'就业薪资:',i[4],'就业公司:',i[5])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入id进行修改')
    									print('-------------------------------------------------------')
    							elif xuan1=='f':
    								name1=input('修改后的学员名字:')
    								import datetime
    								print('修改后的毕业时间')
    								year=int(input('请输入年:'))
    								month=int(input('请输入月:'))
    								day=int(input('请输入日:'))
    								aa=datetime.date(year,month,day)
    								print('修改后的就业时间')
    								year1=int(input('请输入年:'))
    								month1=int(input('请输入月:'))
    								day1=int(input('请输入日:'))
    								aa1=datetime.date(year1,month1,day1)
    								salary=int(input('修改后的就业薪资:'))
    								company=input('修改后的就业公司:')
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update oe set name="%s",gr_time="%s",occ_time="%s",salary=%d,occ_company="%s" where student_id=%d'%(name1,aa,aa1,salary,company,id1))
    									cur.execute('update study set name="%s" where student_id=%d'%(name1,id1))
    									cur.execute('update person set name="%s" where student_id=%d'%(name1,id1))
    									cur.execute('update jh set name="%s" where student_id=%d'%(name1,id1))
    									conn.commit()
    									cur.execute('select * from oe where student_id=%d'%id1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'毕业时间:',i[2],'就业时间:',i[3],'就业薪资:',i[4],'就业公司:',i[5])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入id进行修改')
    									print('-------------------------------------------------------')
    							elif xuan1=='q':
    								print('退出成功!')
    								print('----------------------下一次运行-----------------------')
    								break
    							else:
    								print('输入错误,请重新输入学员id进行修改')
    								print('-------------------------------------------------------')
    						else:
    							jixu=input('学员id不存在,按q退出,其他键继续:')
    							if jixu=='q':
    								print('退出成功!')
    								print('----------------------下一次运行-----------------------')
    								break
    							else:
    								print('请重新输入')
    								print('-------------------------------------------------------')
    					except ValueError as e:
    						print('输入类型错误,请输入数字类型')
    						print('------------------------------------------------------')	
    			elif xuan=='2':
    				while 1:
    					try:
    						name=input('请输入您要修改的学员名字:')
    						cur.execute('select * from oe where name="%s"'%name)
    						data=cur.fetchall()
    						if len(data)!=0:
    							for i in data:
    								print('您要修改的原数据为:')
    								print('学员名字:',i[1],'毕业时间:',i[2],'就业时间:',i[3],'就业薪资:',i[4],'就业公司:',i[5])
    							print('''
    	按a，修改学员名字
    	按b，修改毕业时间
    	按c，修改就业时间
    	按d，修改就业薪资
    	按e，修改就业公司
    	按f，修改全部数据
    	按q，退出程序
    								''')
    							xuan1=input('请再次输入您的选择:')
    							if xuan1=='a':
    								name1=input('修改后的学员名字:')
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update oe set name="%s" where name="%s"'%(name1,name))
    									cur.execute('update study set name="%s" where name="%s"'%(name1,name))
    									cur.execute('update person set name="%s" where name="%s"'%(name1,name))
    									cur.execute('update jh set name="%s" where name="%s"'%(name1,name))
    									conn.commit()
    									cur.execute('select * from oe where name="%s"'%name1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'毕业时间:',i[2],'就业时间:',i[3],'就业薪资:',i[4],'就业公司:',i[5])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入学员名字进行修改')
    									print('-------------------------------------------------------')
    							elif xuan1=='b':
    								import datetime
    								print('修改后的毕业时间')
    								year=int(input('请输入年:'))
    								month=int(input('请输入月:'))
    								day=int(input('请输入日:'))
    								aa=datetime.date(year,month,day)
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update oe set gr_time="%s" where name="%s"'%(aa,name))
    									conn.commit()
    									cur.execute('select * from oe where name="%s"'%name)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'毕业时间:',i[2],'就业时间:',i[3],'就业薪资:',i[4],'就业公司:',i[5])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入学员名字进行修改')
    									print('-------------------------------------------------------')
    							elif xuan1=='c':
    								import datetime
    								print('修改后的就业时间')
    								year=int(input('请输入年:'))
    								month=int(input('请输入月:'))
    								day=int(input('请输入日:'))
    								aa=datetime.date(year,month,day)
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update oe set occ_time="%s" where name="%s"'%(aa,name))
    									conn.commit()
    									cur.execute('select * from oe where name="%s"'%name)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'毕业时间:',i[2],'就业时间:',i[3],'就业薪资:',i[4],'就业公司:',i[5])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入学员名字进行修改')
    									print('-------------------------------------------------------')
    							
    							elif xuan1=='d':
    								salary=int(input('修改后的就业薪资:'))
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update oe set salary=%d where name="%s"'%(salary,name))
    									conn.commit()
    									cur.execute('select * from oe where name="%s"'%name)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'毕业时间:',i[2],'就业时间:',i[3],'就业薪资:',i[4],'就业公司:',i[5])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入学员名字进行修改')
    									print('-------------------------------------------------------')
    							
    							elif xuan1=='e':
    								company=input('修改后的就业公司:')
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update oe set occ_company="%s" where name="%s"'%(company,name))
    									conn.commit()
    									cur.execute('select * from oe where name="%s"'%name)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'毕业时间:',i[2],'就业时间:',i[3],'就业薪资:',i[4],'就业公司:',i[5])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入id进行修改')
    									print('-------------------------------------------------------')
    							elif xuan1=='f':
    								name1=input('修改后的学员名字:')
    								import datetime
    								print('修改后的毕业时间')
    								year=int(input('请输入年:'))
    								month=int(input('请输入月:'))
    								day=int(input('请输入日:'))
    								aa=datetime.date(year,month,day)
    								print('修改后的就业时间')
    								year1=int(input('请输入年:'))
    								month1=int(input('请输入月:'))
    								day1=int(input('请输入日:'))
    								aa1=datetime.date(year1,month1,day1)
    								salary=int(input('修改后的就业薪资:'))
    								company=input('修改后的就业公司:')
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update oe set name="%s",gr_time="%s",occ_time="%s",salary=%d,occ_company="%s" where name="%s"'%(name1,aa,aa1,salary,company,name1))
    									cur.execute('update study set name="%s" where name="%s"'%(name1,name))
    									cur.execute('update person set name="%s" where name="%s"'%(name1,name))
    									cur.execute('update jh set name="%s" where name="%s"'%(name1,name))
    									conn.commit()
    									cur.execute('select * from oe where name="%s"'%name1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'毕业时间:',i[2],'就业时间:',i[3],'就业薪资:',i[4],'就业公司:',i[5])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入id进行修改')
    									print('-------------------------------------------------------')
    							elif xuan1=='q':
    								print('退出成功!')
    								print('----------------------下一次运行-----------------------')
    								break
    							else:
    								print('输入错误，请重新输入学员名字进行修改')
    								print('-------------------------------------------------------')
    						else:
    							jixu=input('学员名字不存在,按q退出,其他键继续:')
    							if jixu=='q':
    								print('退出成功!')
    								print('----------------------下一次运行-----------------------')
    								break
    							else:
    								print('请重新输入')
    															
    					except ValueError as e:
    						print('输入类型错误,请输入数字类型')
    						print('------------------------------------------------------')	
    			elif xuan=='q':
    				print('退出成功!')
    				print('----------------------返回选表界面-----------------------')	
    				break
    			else:
    				print('输入错误，请重新输入')
    				print('----------------------下一次运行-----------------------')
    	elif xuanzhe=='5':
    		while 1:
    			conn=pymysql.connect(host='localhost',user='root',passwd='test',db='project',port=3306,charset='utf8')
    			cur=conn.cursor()
    			print('''
    按1，通过学员id进行修改
    按2，通过学员名字进行修改
    按q，退出程序
    			''')
    			xuan=input('请输入您的选择:')
    			if xuan=='1':
    				while 1:
    					try:
    						id1=int(input('请输入您要修改的学员id:'))
    						cur.execute('select * from jh where student_id=%d'%id1)
    						data=cur.fetchall()
    						if len(data)!=0:
    							for i in data:
    								print('您要修改的原数据为:')
    								print('学员名字:',i[1],'跳槽后公司:',i[2],'跳槽后工资:',i[3],'跳槽时间:',i[4])
    							print('''
    	按a，修改学员名字
    	按b，修改跳槽后公司
    	按c，修改跳槽后工资
    	按d，修改跳槽时间
    	按f，修改全部数据
    	按q，退出程序
    								''')
    							xuan1=input('请再次输入您的选择:')
    							if xuan1=='a':
    								name1=input('修改后的学员名字:')
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update study set name="%s" where student_id=%d'%(name1,id1))
    									cur.execute('update person set name="%s" where student_id=%d'%(name1,id1))
    									cur.execute('update oe set name="%s" where student_id=%d'%(name1,id1))
    									cur.execute('update jh set name="%s" where student_id=%d'%(name1,id1))
    									conn.commit()
    									cur.execute('select * from jh where student_id=%d'%id1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'跳槽后公司:',i[2],'跳槽后工资:',i[3],'跳槽时间:',i[4])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入id进行修改')
    									print('-------------------------------------------------------')
    							elif xuan1=='b':
    								jh_c=input('修改后的跳槽公司:')
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update jh set jh_company="%s" where student_id=%d'%(jh_c,id1))
    									conn.commit()
    									cur.execute('select * from jh where student_id=%d'%id1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'跳槽后公司:',i[2],'跳槽后工资:',i[3],'跳槽时间:',i[4])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入id进行修改')
    									print('-------------------------------------------------------')
    							elif xuan1=='c':
    								jh_s=int(input('修改后的跳槽工资:'))
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update jh set jh_salary=%d where student_id=%d'%(jh_s,id1))
    									conn.commit()
    									cur.execute('select * from jh where student_id=%d'%id1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'跳槽后公司:',i[2],'跳槽后工资:',i[3],'跳槽时间:',i[4])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入id进行修改')
    									print('-------------------------------------------------------')
    							elif xuan1=='d':
    								import datetime
    								print('修改后的跳槽时间')
    								year=int(input('请输入年:'))
    								month=int(input('请输入月:'))
    								day=int(input('请输入日:'))
    								aa=datetime.date(year,month,day)
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update jh set jh_time="%s" where student_id=%d'%(aa,id1))
    									conn.commit()
    									cur.execute('select * from jh where student_id=%d'%id1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'跳槽后公司:',i[2],'跳槽后工资:',i[3],'跳槽时间:',i[4])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入id进行修改')
    									print('-------------------------------------------------------')
    							elif xuan1=='f':
    								name1=input('修改后的学员名字:')
    								jh_c=input('修改后的跳槽公司:')
    								jh_s=int(input('修改后的跳槽工资:'))
    								import datetime
    								print('修改后的跳槽时间')
    								year=int(input('请输入年:'))
    								month=int(input('请输入月:'))
    								day=int(input('请输入日:'))
    								aa=datetime.date(year,month,day)
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update jh set name="%s",jh_company="%s",jh_salary=%d,jh_time="%s" where student_id=%d'%(name1,jh_c,jh_s,aa,id1))
    									cur.execute('update study set name="%s" where student_id=%d'%(name1,id1))
    									cur.execute('update person set name="%s" where student_id=%d'%(name1,id1))
    									cur.execute('update oe set name="%s" where student_id=%d'%(name1,id1))
    									conn.commit()
    									cur.execute('select * from jh where student_id=%d'%id1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'跳槽后公司:',i[2],'跳槽后工资:',i[3],'跳槽时间:',i[4])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入id进行修改')
    									print('-------------------------------------------------------')
    							elif xuan1=='q':
    								print('退出成功!')
    								print('----------------------下一次运行-----------------------')
    								break
    							else:
    								print('输入错误,请重新输入学员id进行修改')
    								print('-------------------------------------------------------')
    								
    						else:
    							jixu=input('学员id不存在,按q退出,其他键继续:')
    							if jixu=='q':
    								print('退出成功!')
    								print('----------------------下一次运行-----------------------')
    								break
    							else:
    								print('请重新输入')
    					except ValueError as e:
    						print('输入类型错误,请输入数字类型')
    						print('------------------------------------------------------')
    					
    			elif xuan=='2':
    				while 1:
    					try:
    						name=input('请输入您要修改的学员名字:')
    						cur.execute('select * from jh where name="%s"'%name)
    						data=cur.fetchall()
    						if len(data)!=0:
    							for i in data:
    								print('您要修改的原数据为:')
    								print('学员名字:',i[1],'跳槽后公司:',i[2],'跳槽后工资:',i[3],'跳槽时间:',i[4])
    							print('''
    	按a，修改学员名字
    	按b，修改跳槽后公司
    	按c，修改跳槽后工资
    	按d，修改跳槽时间
    	按f，修改全部数据
    	按q，退出程序
    								''')
    							xuan1=input('请再次输入您的选择:')
    							if xuan1=='a':
    								name1=input('修改后的学员名字:')
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update study set name="%s" where name="%s"'%(name1,name))
    									cur.execute('update person set name="%s" where name="%s"'%(name1,name))
    									cur.execute('update oe set name="%s" where name="%s"'%(name1,name))
    									cur.execute('update jh set name="%s" where name="%s"'%(name1,name))
    									conn.commit()
    									cur.execute('select * from jh where name="%s"'%name1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'跳槽后公司:',i[2],'跳槽后工资:',i[3],'跳槽时间:',i[4])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入学员名字进行修改')
    									print('-------------------------------------------------------')
    							elif xuan1=='b':
    								jh_c=input('修改后的跳槽公司:')
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update jh set jh_company="%s" where name="%s"'%(jh_c,name))
    									conn.commit()
    									cur.execute('select * from jh where name="%s"'%name)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'跳槽后公司:',i[2],'跳槽后工资:',i[3],'跳槽时间:',i[4])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入学员名字进行修改')
    									print('-------------------------------------------------------')
    							elif xuan1=='c':
    								jh_s=int(input('修改后的跳槽工资:'))
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update jh set jh_salary="%s" where name="%s"'%(jh_s,name))
    									conn.commit()
    									cur.execute('select * from jh where name="%s"'%name)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'跳槽后公司:',i[2],'跳槽后工资:',i[3],'跳槽时间:',i[4])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入学员名字进行修改')
    									print('-------------------------------------------------------')
    							elif xuan1=='d':
    								import datetime
    								print('修改后的跳槽时间')
    								year=int(input('请输入年:'))
    								month=int(input('请输入月:'))
    								day=int(input('请输入日:'))
    								aa=datetime.date(year,month,day)
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update jh set jh_time="%s" where name="%s"'%(aa,name))
    									conn.commit()
    									cur.execute('select * from jh where name="%s"'%name)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'跳槽后公司:',i[2],'跳槽后工资:',i[3],'跳槽时间:',i[4])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入学员名字进行修改')
    									print('-------------------------------------------------------')
    							elif xuan1=='f':
    								name1=input('修改后的学员名字:')
    								jh_c=input('修改后的跳槽公司:')
    								jh_s=int(input('修改后的跳槽工资:'))
    								import datetime
    								print('修改后的跳槽时间')
    								year=int(input('请输入年:'))
    								month=int(input('请输入月:'))
    								day=int(input('请输入日:'))
    								aa=datetime.date(year,month,day)
    								a=input('确认修改吗(yes确认,no取消,q退出):')
    								if a=='yes':
    									cur.execute('update jh set name="%s",jh_company="%s",jh_salary=%d,jh_time="%s" where name="%s"'%(name1,jh_c,jh_s,aa,name))
    									cur.execute('update study set name="%s" where name="%s"'%(name1,name))
    									cur.execute('update person set name="%s" where name="%s"'%(name1,name))
    									cur.execute('update oe set name="%s" where name="%s"'%(name1,name))
    									conn.commit()
    									cur.execute('select * from jh where name="%s"'%name1)
    									data=cur.fetchall()
    									for i in data:
    										print('修改后的数据为:')
    										print('学员名字:',i[1],'跳槽后公司:',i[2],'跳槽后工资:',i[3],'跳槽时间:',i[4])
    										print('----------------------下一次运行-----------------------')
    									cur.close()
    									conn.close()
    									break
    								elif a=='no':
    									print('-------------------------------------------------------')
    								elif a=='q':
    									print('退出成功!')
    									print('----------------------下一次运行-----------------------')
    									break
    								else:
    									print('输入错误,请重新输入学员名字进行修改')
    									print('-------------------------------------------------------')
    					except ValueError as e:
    						print('输入类型错误,请输入数字类型')
    						print('------------------------------------------------------')
    					
    			elif xuan=='q':
    				print('退出成功!')
    				print('----------------------返回选表界面-----------------------')	
    				break
    			else:
    				print('输入错误，请重新输入')
    				print('----------------------下一次运行-----------------------')
    	elif xuanzhe=='q':
    		print('退出成功!')
    		break
    	else:
    		print('输入错误，请重新输入')
    		print('----------------------下一次运行-----------------------')
