#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: Generator.py.py
@time: 2021/10/19 12:29 下午
"""

from abc import ABCMeta, abstractmethod, ABC
from typing import Any


class Builder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self, part_a: str) -> None:
        pass

    @abstractmethod
    def produce_part_b(self, part_b: str) -> None:
        pass

    @abstractmethod
    def produce_part_c(self, part_c: str) -> None:
        pass


class Produce(object):
    """产品模板 """
    def __init__(self, name):
        self.name = name
        self.part_a = ""
        self.part_b = ""
        self.part_c = ""

    def __str__(self):
        return "-".join([self.name, self.part_a, self.part_b, self.part_c])


class ProduceBuilder(Builder):
    """建造者"""
    def __init__(self, name):
        self.produce = Produce(name)

    def product(self) -> Produce:
        return self.produce

    def produce_part_a(self, part_a) -> None:
        self.produce.part_a = part_a

    def produce_part_b(self, part_b) -> None:
        self.produce.part_b = part_b

    def produce_part_c(self, part_c) -> None:
        self.produce.part_c = part_c


class Engineer(object):
    """指挥者 """
    def __init__(self):
        self.builder = None

    def build(self, name, part_a, part_b, part_c) -> Produce:
        self.builder = ProduceBuilder(name)
        self.builder.produce_part_a(part_a)
        self.builder.produce_part_b(part_b)
        self.builder.produce_part_c(part_c)
        return self.builder.product()


if __name__ == '__main__':
    en = Engineer()
    res = en.build("xx", "parta", "partb", "partc")
    print(res)



# https://zhuanlan.zhihu.com/p/366156798
# https://segmentfault.com/a/1190000013089924
# https://blog.csdn.net/sinat_33455447/article/details/115336163