####Preprocess=================================================================
import os
import jieba
import pickle
from sklearn.datasets.base import Bunch#类似字典的数据结构

train_file = './char-level/cnews.train.txt'#训练集路径
test_file = './char-level/cnews.test.txt'#测试集路径
val_file = './char-level/cnews.val.txt'#验证集路径
category_file = './char-level/cnews.category.txt'#类别的信息路径

new_file='./word-level/'#新目录
word_level_file='./word-level/train.jieba.bat'#新bat文档

if not os.path.exists(new_file):#如果目录不存在，创建新目录
	os.mkdir(new_file)

#处理类别文件，将类别文件内容写成字典，并获得对应类别的标签
class Categories:
	def __init__(self,path_file):#类别和标签对应的字典
		self.category_label={}
		for line in open(path_file,'r',encoding='utf-8'):#打开遍历文件内容
			category,label = line.strip().split('\t')#清除strip，拆分split
			self.category_label[category]=label#写入字典

	def category_to_label(self,category):#获得对应类别的标签
		#print(self.category_label[category])
		return self.category_label[category]
'''
c=Categories(category_file)
c.category_to_label('体育')
'''
def generate_word(inputfilelist,outputfile):
	'''
	处理文章的内容和类别：
	内容部分：通过结巴分词，组织成英语的形式；
	类别部分：转化为类别标签
	并将处理的结果进行保存
	'''
	bunch = Bunch(category_label={},labels=[],contents=[])#声明Bunch包含的信息和类型
	categories=Categories(category_file)#调用上面的类别处理对象
	bunch.category_label=categories.category_label#把类别和标签赋值bunch.category_label
	for inputfile in inputfilelist:#处理文件[train_file,val_file,test_file]
		print('开始处理'+inputfile)
		i=0
		with open(inputfile,'r',encoding='utf-8') as f:#打开文件集
			lines = f.readlines()#读取
		#处理文章和类别
		for line in lines:
			words = ''
			category,content = line.strip().split('\t')
			label=categories.category_to_label(category)#把文章类别转化为标签
			bunch.labels.append(label)
			word_list=jieba.cut(content.strip())#结巴分词
			for word in word_list:
				word = word.strip()
				if word != '':
					words +=word + ' '
			bunch.contents.append(words.strip())#把处理之后的文章内容信息添加到bunch
			i += 1
		print(i)
	#保存数据
	with open(outputfile,'wb') as fout:#写入保存到word_level_file

		pickle.dump(bunch,fout)

generate_word([train_file,val_file,test_file],word_level_file)#处理文件[train_file,val_file,test_file],写入保存到word_level_file

####Preprocess-test=====================================================================
import pickle
#from sklearn.datasets.base import Bunch

with open('./word-level/train.jieba.bat','rb') as ff:
	bunch = pickle.load(ff)
print(bunch.category_label)
print(bunch.labels[-10:])

####tfidftransform=======================================================================
import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets.base import Bunch#类似字典的数据结构

word_level_file='./word-level/train.jieba.bat'
word_tfidf_file='./word-level/train.tfidf.bat'

#读文件
def _read_file(filepath):
    with open(filepath,'rb') as f:
        bunch = pickle.load(f)
    return bunch
#写文件
def _wirte_file(filepath,bunch):
    with open(filepath,'wb') as f:
        pickle.dump(bunch,f)

#获取停用词
def get_stop_words(filepath='./中文停用词库.txt'):
	stop_words = []
	for line in open(filepath,'r',encoding='gb18030'):
		stop_words.append(line.strip())
	return stop_words

#tfidf量化文章信息
def gen_tfidf(inputfile,output):
	bunch = _read_file(inputfile)#读取之前处理后的内容
	tfidf_bunch = Bunch(category_lables={},labels=[],vocabulary={})#声明Bunch包含的信息和类型
	tfidf_bunch.category_labels=bunch.category_label#类别和标签对应的字典
	tfidf_bunch.labels = bunch.labels#文章的标签
	stop_words =  get_stop_words()#引用停用词
	tfidf = TfidfVectorizer(stop_words=stop_words,sublinear_tf=True,max_df=0.8)
	tfidf_bunch.tfidf=tfidf.fit_transform(bunch.contents)#tfidf转化后文章信息
	tfidf_bunch.vocabulary = tfidf.vocabulary_#词汇对照字典
	#保存信息
	_wirte_file(output,tfidf_bunch)

gen_tfidf(word_level_file,word_tfidf_file)

####model================================================================================
import pickle
import os
from sklearn.datasets.base import Bunch#类似字典的数据结构
from sklearn.naive_bayes import MultinomialNB#导入朴素贝叶斯模型
word_tfidf_file='./word-level/train.tfidf.bat'
#读文件
def _read_file(filepath):
	with open(filepath,'rb') as f:
		bunch = pickle.load(f)
	return bunch

bunch = _read_file(word_tfidf_file)#获取文件内的信息

X=bunch.tfidf#提取数据集的特征
print(X.shape)
print(type(X))

y=bunch.labels#提取数据集的标签
print(len(y))
print(y[:10])

#拆分数据集
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=1)

#建立模型
nb = MultinomialNB(alpha=0.01)
nb.fit(X_train,y_train)#训练模型

from sklearn.metrics import classification_report#模型评估模块

y_pred = nb.predict(X_test)
print(classification_report(y_test,y_pred))

from sklearn.metrics import confusion_matrix#混淆矩阵，查看实际结果跟预测结果的矩阵
print(confusion_matrix(y_test,y_pred))

from sklearn.metrics import precision_score#导入查准率模块
from sklearn.metrics import recall_score#导入查全率模块
alphas = [0.001,0.01,0.1,1]#参数列表
for alpha in alphas:
	nb1 = MultinomialNB(alpha=alpha)#初始化朴素贝叶斯分类器，加入参数
	nb1.fit(X_train,y_train)# 训练集合上进行训练， 估计参数
	y_pred1 = nb1.predict(X_test)# 对测试集合进行预测 保存预测结果
	precision=precision_score(y_test,y_pred1,average='weighted')
	recall = recall_score(y_test,y_pred1,average='weighted')
	print(alpha,precision,recall)
