import jieba # jieba中文分词库

with open('test.txt', 'r', encoding='UTF-8') as novelFile:
    novel = novelFile.read()
# print(novel)
stopwords = [line.strip() for line in open('stop.txt', 'r', encoding='UTF-8').readlines()]
novelList = list(jieba.lcut(novel))
novelDict = {}

# 统计出词频字典
for word in novelList:
    if word not in stopwords:
            # 不统计字数为一的词
            if len(word) == 1:
                continue
            else:
                novelDict[word] = novelDict.get(word, 0) + 1

# 对词频进行排序
novelListSorted = list(novelDict.items())
novelListSorted.sort(key=lambda e: e[1], reverse=True)

# 打印前10词频
topWordNum = 0
for topWordTup in novelListSorted[:10]:
    print(topWordTup)

from matplotlib import pyplot as plt
x = [c for c,v in novelListSorted]
y = [v for c,v in novelListSorted]
plt.plot(x[:10],y[:10],color='r')
plt.show()


