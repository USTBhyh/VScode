# -*- coding:utf-8 -*-
'''
@File    :   11.基于朴素贝叶斯实现文本分类.py
@Time    :   2022/03/27 12:00:46
@Author  :   hyh
@Version :   1.0
@Contact :   1360895771@qq.com
@Desc    :   使用朴素贝叶斯方法解决文本分类问题
'''
# here put the import lib
#导入必要的包
import random
import jieba  # 处理中文
from sklearn import model_selection
from sklearn.naive_bayes import MultinomialNB
import re,string




# 1.数据集介绍
# 网上公开中文新闻数据：
# 数据来源：从中文新闻网站上爬取56821条新闻摘要数据。
# 数据内容：数据集中包含10个类别
# 数据划分：本次实践将其中90%作为训练集，10%作为验证集。

# 关于特征词和特征向量：
# 【举例说明】
# 停用词：是、的、你、我、他，这、那
# 特征词：[‘中国’，’西安‘，’天安门‘，’首都‘，’故宫’，‘机器学习’，’北京‘]
# text：北京是中国的首都
# 通过分词之后 [北京，是，中国，的，首都]
# 去除停用词：[北京，中国，首都]
# 形成特征向量：[1,0,0,1,0,0,1]

def text_to_words(file_path):
    '''
    分词
    return:sentences_arr, lab_arr
    '''
    sentences_arr = []
    lab_arr = []
    with open(file_path,'r',encoding='utf8') as f:
        for line in f.readlines():
            lab_arr.append(line.split('_!_')[1])
            sentence = line.split('_!_')[-1].strip()
            sentence = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）《》：]+", "",sentence) #去除标点符号
            sentence = jieba.lcut(sentence, cut_all=False)
            sentences_arr.append(sentence)
    return sentences_arr, lab_arr

    
def load_stopwords(file_path):
    '''
    创建停用词表
    参数 file_path:停用词文本路径
    return：停用词list
    '''
    stopwords = [line.strip() for line in open(file_path, encoding='UTF-8').readlines()]
    return stopwords


def get_dict(sentences_arr,stopswords):
    '''
    遍历数据，去除停用词，统计词频
    return: 生成词典
    '''
    word_dic = {}
    for sentence in sentences_arr:
        for word in sentence:
            if word != ' ' and word.isalpha():
                if word not in stopswords:
                    word_dic[word] = word_dic.get(word,1) + 1
    word_dic=sorted(word_dic.items(),key=lambda x:x[1],reverse=True) #按词频序排列

    return word_dic


def get_feature_words(word_dic,word_num):
    '''
    从词典中选取N个特征词，形成特征词列表
    return: 特征词列表
    '''
    n = 0
    feature_words = []
    for word in word_dic:
        if n < word_num:
            feature_words.append(word[0])
        n += 1
    return feature_words

# 文本特征
def get_text_features(train_data_list, test_data_list, feature_words):
    '''
    根据特征词，将数据集中的句子转化为特征向量
    '''
    def text_features(text, feature_words):
        text_words = set(text)
        features = [1 if word in text_words else 0 for word in feature_words] # 形成特征向量
        return features
    train_feature_list = [text_features(text, feature_words) for text in train_data_list]
    test_feature_list = [text_features(text, feature_words) for text in test_data_list]
    return train_feature_list, test_feature_list

#获取分词后的数据及标签
sentences_arr, lab_arr = text_to_words('data/data6826/news_classify_data.txt')
#加载停用词
stopwords = load_stopwords('data/data43470/stopwords_cn.txt')
# 生成词典
word_dic = get_dict(sentences_arr,stopwords)
#数据集划分
train_data_list, test_data_list, train_class_list, test_class_list = model_selection.train_test_split(sentences_arr, 
                                                                                                      lab_arr, 
                                                                                                      test_size=0.1)
#生成特征词列表
feature_words =  get_feature_words(word_dic,10000)

#生成特征向量
train_feature_list,test_feature_list = get_text_features(train_data_list,test_data_list,feature_words)

from sklearn.metrics import accuracy_score,classification_report
#获取朴素贝叶斯分类器
classifier = MultinomialNB(alpha=1.0,  # 拉普拉斯平滑
                          fit_prior=True,  #否要考虑先验概率
                          class_prior=None)

#进行训练                        
classifier.fit(train_feature_list, train_class_list)
# 在验证集上进行验证
predict = classifier.predict(test_feature_list)
test_accuracy = accuracy_score(predict,test_class_list)
print("accuracy_score: %.4lf"%(test_accuracy))
print("Classification report for classifier:\n",classification_report(test_class_list, predict))

#加载句子，对句子进行预处理
def load_sentence(sentence):
    sentence = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）《》：]+", "",sentence) #去除标点符号
    sentence = jieba.lcut(sentence, cut_all=False)
    return sentence

lab = [ '文化', '娱乐', '体育', '财经','房产', '汽车', '教育', '科技', '国际', '证券']

#p_data = '【中国稳健前行】应对风险挑战必须发挥制度优势'
p_data = '北京科技大学是一所211双一流名校'
sentence = load_sentence(p_data)
sentence= [sentence]
print('分词结果:', sentence)
#形成特征向量
p_words = get_text_features(sentence,sentence,feature_words)
res = classifier.predict(p_words[0])
print("所属类型：",lab[int(res)])
