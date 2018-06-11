#coding:utf8
#python中文转换成拼音,汉字转拼音 word必须为unicode    pypinyin模块可以通过pip install安装
__author__ = 'liyatao'
from pypinyin import lazy_pinyin
def get_pinyin(word):
    word=unicode(word.decode('utf8'))   #汉字转拼音 word必须为unicode
    result=lazy_pinyin(word,errors="ignore")  #转换为拼音，忽略非中文转换不成功的。 返回一个列表
    result=''.join(result)  #把每个汉字的拼音连接起来
    print  result
    # return result

if __name__=="__main__":
    word="dddd5dd45d498ddd我是  ***20。。。d李亚涛]]]]]"
    #word="高铁是中国自主创新的典型成果，也是代表中国速度的一张国家名片。"
    get_pinyin(word)
