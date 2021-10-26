#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: factory.py.py
@time: 2021/10/19 11:35 上午
"""


class Mmember(object):
    def __init__(self):
        pass

    def __repr__(self) -> str:
        return "member name is M"


class Qmember(object):
    def __init__(self):
        pass

    def __repr__(self) -> str:
        return "member name is Q"


class MemberGenerate(object):
    """简单工厂
    """
    def __init__(self):
        pass

    @staticmethod
    def generate_member(name: str) -> str:
        if name.upper() == "M":
            return "member name is M"
        elif name.upper() == "Q":
            return "member name is Q"

import abc


class AbstractFactory(object):
    """抽象工厂
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def generate_member(self):
        pass

    @abc.abstractmethod
    def add_newfunc(self):
        pass


class QmemberFactory(AbstractFactory):
    def generate_member(self):
        return Qmember()

    def add_newfunc(self):
        return "add_new function is Q"


class MmemberFactory(AbstractFactory):
    def generate_member(self):
        return Mmember()

    def add_newfunc(self):
        return "add_new function is M"


if __name__ == '__main__':
    mr = Mmember()
    qr = Qmember()
    print(f"mr => {mr}\nqr => {qr}")

    mr = MemberGenerate.generate_member("M")
    qr = MemberGenerate.generate_member("Q")
    print(f"mr => {mr}\nqr => {qr}")

    mr = MmemberFactory().generate_member()
    qr = QmemberFactory().generate_member()
    print(f"mr => {mr}\nqr => {qr}")

    print(f"mr => {MmemberFactory().add_newfunc()}\nqr => {QmemberFactory().add_newfunc()}")
