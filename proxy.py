#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: proxy.py.py
@time: 2021/10/22 2:43 下午
"""

"""
代理模式
"""

from abc import ABCMeta, abstractmethod



class FemaleA():
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return "目标"

class Male():

    __metaclass__ = ABCMeta

    @abstractmethod
    def send_flower(self):
        pass

    @abstractmethod
    def send_chocolate(self):
        pass

    @abstractmethod
    def send_book(self):
        pass

class MaleA(Male):
    def __init__(self, name, love_female):
        self.name = name
        self.love_female = FemaleA(love_female)

    def send_flower(self):
        print(f"{self.name} 送花给 {self.love_female.name}")

class Proxy(Male):
    def __init__(self, name, proxyed_name, love_female):
        self.name = name
        self.proxyed_to = MaleA(proxyed_name, love_female)

    def send_flower(self):
        self.proxyed_to.send_flower()


if __name__ == '__main__':
    p = Proxy('男B', '男A', '女A')
    p.send_flower() # 男b 是隐式的
