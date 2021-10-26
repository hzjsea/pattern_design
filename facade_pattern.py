#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: facade_pattern.py
@time: 2021/10/26 11:05 上午
"""
from abc import  ABCMeta, abstractmethod

class EquipmentABC():

    __metaclass__ = ABCMeta

    def __init__(self, name, state):
        self.name = name
        self.state = state

    @abstractmethod
    def turn_off(self):
        pass


class Equipment(EquipmentABC):
    def __init__(self, name, state):
        self.name = name
        self.state = state

    def turn_off(self):
        if self.state == "off":
            self.state = "open"
        else:
            self.state = "off"

class Fan(Equipment):
    def __init__(self, fan, state):
        super(Fan, self).__init__(fan,state)
        self.name = fan


class Lamp(Equipment):
    def __init__(self, lamp, state):
        super(Lamp, self).__init__(lamp, state)
        self.name = lamp


class Normal(object):
    def __init__(self, fan, lamp):
        self.fan = fan
        self.lamp = lamp

    def leave_home(self):
        self.fan.turn_off()
        self.lamp.turn_off()

class FacadeEquipment(object):
    def __init__(self, fan, lamp):
        self.fan = fan
        self.lamp = lamp

    def close(self):
        self.fan.turn_off()
        self.lamp.turn_off()

class FacadeEquipment2(object):
    """
    这家人只有点灯没有风扇
    """
    def __init__(self, fan):
        self.fan = fan

    def close(self):
        self.fan.turn_off()

class Facade(object):
    """
    上面包了一层，所以下面直接调用就可以了
    对于不同的内容，封装的内容可以不通
    """
    def __init__(self, equipment: object):
        self.equipment = equipment

    def close(self):
        self.equipment.close()


if __name__ == '__main__':
    fan = Fan("fan1", "open")
    lamp = Lamp("lamp1", "open")

    facade_equipment = FacadeEquipment(fan, lamp)
    fe = Facade(facade_equipment)
    fe.close()
    print(lamp.state)
    print(fan.state)

    print("2")
    facade_equipment2 = FacadeEquipment2(fan)
    fe2 = Facade(facade_equipment2)
    fe2.close()
    print(fan.state)
