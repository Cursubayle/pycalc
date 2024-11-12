from enum import Enum
import math
from my_sort import *
#from mainwindow import MainWindow
ops = ["+", "-", "*", "/"]
acts = ["AC", "C", "=","sqrt"]
digits = list("0123456789.")
brackets = ["(",")"]
#1233321123123132132
#from mainwindow import MainWindow
class State(Enum):
    CLEAR = 0
    DIGITS = 1
    OPS = 2
    BRACKETS = 3

class EventType(Enum):
    NUMBER = 0
    ACTS = 1
    OP = 2
    BRACKETS = 3


class MyCalc():
    def __init__(self):
        self.event_type = EventType.NUMBER
        self.current_line = ""
        self.input = []
        self.state = State.CLEAR
        self.stack = []
        self.history = None
        self.brcts = 0
        print (self.state)

    def clear(self):
        return
    def number(self):
        return
    def op(self):
        return






    digitsTable = ['acts','number','op']


    def do_event(self, value):
        print("history", self.history)
        self.history = None
        if Token(self.current_line + value):
            self.current_line += value
        else:
            self.stack.append(self.current_line)
            self.current_line = value

        print(self.current_line, self.stack)
        

     





    def send(self,s):
        return self.do_event(s)





