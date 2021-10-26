#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: bridge.py
@time: 2021/10/19 5:39 下午
"""


class EchoEnglish:

    def run(self, name):
        print("my name is :{}".format(name))


class EchoChinese:

    def run(self, name):
        print("我的名字是：{}".format(name))


class Bridge:

    def __init__(self, ager, classname):
        self.ager = ager
        self.classname = classname

    def bridge_run(self):
        self.classname.run(self.ager)


if __name__ == '__main__':
    test = Bridge('李华', EchoChinese())
    test.bridge_run()

    test.ager = 'Tome'
    test.bridge_run()

    test.classname = EchoEnglish()
    test.bridge_run()

    test.ager = '李华'
    test.bridge_run()
