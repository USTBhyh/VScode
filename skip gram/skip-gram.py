import collections
import numpy as np
import time
import random

'''
处理文本数据，替换特殊符号、同义词，根据物体出现次数输出最终的物体排序
    text: 文本数据
    freq: 词频阈值
输出：经过预处理的物体
'''
def preprocess(text, freq=0):

    # 替换文本中特殊符号
    text = text.lower()
    # lower() 字符串中所有大写字符转为小写
    # text = text.replace('.', ' <PERIOD> ')
    # text = text.replace(',', ' <COMMA> ')
    # text = text.replace('"', ' <QUOTATION_MARK> ')
    # text = text.replace(';', ' <SEMICOLON> ')
    # text = text.replace('!', ' <EXCLAMATION_MARK> ')
    # text = text.replace('?', ' <QUESTION_MARK> ')
    # text = text.replace('(', ' <LEFT_PAREN> ')
    # text = text.replace(')', ' <RIGHT_PAREN> ')
    # text = text.replace('--', ' <HYPHENS> ')
    # text = text.replace('?', ' <QUESTION_MARK> ')
    # text = text.replace(':', ' <COLON> ')

    # text = text.replace('fire hydrant', 'firehydrant')
    # text = text.replace('stop sign', 'stopsign')
    # text = text.replace('parking meter', 'parkingmeter')
    #  text = text.replace('sports ball', 'sportsball')
    # text = text.replace('baseball bat', 'baseballbat')
    # text = text.replace('baseball glove', 'baseballglove')
    # text = text.replace('tennis racket', 'tennisracket')
    # text = text.replace('potted plant', 'pottedplant')
    # text = text.replace('dining table', 'diningtable')
    # text = text.replace('cell phone', 'cellphone')
    # text = text.replace('teddy bear', 'teddybear')
    # text = text.replace('hair drier', 'hairdrier')
    # text = text.replace('hot dog', 'hotdog')
    # text = text.replace('wine glass', 'wineglass')
    '''
    # kitchen用
    text = text.replace('dining table', 'diningtable')
    text = text.replace('laptop', 'tv')
    text = text.replace('potted plant', 'diningtable')
    text = text.replace('vase', 'diningtable')
    text = text.replace('cup', 'bottle')
    text = text.replace('chair', 'chair diningtable')
    text = text.replace('oven', 'oven microwave microwave')
    text = text.replace('bowl', 'bowl bottle bottle')
    text = text.replace('wine glass', 'wineglass bottle bottle')
    text = text.replace('tv', 'oven oven')
    text = text.replace('refrigerator', 'refrigerator sink sink')

    # newkitchen用
    text = text.replace('', '')


    text = text.replace('person', ' ')
    text = text.replace('airplane', ' ')
    text = text.replace('cat', ' ')
    text = text.replace('skateboard', ' ')
    text = text.replace('remote', ' ')
    text = text.replace('suitcase', ' ')
    text = text.replace('mouse', ' ')
    text = text.replace('keyboard', ' ')
    text = text.replace('toilet', ' ')
    text = text.replace('bird', ' ')
    text = text.replace('book', ' ')
    '''


    words = text.split()
    # split() 通过指定分隔符对字符串进行切片，默认为空格，如果参数 num 有指定值，则分隔 num+1 个子字符串

    # 删除低频词，减少噪音影响
    # 获得words中不同物体出现的次数
    word_counts = collections.Counter(words)
    # 保留出现次数大于freq的物体名称
    trimmed_words = [word for word in words if word_counts[word] > freq]
    
    # print(trimmed_words)  有重复的
    return trimmed_words

'''
输入：txt文件的路径、t、阈值、文本出现的频数
输出：(int_to_vocb)以字典的形式输出训练单词：{0:a,1:b，……}
     (train_word)以数字的形式训练单词(出现频数大于freq的单词)
'''
def get_train_words(path, t, threshold, freq):
    with open(path) as f:
        text = f.read()
    # 获得经过预处理的单词，包括重复的单词
    words = preprocess(text, freq)

    # 删去重复的单词
    vocab = set(words)  
    # set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。

    # 词向量表示：单词
    # 对原文本进行vocab到int的转换
    # 使用int数字表示物体类别
    vocab_to_int = {w: c for c, w in enumerate(vocab)} #word：num
    int_to_vocab = {c: w for c, w in enumerate(vocab)}  #num:word
    # 根据去重单词序列将预处理过的物体以数字的形式表现出来 
    int_words = [vocab_to_int[w] for w in words] # num

    # 统计单词出现频次
    int_word_counts = collections.Counter(int_words)

    total_count = len(int_words)
    # 计算单词频率
    word_freqs = {w: c / total_count for w, c in int_word_counts.items()}
    # 计算被删除的概率
    prob_drop = {w: 1 - np.sqrt(t / word_freqs[w]) for w in int_word_counts}
    # 对单词进行采样
    train_words = [w for w in int_words if prob_drop[w] < threshold]
    return int_to_vocab, train_words


'''
获得中心词的上下文单词列表
words: 单词列表
idx: input word的索引号
window_size: 窗口大小

'''

def get_targets(words, idx, window_size):
    target_window = np.random.randint(1, window_size + 1)   # 1 <= 数值范围 < window_size + 1
    # 这里要考虑input word前面单词不够的情况
    start_point = idx
                  # - target_window if (idx - target_window) > 0 else 0
    end_point = idx + target_window
    # output words(即窗口中的上下文单词)
    targets = set(words[start_point: idx] + words[idx + 1: end_point + 1])
    return list(targets)

'''
将中心词的上下文单词列表一一与中心词配对
words[idx], y
中心词      上下文
words:训练物体名称
windows_size :窗口大小
'''
def get_batches(words, window_size):

    for idx in range(0, len(words)):
        targets = get_targets(words, idx, window_size)
        # print(targets)
        for y in targets:
            yield words[idx], y

def softmax(vector):
    res = np.exp(vector)
    e_sum = np.sum(res)
    res /= e_sum
    return res

def sigmoid(inp):
    return 1.0 / (1.0 + 1.0 / np.exp(inp))

def sigmiod_grad(inp):
    return inp * (1 - inp)

def neg_forward_backword(input_vectors, output_vectors, in_idx, out_idx, sigma, vocabulary_size, K=10):
    epsilon = 1e-5

    # 第(in_idx-1)行的向量 1*200
    hidden = input_vectors[in_idx]
    # 1*k维的随机数阵列
    neg_idxs = neg_sample(vocabulary_size, out_idx, K)
    # 对输入产生逻辑分类的函数 output_vectors[out_idx]和hidden对应位置相乘再求和 0<tmp<1
    tmp = sigmoid(np.dot(output_vectors[out_idx], hidden))
    hidden_grad = (tmp - 1.0) * output_vectors[out_idx]
    output_vectors[out_idx] -= sigma * (tmp - 1.0) * hidden
    loss = -np.log(tmp + epsilon)
    for idx in neg_idxs:
        tmp = sigmoid(np.dot(output_vectors[idx], hidden))
        loss -= np.log(1.0 - tmp + epsilon)
        hidden_grad += tmp * output_vectors[idx]
        output_vectors[idx] -= sigma * tmp * hidden
    input_vectors[in_idx] -= sigma * hidden_grad
    return loss

def neg_sample(vocabulary_size, out_idx, K):
    res = [None] * K
    # print(res)
    for i in range(K):
        tmp = np.random.randint(0, vocabulary_size)
        while tmp == out_idx:
            tmp = np.random.randint(0, vocabulary_size)
        res[i] = tmp
        # print(res)
    return np.array(res)

'''
随机构造验证集，并计算验证集中物体与输入物体余弦相似度

输入：input_vectors 无重复的物体单词
输出：余弦相似度，验证集大小，验证集
'''
def get_simi(input_vectors):
    valid_size = 18     # 原来是16//8//24
    valid_window = 9   # 原来是18//5//12 （有几种类型的关联规则生成）
    # 从valid_window随机选出8个元素构造验证集
    # random.sample（list,n） 从list中随机获得n个元素返回
    valid_examples = np.array(random.sample(range(valid_window), valid_size // 2))
    #valid_examples = np.append(valid_examples,random.sample(range(1000, 1000 + valid_window), valid_size // 2))
    valid_size = len(valid_examples)

    # 计算每个词向量的模并进行单位化
    norm = np.sqrt(np.square(input_vectors).sum(axis=1)).reshape(len(input_vectors), 1)
    normalized_embedding = input_vectors / norm

    # 查找验证单词的词向量
    valid_embedding = normalized_embedding[valid_examples]
    # 计算余弦相似度
    similarity = np.dot(valid_embedding, normalized_embedding.T)

    return similarity, valid_size, valid_examples

if __name__ == "__main__":
    #path = 'C:/Users/zhaoz/Desktop\\1-kitchen.txt'
    path = './0000.txt' 
    t = 1e-5
    # 这里是小南瓜帮我改过的！！！！！他说原来是0.8
    threshold = 1.0  # 剔除概率阈值
    windows = 3
    freq = 300   # 之前是2
    int_to_vocab, train_words = get_train_words(path, t, threshold, freq)
    np.save('int_to_vocab', int_to_vocab)
    # np.save 以npy格式将数组保存到二进制文件中。
    vocabulary_size = len(int_to_vocab) # 有多少个无重复单词
    #print(vocabulary_size)
    vector_dimension = 200
    # 构建vocabulary_size*vector_dimension维的随机阵列，（物体数量*物体标签向量）
    input_vectors = np.random.random([vocabulary_size, vector_dimension])   
    output_vectors = np.random.random([vocabulary_size, vector_dimension])
    epochs = 10 #
    sigma = 0.01
    K = 10
    iter = 1
    # 对单词训练epochs次
    # 每一次都需要重新获得batches
    for e in range(1, epochs + 1):
        if e > 1:
            sigma = 0.001
        elif e > 3:
            sigma = 0.0001
        loss = 0
        batches = get_batches(train_words, windows)
        # start = time.time()
        for x, y in batches:
            loss += neg_forward_backword(input_vectors, output_vectors, x, y, sigma, vocabulary_size, K)
            # 打印信息
            if iter :  
                # end = time.time()
                print("Epoch {}/{}".format(e, epochs),
                      "Iteration: {}".format(iter),
                      "Avg. Training loss: {:.4f}".format(loss / 100000),
                      # "{:.4f} sec/100000".format((end - start))
                      )
            # loss = 0
            # start = time.time()
            # 这里是小南瓜帮我改过的！！！！！
            np.save('input_vectors', input_vectors)
            similarity, valid_size, valid_examples = get_simi(input_vectors)
            for i in range(valid_size):
                valid_word = int_to_vocab[valid_examples[i]]
                top_k = 8  # 取最相似单词的前6个 之前是8
                temp1 = (-similarity[i, :])
                temp = temp1.argsort()
                # argsort()函数是将x中的元素从小到大排列，输出其对应的索引
                nearest = temp[1:top_k + 1]
                log = 'Nearest to [%s]:' % valid_word
                for k in range(top_k):
                    close_word = int_to_vocab[nearest[k]]
                    log = '%s %s %0.3f' % (log, close_word, similarity[i, :][temp[k]])
                with open("./0001.txt", "a") as t:  # 打开文件
                    t.write(log + "\n")  # 写入文件
                if iter % 10000 == 0:
                    print(log)
            iter += 1
