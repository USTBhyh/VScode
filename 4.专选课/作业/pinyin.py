# -*- coding:utf-8 -*-
'''
@File    :   pinyin.py
@Time    :   2022/03/26 22:51:53
@Author  :   hyh
@Version :   1.0
@Contact :   1360895771@qq.com
@Desc    :   None
'''
# here put the import lib
import pypinyin as py
list = py.lazy_pinyin("侯云浩")
print(list[0])


if __name__ == '__main__':
    pass
