#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: single.py
@time: 2021/10/19 2:17 下午
"""


def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton


@Singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


if __name__ == '__main__':

    a1 = A(2)
    a2 = A(3)
    print(id(a1))
    print(id(a2))