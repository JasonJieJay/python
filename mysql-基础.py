student_id 自增长： 添加输入时用0代替
create table person (student_id  int primary key auto_increment,
name varchar(20),
sex  varchar(10),
college varchar(20),
tel  int,
class_id  int) charset=utf8;

去重 distinct
select distinct name,id from user;

select * from test order by 列名 DESC  limit 1;

显示表的最后一行数据
select count(*) from kr;
select * from kr limit (上面打行数减1) , 1;

自连查询
SELECT b.* 
from shopping as a,shopping as b
where a.name='惠惠'
and a.price<b.price 
order by b.id

linux下

一、导出数据库用mysqldump命令（注意mysql的安装路径，即此命令的路径）：
1、导出数据和表结构：
mysqldump -u用户名 -p密码 数据库名 > 数据库名.sql
#/usr/local/mysql/bin/   mysqldump -uroot -p abc > abc.sql
敲回车后会提示输入密码

2、只导出表结构
mysqldump -u用户名 -p密码 -d 数据库名 > 数据库名.sql
#/usr/local/mysql/bin/   mysqldump -uroot -p -d abc > abc.sql

注：/usr/local/mysql/bin/  --->  mysql的data目录


二、导入数据库
1、首先建空数据库
mysql>create database abc;

2、导入数据库
方法一：
（1）选择数据库
mysql>use abc;
（2）设置数据库编码
mysql>set names utf8;
（3）导入数据（注意sql文件的路径）
mysql>source /home/abc/abc.sql;
方法二：
mysql -u用户名 -p密码 数据库名 < 数据库名.sql
#mysql -uabc_f -p abc < abc.sql

1.数据库
存放数据的

2.常见数据库软件
	关系型数据库
		informix
		db2
		oracle
		mysql
		sqlserver
	非关系型数据库
		mongodb
		redis
		cassandra
3.mysql数据库
a.安装mysql的服务端
	sudo apt-get install mysql-server(安装中会提示输入密码)
b.安装mysql的客户端
	sudo apt-get install mysql-client
c.安装相关的库文件
	sudo apt-get install libmysqlclient-dev
d.mysql基础
	1.mysql的主服务(mysqld)
	检查mysqld进程是否正常运行
	ps -ef |grep mysqld
	2.mysql的端口(3306)
	检查mysqld的端口是否正常运行
	netstat -an|grep 3306
	3.mysql的管理员
	root
	4.mysql的登录
	mysql -u root -p
	管理员登录本地数据库
	mysql -h 127.0.0.1 -u root -p
	管理员登录IP为127.0.0.1的数据库(远程)
	5.mysql的概念
	数据库分2部分：数据库软件、数据库数据
	常说的数据库是数据库数据
	数据库数据是由表组成
	表是由数据组成
	6.基础命令
	show databases;
	查看当前有哪些数据库
	select user();
	查看当前登录用户信息
	select database();
	查看当前数据库的名字
	use mysql;
	数据库切换为mysql
	show tables;
	查看但前数据库中有哪些表
	select * from db\G;
查看db表中所有数据

1.表结构的创建
	表：行、列、名字
	a.数据类型
		字符串 char  varchar
		数字   int
		日期   date
	注意：char和varchar区别(char是定长，varchar是变长)
		char(10)  --6 ----char(10)    速度快
		varchar(10) --6 ---varchar(6) 节省空间
	注意：字符串一定要定义最多放置多少字符串
	b.表结构的创建
	语法：create table 表(
			列名  数据类型,
			列名  数据类型,
			...
		);
	例子：创建表韩国(kr),泡菜名字(pname)字符类型，泡菜价格(price)数字类型，出厂日期ddate
	create table kr(
		pname char(10),
		price int,
		ddate date
	);
	补充：创建数据库 create database test;
	补充：查看表结构  desc kr;
	c.约束
	主键：列中的数据不能为空，每个条件只能搜索到1条数据(数据唯一)，每张表中只能有一个主键
	唯一：每个条件只能搜索到1条数据(数据唯一)，表中可以有多个，主要作为主键约束的补充
	非空：列中的数据不能为空
	检查：列中的数据是否满足条件
	外键(参考)：列中的数据依赖于另外一张表中的数据
2.SQL语句
	结构化查询语言
	DDL：数据库定义语言   create alter drop truncate
	DML：数据库操作语言   insert update  delete
	DCL：数据库控制语言   grant revoke
	DQL：数据库查询语言   select
3.数据的新增
	注意：字符、日期类型使用单引号
	      数字类型直接使用
	a.向表中所有列新增数据
	语法：insert into 表 values(值1,值2...);
	注意：数据的顺序和列的顺序必须一致，列的数据类型和值的数据类型必须一致
	例子：向kr表中新增数据，名字chui，价格2500,出厂日期 2018-01-01
	insert into kr values('chui',2500,'2018-01-01');
	b.向表中指定列新增数据
	语法：insert into 表(列1,列2) values(值1,值2);
	例子：向kr表中新增数据，名字hey，价格2900,出厂日期 1986-01-01
	insert into kr(pname,price,ddate) values('hey',2900,'1986-01-01');
	例子：向kr表中新增数据，名字为55k，价格251
	insert into kr(pname,price) values('55k',251);
	c.新增多条数据
	insert into kr(pname,price) values('simida',100),('kouniqiwa',200),('haleshao',300);
4.数据的修改
	注意：字符、日期类型使用单引号
	数字类型直接使用
	语法：update 表 set 列=值 where 条件;
	注意：如果增加where条件，修改的是指定行的的列，如果不加是修改整个列的数据
	例子：修改kr表中名字55k的价格为0
	update kr set price=0 where pname='55k';
	例子：修改kr表中price为1000
	update kr set price=1000;
5.数据的删除
	delete		可以删除指定数据，删除数据可以找回，DML
	truncate	只能删除所有数据，删除数据无法找回，DDL
	delete语法：
	delete from 表 where 条件;
	例子：删除kr表中名字是55k的所有数据
	delete from kr where pname='55k';
	例子：删除kr表中所有数据
	delete from kr ;
	truncate语法：
	truncate table 表;
	例子：删除kr表中所有数据
	truncate table kr;
补充：删除表结构(数据也被删除)
	drop table 表名;
	删除kr表
	drop table kr
补充：
	sakila样例数据库安装
	a.下载
	https://dev.mysql.com/doc/index-other.html
	b.进入到压缩包所在目录
	cd 下载
	c.解压压缩包到当前目录下
	 tar -xzvf sakila-db.tar.gz 
	d.进入到已经解压的目录中(sakila-data.sql所在目录)
	cd sakila-db/
	e.登录mysql数据库
	mysql -u root -p
	f.导入数据库的表结构
	source sakila-schema.sql;
	g.导入数据库的数据库
	source sakila-data.sql;
10.数据的查询
	查询可以查询指定的行，指定的列，指定行的列
	语法：select 列 from 表 [where 条件];
	例子：
	查询city表中所有数据
	select * from city;
	select city_id,city,country_id,last_update from city;
	注意：*代表所有列
	查询city表中城市名称是Weifang的所有信息
	select * from city where city='Weifang';
	查询city表中所有城市的名称
	select city from city;
	查询city表中城市名称为Yingkou的country_id
	select country_id from city where city='Yingkou';
	a.where条件
	a1.比较运算符
		>	大于
		<	小于
		=	等于
		>=	大于等于
		<=	小于等于
		<>	不等于
		!=	不等于
	注意：=>   =< 非正常写法
	例子：查询customer表中customer_id小于100的所有信息
	select * from customer where customer_id<100;
	例子：查询customer表中名字不是Long的所有信息
	select * from customer where first_name<>'LONG';
	a2.关系运算符
		and	同时满足条件
		or	满足一个条件即可
		not	不满足条件
	例子：查询customer表中customer_id范围在100和110之间所有人员的名字
	select first_name from customer where customer_id >=100 and customer_id<=110;
	例子：查询customer表中名字是Mike或者heygor的所有信息
	select * from customer where first_name='Mike' or first_name='heygor';
	a3.区间
	between...and...
	包括两个端点，小在前，大在后
	例子：查询customer表中customer_id范围在100和110之间所有人员的名字
	select first_name from customer where customer_id between 100 and 110;
	a4.模糊查询
	当信息不完整时候，使用模糊查询，通常和字符串类型一起使用
	like
	%	任意个字符
	_	一个字符
	例子：查询customer表中名字以M开头的所有信息
	select * from customer where first_name like 'M%';
	例子：查询customer表中名字以E结尾的所有信息
	select * from customer where first_name like '%E';
	例子：查询customer表中名字是6个字符的所有信息
	select * from customer where first_name like '______';
	a5.空值查询
	空没有任何数据类型，没有任何值
	不能用于比较和运算
	查询时候使用is null或者is not null
	查询kr表中ddate为空的所有信息
	select * from kr where ddate is null;
	查询kr表中ddate不为空的所有信息
	select * from kr where ddate is not null;
	a6.in(在...里面)
	或的关系
	例子：查询customer表中名字是Mike或者heygor的所有信息
	select * from customer where first_name in ('Mike','heygor')

======================================================================
多表查询
当一张表无法满足查询条件是后，使用多张表进行操作
a.迪卡尔积
不做任何关联产生的数据库
表1
1
2

表2
1 a
2 b
3 c

1 1 a
1 2 b
1 3 c
2 1 a
2 2 b
2 3 c
统计city表中所有的数据
select count(*) from city;600
统计country表中所有的数据
select count(*) from country;109
统计迪卡尔积中所有数据
select count(*) from city,country;65400

迪卡尔积会造成数据量成倍增加，无效数据增多，降低系统性能
为了避免此类情况使用内联查询，左联查询，右联查询

内联查询
语法：
select 列 from 表1,表2 where 表1.列=表2.列;
select 列 from 表1 inner join 表2 on 表1.列=表2.列;
例子：查询国家名称为China的城市名称有哪些？
1.分析相关的列
	国家名称
	城市名称

2.分析列相关的表有哪些
	city  city
	country country
3.关联两张表
	select * from city,country
	where city.country_id=country.country_id;
4.过滤
         select city from city,country
         where city.country_id=country.country_id
	 and country='China';

例子：查询城市名称为Shenzhen的国家名称是什么？country_id是什么？
3.关联
	select * from city c,country co
	where c.country_id=co.country_id;
4.过滤
	select co.country,c.country_id  from city c,country co
        where c.country_id=co.country_id
	and c.city='Shenzhen';

子查询
一条SQL语句的执行依赖于另外一条SQL语句的执行结果
查询国家名称为China的城市名称有哪些？
1.分析列
	国家名称
	城市名称
2.分析表
	city
	country
3.关联列
	country_id
4.
	查询国家表中国家名称为China的country_id
	select country_id from country where country='China';
	查询城市表中country_id为上面查询出来结果的城市名称
	select city from city where country_id=(select country_id from country where country='China');
注意：子查询可以用于数据查询、新增、修改、删除方面
例子：查询country表中country_id最大的国家名称
	max()     最大值
      查询出来表中最大contry_id是多少
	select max(country_id) from country;
      查看coutnry_id为上面查询出来结果的国家名称
	select country from country where country_id=( select max(country_id) from country);
注意：查询字句的结果可以有一个也可以有多个
	如果查询出来结果有1个，可以用等于或者in
	如果查询出来结果是多个，用in

	1.用子查询查询国家名称为China的所有D开头的城市名称
		查询country表中满足条件的country_id
		select country_id from country where country='China';
		查询city表中country_id为上面查询出来结果的城市名称
		select city from city where country_id in (select country_id from country where country='China') and city like 'D%';
	2.用子查询查询城市名称为Daxian的所有客户名字
	city
	customer
	a.查询city表中满足条件的city_id
		select city_id from city where city='Daxian';
	b.查询address表中city_id为上面查询出来结果的address_id
		select address_id from address where city_id in (select city_id from city where city='Daxian')
	c.查询customer表中address_id为上面查询出来结果的客户名字
		select first_name from customer where address_id in (select address_id from address where city_id in (select city_id from city where city='Daxian'));
==============================================================
分组查询
按照某种条件进行分类
a.分组函数(聚合函数)
	max()	最大
	min()	最小
	avg()	平均
	sum()	求和
	count() 计数
	注意：分组函数通常和分组一起使用，也可以单独使用。
	例子：查询city表中最大city_id是多少
	select max(city_id) from city;

b.分组查询
	语法：select 列 from  表 
		where 条件
			group by 分组条件
				having 分组后过滤条件;
	分组条件的判断
		每后面跟的就是分组条件
	例子：查询每个国家有多少个城市？要求显示country_id,城市数量
		select country_id,count(city)   from  city group by country_id;

	例子：查询每个国家有多少个城市，要求显示国家名称，城市数量
		select * from country co,city c where co.country_id=c.country_id;
		select co.country,count(c.city)  from country co,city c where co.country_id=c.country_id group by co.country;
c.分组后过滤
	where和having区别
	where 	分组前过滤    后面不能直接跟分组函数
	having	分组后过滤    后面可以直接跟分组函数
	例子：查询城市数量大于50的国家名称
		 select co.country,count(c.city)  from country co,city c where co.country_id=c.country_id group by co.country having count(c.city)>50;
	有group by 才有having，没有group by就没有having
	补充：分组分为单分组和多分组，按照分组条件进行分类
	每个门店，每天营业额
	group by 门店,天

==================================================
mysql的排序和分页
排序
语法：select 列  from  表
	where 条件
		group by 分组条件
			having 分组后过滤条件
				order by 排序条件
顺序(从小到大)
	order by 列;
	order by 列 asc
	例子：查询city表中所有数据，按照country_id从小到大进行排列
	select * from city order by country_id;

逆序(从大到小)
	order by 列 desc;
	查询city表中所有数据，按照city_id从大到小进行排列
	select * from city order by city_id desc;

分页查询(limit)
	例子：查询city表中前8行数据
	select * from city limit 8;
	例子：查询city表中9-19行数据
	select * from city limit 8,11;

课程目标
掌握python和数据库的交互

课程内容
a.mysql基础
b.python和数据库的交互


a.mysql基础
	mysql的管理员：root
	mysql的端口：  3306
	select 列 from 表 where 条件;

b.python和数据的交互
	1.安装pymysql模块
		a.通过pip安装
			sudo pip3 install pymysql
		b.通过压缩包方式安装
			官方网站下载.tar.gz
			解压压缩包
			进入到解压目录执行
			sudo python3 setup.py install
		注意：如果在执行程序时候出现没有setuptools执行下面命令
			sudo apt-get install python3-setuptools
		c.测试
			import pymysql
	2.python操作数据库
	#设置链接参数
	conn=pymysql.connect(host='localhost',user='root',passwd='test',db='test',port=3306,charset='utf8')
	#链接的主机名或者IP   host
	#链接使用的用户名     user
	#链接用户的密码       passwd
	#链接目标数据库       db
	#链接数据库的端口     port
	#链接使用字符集       charset
	#定义一个游标
	cur=conn.cursor()
	#所需要执行的命令
	cur.execute('select * from kr')
	#获取执行语句的执行结果
	data=cur.fetchall()
	for i in data:
        	print(i)
	#关闭游标
	cur.close()
	#关闭链接，释放数据库资源
	conn.close()
	
一、以公司员工薪水为案例进行设计(公司员工薪水管理系统)

题目：

	1、新员工王小明，性别是男，年龄30，岗位是测试部的测试工程师，薪水6000(基本工资2800，奖金3200);
	inser into employ values('YG001','王小明','男',30,'BM002','GW003');
	inser into salary values('XS004','YG001',2800,3200);	

	2、王小明试用期过了，表现非常好，公司决定给他基本工资调薪10%，奖金调15%;
	update salary set basesalary=(select basesalary from salary s,employ e where s.employid=e.employid and ename='王小明' )*1.1;
	update salary set bonussalary=(select bonussalary from salary s,employ e where s.employid=e.employid and ename='王小明' )*1.15;	
	update salary set basesalary=basesalary*1.1,bonussalary=bonussalary*1.15 from salary where employid=(select employid form employ where ename='王小明');

	3、查询测试部门最高薪水，最低薪水，平均薪水，显示最高薪水，最低薪水，平均薪水;
	select d.deptname,max(s.basesalary+s.bonussalary),min(s.basesalary+s.bonussalary),avg(s.basesalary+s.bonussalary) from dept d,employ e,salary s where d.deptid=e.deptid and e.employid=s.employid and d.deptname='测试部门';

	4、查询所有部门的最高薪水，最低水，平均薪水，显示部门，最高薪水，最低薪水，平均薪水,并按部门名升序排序;
	select d.deptname,max(s.basesalary+s.bonussalary),min(s.basesalary+s.bonussalary),avg(s.basesalary+s.bonussalary) from dept d,employ e,salary s where d.deptid=e.deptid and e.employid=s.employid group by e.deptid order by e.deptid;

	5、统计测试部门有多少员工，显示员工数;
	select count(e.employid) from dept d,employ e where e.deptid=d.deptid and d.deptname='测试部门' group by e.deptid;

	6、统计所有部门员工数，并按部门进行升序排序，显示部门，员工数;
	select d.deptname,count(e.employid) from dept d,dmploy e where e.deptid=d.deptid group by d.deptid order by e.deptid;

	7、查询所有姓王的所有员工信息;
	select * from dept d,station s,employ e,salsry sa where d.deptid=e.deptid and s.stationid=e.stadtionid and e.employid=sa.employid and e.ename like '王%';

	8、按部门，性别统计平均薪水;
	select d.deptname,e.sex,avg(s.basesalary+s.bonussalary) from dept d,employ e,salary s where d.deptid=e.deptid and e.employid=s.employid group by d.deptid,e.sex;

	9、查询30到40岁 平均薪水;
	select avg(s.basesalary+s.bonussalary) from employ e,salary s where e.employid=s.employid  and e.age between 30 and 40;

	10、查询测试部薪水最高的员工，显示员工姓名；
	select e.ename from dept d,employ e,salary s where d.deptid=e.deptid and e.employid=s.employid group by d.deptid having max(s.basesalary+s.bonussalary);

	11、删除王小明的所有信息
	delete from salary where employid in (select employid from employ where ename='王小明');
	delete from employ where ename='王小明';
	delete from employ e,salary s where e.employid=s.employid and ename='王小明';


二、以个人简历为案例进行设计(个人简历管理系统)

题目：

	1、新增王小明个人信息,性别男，年龄30，工作经历在泽林当测试讲师，薪水为6000;
	

	2、由于录入人员错误，王小明在泽林公司的薪水录入错误，调整为薪水是7000;


	3、查询工作经历所在泽林公司的最高薪水，最低薪水，平均薪水，显示：最高薪水，最低薪水，平均薪水;


	4、查询所有岗位的最高薪水，最低薪水，平均薪水，显示：岗位,最高薪水，最低薪水，平均薪水并按岗位进行升序排序;


	5、查询所有工作单位的最高薪水，最低薪水，平均薪水，显示：工作单位,最高薪水，最低薪水，平均薪水并按工作单位降序排序;


	6、统计所有工作单位人员数并按工作单位进行升序排序，显示工作单位，人员数并按工作单位升序排序;


	7、查询所有姓王的所有员工信息;


	8、按工作单位，性别统计平均薪水，显示：工作单位,性别,平均薪水;


	9、查询30到40岁 平均薪水;


	10、查询工作经历在泽林的薪水最高的人，显示姓名


	11、删除王小明的所有信息



/*========================公司员工薪水管理系统start========================*/
/*
    总薪水=基本薪水+奖金
    关系：
        1、employ.deptid = dept.deptid(某个员工属于某个部门)
        2、employ.stationid = station.stationid(某个员工在某个部门任职的岗位)
        3、salary.employid = employ.employid(某个员工的薪新)
*/
create table dept(
       deptid number, 
       deptname varchar2(50)
);
alter table DEPT add constraint PK_DEPT primary key(DEPTID);
comment on table dept is '部门信息';
comment on column dept.deptid is '部门ID';
comment on column dept.deptname is '部门名称';

create table station(
       stationid number,
       stationname varchar2(50)
);
alter table STATION add constraint PK_STATION primary key (STATIONID);
comment on table station is '岗位信息';
comment on column station.stationid is '岗位ID';
comment on column station.stationname is '岗位名称';

create table employ(
       employID number,
       ename varchar2(50),
       sex varchar2(50),
       age number,
       deptid number,
       stationid number
); 
alter table EMPLOY add constraint PK_EMPLOY primary key (EMPLOYID);
comment on table employ is '员工信息';
comment on column employ.employID is '员工ID';
comment on column employ.ename is '员工姓名';
comment on column employ.sex is '性别';
comment on column employ.age is '年龄';
comment on column employ.deptid is '部门ID';
comment on column employ.stationid is '岗位ID';

create table salary(
       salaryid number,
       employid number,
       basesalary number,
       bonussalary number
);
alter table SALARY add constraint PK_salary primary key (SALARYID);
comment on table salary is '员工薪水';
comment on column salary.salaryid is '薪水ID';
comment on column salary.employid is '员工ID';
comment on column salary.basesalary is '基本薪水';
comment on column salary.bonussalary is '奖金';
/*========================公司员工薪水管理系统end========================*/



/*========================个人简历管理系统start========================*/
/*
    关系：
        1、 companystation.companyid = company.companyid(某个人所在某个公司任职岗位)
        2、 companystation.personid = person.personid(某个人所在某个公司任职岗位)
        3、 experience.companystationid = companystation.companystationid(某个人所有任职公司的工作经历)
*/
create table person(
       personID number,
       ename varchar2(50),
       sex varchar2(50),
       age number
); 
alter table PERSON add constraint PK_PERSON primary key (PERSONID);
comment on table person is '个人信息';
comment on column person.personID is '人员ID';
comment on column person.ename is '名称';
comment on column person.sex is '性别';
comment on column person.age is '年龄';

create table company(
       companyid number,
       companyname varchar2(50)
);
alter table COMPANY add constraint PK_COMPANY primary key (COMPANYID);
comment on table company is '工作单位';
comment on column company.companyid is '公司ID';
comment on column company.companyname is '公司名称';

create table companystation(
       companystationid number,
       companyid number,
       personid number,
       stationname varchar2(50)
);
alter table COMPANYSTATION add constraint PK_COMPANYSTATION primary key (COMPANYSTATIONID);
comment on table companystation is '个人所在公司的岗位';
comment on column companystation.companystationid is '个人所在公司的岗位ID';
comment on column companystation.companyid is '公司ID';
comment on column companystation.personid is '个人ID';
comment on column companystation.stationname is '岗位名称';

create table experience(
       experienceid number,
       companystationid number,
       startdate date,
       enddate date,
       descsr varchar2(1000),
       salary number
);
alter table EXPERIENCE add constraint PK_EXPERIENCE primary key (EXPERIENCEID);
comment on table experience is '个人工作经历';
comment on column experience.experienceid is '经历ID';
comment on column experience.companystationid is '个人所在公司的岗位ID';
comment on column experience.startdate is '工作起始日期';
comment on column experience.enddate is '工作结束日期';
comment on column experience.descsr is '工作描述';
comment on column experience.salary is '薪水';
/*========================个人简历管理系统end========================*/






