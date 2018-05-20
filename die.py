#_*_ coding: utf_8 _*_
from random import randint

class Die(object):
    """一个骰子类"""
    def __init__(self,num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        """返回 一个位于1和骰子面数之间的数"""
        return randint(1,self.num_sides)