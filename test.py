def lo(word):
    for c in word:
        if c < '\u4e00' or c > '\u9fa5':
            return False
    return True  # 去除文本中的符号

def li(word):
    dictionary = {}  # 创建一个空字典来存放重复词语次数
    for LER in word:  # 遍历文章中的词语，并输出重复词语的次数
        if lo(LER) : dictionary[LER] = 0
    for LER in word:
        if lo(LER) : dictionary[LER] = dictionary[LER] + 1
    return dictionary


word = ['我','是','尿频','马', '我','.','!']
dt = li(word)

print(dt)
