# -*- coding:utf-8 -*-

import gensim
import json
import jieba
import glob
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def readfile(filename):
    with open(filename, 'r') as fp:
        dict1 = json.load(fp, encoding='utf-8')
    return dict1


def writefile(filename, dict1):
    with open(filename, 'w') as f:
        json.dump(dict1, f)


def train_embedding(sentences,iter=30):
    #iter为迭代次数
    #sentences = [["data", "science"], ["vidhya", "science", "data", "analytics"],["machine", "learning"], ["deep", "learning"]]
    model = gensim.models.Word2Vec(sentences=sentences,min_count=1,iter=iter)
    return model


def save_model(model, local):
    model.save(local)


def load_model(local):
    new_model = gensim.models.Word2Vec.load(local)
    return new_model


def get_word_similar(word,model):
    model_ = model.most_similar(word)
    # for i in model_:
    #     print i
    return model_


def segmentation(doc):
    doc_cut_word = []
    segmentation_doc = jieba.cut(doc)
    for i in segmentation_doc:
        doc_cut_word.append(i)
    return doc_cut_word


def addword(new_word):
    for word in new_word:
        jieba.add_word(word)

def get_dict():
    all_dict_word = []
    all_dict_local = glob.glob('dict/*')
    for dict_local in all_dict_local:
        with open(dict_local,'r') as f:
            words = [line.strip().decode('utf-8') for line in f.readlines()]
            for word in words:
                word = word.split(' ')[0]
                all_dict_word.append(word)
    return all_dict_word


if __name__ == '__main__':
    # all_dict_word = get_dict()
    # addword(all_dict_word)
    # all_word = []
    # all_document_name = glob.glob('simplified_corpus/*')
    # for document_name in all_document_name:
    #     article_list = readfile(document_name)
    #     for article in article_list:
    #         all_word.append(segmentation(article[u'内容']))
    # model = train_embedding(all_word)

    # save_model(model,'mymodel1')
    model = load_model('mymodel1')
    # all_dict_word = get_dict()
    # print len(all_dict_word) # 1699
    # new_dict = []
    # throw_dict = []
    # for i in all_dict_word:
    #     # 如果该词没被抛掉
    #     if i not in throw_dict:
    #         # 尝试该词是否出现在model里面，如果没有则直接加入new_dict
    #         try:
    #             get_word_similar(i,model)
    #         except:
    #             new_dict.append(i)
    #             continue
    #
    #         # 该词存在于model里面，添加至new_dict
    #         new_dict.append(i)
    #
    #         # 循环判断是否有关联词
    #         for j in all_dict_word:
    #             # 如果j不等于i且j没有在new_dict和throw_dict里面则进入判断
    #             if j != i and j not in new_dict and j not in throw_dict:
    #
    #                 try:
    #                     if model.similarity(i,j) >0.6:
    #                         throw_dict.append(j)
    #                 except:
    #                     new_dict.append(j)
    #
    # print len(new_dict)
    # fp = open('new_dict','w')
    # for i in new_dict:
    #     fp.write(str(i))
    #     fp.write('\n')
    # fp.close()





    a = get_word_similar(u'工作',model)
    try:
        for i in a:
            print i[0]
    except:
        pass
    # print new_model
    # print model['first']
    # print model.similarity('first', 'one')
    # print model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)
    # print model.most_similar('first')