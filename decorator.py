#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: decorator.py.py
@time: 2021/10/19 6:37 下午
"""

"""
装饰模式
总的来说就是创建一个可扩展的对象，保证后期代码维护中可以动态的扩展对象内容
"""

from abc import ABCMeta, abstractmethod


# 主类
class Person(object):
    def __init__(self, name: str):
        self.name = name
        self.component = ""

    # 动态函数
    def decorator(self, component):
        self.component = component

    def show(self):
        print(f"{self.name} 开始穿衣")
        self.component.show()


# 扩展类

class Expand(object):
    def __init__(self):
        self.component = None

    def decorator(self, component):
        self.component = component

    __metaclass__ = ABCMeta

    @abstractmethod
    def show(self):
        if self.component:
            self.component.show() # 调用扩展类当中的方法


class TShirt(Expand):
    def __init__(self):
        super(TShirt, self).__init__()

    def show(self):
        Expand.show(self)
        print("chuan tshirt")


class Trouser(Expand):
    def __init__(self):
        super(Trouser, self).__init__()

    def show(self):
        Expand.show(self)
        print("chuan trouser")


class Shoe(Expand):
    def __init__(self):
        super(Shoe, self).__init__()

    def show(self):
        Expand.show(self)
        print("chuan shoe")


class Tie(Expand):
    def __init__(self):
        super(Tie, self).__init__()

    def show(self):
        Expand.show(self)
        print("chuan tie")


if __name__ == '__main__':
    p = Person("h")
    # 开始装饰
    tshirt = TShirt()
    trouser = Trouser()
    shoe = Shoe()
    tie = Tie()

    trouser.decorator(tshirt)
    shoe.decorator(trouser)
    tie.decorator(shoe)
    p.decorator(tie)
    p.show()
