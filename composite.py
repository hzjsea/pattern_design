#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: composite.py.py
@time: 2021/10/19 6:24 下午
"""
import abc
from abc import ABC


# 抽象一个组织类
class Component(ABC):

    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def add(self,comp):
        pass

    @abc.abstractmethod
    def remove(self,comp):
        pass

    @abc.abstractmethod
    def display(self, depth):
        pass


# 叶子节点
class Leaf(Component):

    def add(self, comp):
        print('不能添加下级节点')

    def remove(self,comp):
        print('不能删除下级节点')

    def display(self, depth):
        strtemp = ''
        for i in range(depth):
            strtemp += strtemp+'-'
        print(strtemp+self.name)


# 枝节点
class Composite(Component):

    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.children = []

    def add(self,comp):
        self.children.append(comp)

    def remove(self,comp):
        self.children.remove(comp)

    def display(self, depth):
        strtemp = ''
        for i in range(depth):
            strtemp += strtemp+'-'
        print(strtemp+self.name)
        for comp in self.children:
            comp.display(depth+2)


if __name__ == "__main__":
    # 生成树根
    root = Composite("root")
    # 根上长出2个叶子
    root.add(Leaf('leaf A'))
    root.add(Leaf('leaf B'))

    # 根上长出树枝Composite X
    comp = Composite("Composite X")
    comp.add(Leaf('leaf XA'))
    comp.add(Leaf('leaf XB'))
    root.add(comp)

    # 根上长出树枝Composite X
    comp2 = Composite("Composite XY")
    # Composite X长出2个叶子
    comp2.add(Leaf('leaf XYA'))
    comp2.add(Leaf('leaf XYB'))
    root.add(comp2)
    # 根上又长出2个叶子,C和D,D没长好,掉了
    root.add(Leaf('Leaf C'))
    leaf = Leaf("Leaf D")
    root.add(leaf)
    root.remove(leaf)
    # 展示组织
    root.display(1)