import jieba  # 导入jieba中文分词库
import math
import sys  # 导入命令行参数模块
import warnings

warnings.filterwarnings(action='ignore')  # 消除警告

file1 = open(sys.argv[1], 'r', encoding='utf-8')
file2 = open(sys.argv[2], 'r', encoding='utf-8')
answer = open(sys.argv[3], 'w', encoding='utf-8')
txt1 = file1.read()
txt2 = file2.read()
word1 = jieba.lcut(txt1)  # 通过结巴库对文本进行分词,并返回一个列表形式
word2 = jieba.lcut(txt2)


def li(word):
    dictionary = {}  # 创建一个空字典来存放重复词语次数
    for LER in word:  # 遍历文章中的词语，并输出重复词语的次数
        dictionary[LER] = 0
    for LER in word:
        dictionary[LER] = dictionary[LER] + 1
    return dictionary


dictionary1 = li(word1)
dictionary2 = li(word2)
a = 0
for ler in dictionary1:
    if ler in dictionary2:
        a = a + dictionary1[ler] * dictionary2[ler]
b = 0
for ler in dictionary1:
    b = b + dictionary1[ler] ** 2
c = 0
for ler in dictionary2:
    c = c + dictionary2[ler] ** 2

cos = a / (math.sqrt(b) * math.sqrt(c))  # 余弦相似度公式计算论文重复率
answer.write(str(cos))
print(cos)
print('参数个数:', len(sys.argv))
print('参数列表:', str(sys.argv))
