# _*_ coding: utf-8 _*_

"""
  @Time    : 2023.11.16 15:35
  @File    : naiveBayes.py
  @Project : ml_in_action
  @Author  : Saitama
  @IDE     : PyCharm
  @Desc    : 使用朴素贝叶斯进行文本分类
"""


# 加载数据集
def load_dataset():
    postingList = [
        ['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
        ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
        ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
        ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
        ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
        ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']
    ]
    # 1 表示侮辱性文字，2 表示正常言论
    classVec = [0, 1, 0, 1, 0, 1]
    return postingList, classVec


def generate_vocab_list(dataset):
    vocabList = list()
    for sentence in dataset:
        vocabList.extend(sentence)
    vocabSet = set(vocabList)
    retList = list(vocabSet)
    retList.sort()
    return retList


def generate_vec(vocab, sentence):
    resVec = [0] * len(vocab)
    for word in sentence:
        if word in vocab:
            resVec[vocab.index(word)] = 1
        else:
            print("{} not in the vocabulary", word)
    return resVec


# 测试
if __name__ == '__main__':
    sentenceList, classVec = load_dataset()
    vocabList = generate_vocab_list(sentenceList)
    print("Vocabulary")
    print(vocabList)
    print()
    for sentence in sentenceList:
        vec = generate_vec(vocab=vocabList, sentence=sentence)
        print(sentence)
        print(vec)
        print()
