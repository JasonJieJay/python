import Jason
import yangl
import yuhang
import Dragon

def main():
    import pymysql
    conn=pymysql.connect(host='localhost',user='root',passwd='jiejay',db='project',port=3306,charset='utf8') 
    cur=conn.cursor()
    
    while 1:    
        print('''
    
----------------------------------------------------------------------    
    
欢迎使用本系统
      
    按1新增信息
    **************
    按2查询信息
    **************
    按3修改信息
    **************
    按4删除信息
    **************  
 
						按q退出系统
					        **********************
----------------------------------------------------------------------
    ''')
        i=input('在此键入:')
     
        if i=='1':
            yuhang.Add()   
    
        elif i=='2':
            yangl.Sch()
    
        elif i=='3':
            Dragon.Modify()

        elif i=='4':
            Jason.remove0()
 
        elif i=='q':
            print('See you next time~')
            break
        else:
            print('请重新输入')    


main()
