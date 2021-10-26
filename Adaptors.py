#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: Adaptors.py
@time: 2021/10/19 5:29 下午
"""

from abc import ABC, abstractmethod


class Target(ABC):
    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass


class NeedToAdapt(object):
    def __init__(self):
        pass

    def operation1(self):
        return "operation1"


class Adapter(NeedToAdapt, Target):
    def __init__(self):
        super().__init__()
        self.adapt = NeedToAdapt()

    def operation2(self):
        return "operation2"


class Adapter2(Target):
    def __init__(self):
        self.adapt = NeedToAdapt()

    def operation2(self):
        return "operation2"

    def operation1(self):
        return "operation1"


if __name__ == '__main__':
    aa = Adapter()
    aa.operation2()
    aa.operation1()

    aa2 = Adapter2()
    aa2.operation1()
    aa2.operation1()