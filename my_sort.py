#!/usr/bin/env python3 

import re
from enum import Enum

class TOKEN_TYPE(Enum):
    """
    Класс типа токена.
    """
    NUMBER = 0
    OPERATOR = 1
    BRACKET = 2


class Token():
    """
    Класс для токена.
    Атрибуты
    --------
    data : str
    type : TOKEN_TYPE
    """
    
    operators = {'+':1,'-':1,'*':2,'/':2}

    def __new__(self, data):
        """
        Создаёт новый экземпляр класса из строки.
        """
        rc = super(Token, self).__new__(self)
        rc.data = data
        rc.type = None
        if rc.is_token(data):
            return rc
            # if rc.type == TOKEN_TYPE.OPERATOR
            #     rc.data = operators   
            # return rc
        return None

    def __repr__(self):
        return(f"('{self.data}', {self.type})")

    def is_number(self, n: str) -> bool:
        return re.match(r'^-?\d+\.?\d*$', n)

    def is_token(self, pattern: str) -> bool:
        """ Это токен или нет """
        if len(pattern) == 0:
            return True
        t_list=['+', '-', '*', '/', '**' ]
        if pattern in ['(',')']:
            self.type = TOKEN_TYPE.BRACKET
            return True
        if pattern in t_list:
        #if pattern in [ z.data for z in t_list ]:
            self.type = TOKEN_TYPE.OPERATOR
            return True
        if self.is_number(pattern):
            self.type = TOKEN_TYPE.NUMBER
            return True
        return False


class MyEval():
    def __init__(self, s=None):
        self.last_token = None
        self.compiled = None
        if s is not None:
            self.compiled = self.tokens(s)

    def __repr__(self):
        return(f"self.compiled = {self.compiled}")

    def tokens(self, s:str) -> list:
        """разбираем строку на токены"""
        ls = list()
        start_pos = 0
        end_pos = 0
        while end_pos < len(s):
            while token := Token(s[start_pos:end_pos]):
                self.last_token = token
                end_pos +=1
                if end_pos > len(s):
                    break
            end_pos -= 1
            ls.append(self.last_token)
            start_pos = end_pos
        return ls

class Sortir():
    """
    Класс для сортировки токена
    Атрибуты
    --------
    stack - стэк
    output - вывод
    """
    def __init__(self):
        self.stack = []
        self.output = []
    def sort(self, s:list):
        """
        Получаем список элементов типа ('(',TOKEN_TYPE.BRACKET)
        Преобразуем в постфиксную запись
        """
        for i in s:
            if i.type == TOKEN_TYPE.NUMBER:
                self.output.append(i)
                # если токен число, заносим его в вывод
                print('добавляем в вывод', i.data)
            if i.type == TOKEN_TYPE.OPERATOR:
                try:
                    while Token.operators[i.data] <= Token.operators[self.stack[-1]]:
                         # Если токен на вершине стека по приоритету выше или равен токену, то перекладываем оператор на вершине стека в вывод
                        self.output.append(self.stack.pop())
                    print('aaaaa')
                except IndexError:
                    print('stek pustoi')
                except KeyError:
                    print('v steke ne operazia')
                # в ином случае добавляем его в стек
                self.stack.append(i)
            if i.type == TOKEN_TYPE.BRACKET:
                # если токен открывающая скобка, то положить ее в стек
                if i.data == "(":
                    self.stack.append(i)
                if i.data == ")":
                    # если токен закрывающая скобка, то пока токен на вершине стека не открывающая скобка переложить оператор из стека в выходную очередь
                    try:
                        while self.stack[-1].data != "(":
                            # print(self.stack[-1])
                            print('bbbbbbbbbbbbbbb',self.stack[-1],self.stack)
                            self.output.append(self.stack.pop())
                        if self.stack[0].data == "(":
                            self.stack.pop(0)
                    except IndexError:
                        continue
        while len(self.stack) >= 0:
            try:
                self.output.append(self.stack.pop())
            except IndexError:
                break
        
        a = []
        for i in self.output:
            a.append(i.data)
        print(a,self.output)
        return self.output

    # def Evaluate(self,value):
    #     """" вычисляем """
    #     def 
    #     ops = {"+":addition}
    #     stack = []
    #     for i in value:
    #         if i.type == TOKEN_TYPE.NUMBER:
    #             stack.append(i.data)
    #         if i.type == TOKEN_TYPE.OPERATOR:
    #             result = stack.pop(-2) + i.data + stack.pop(-1)
    #             stack.append(str(eval(result)))
    #     return stack

class Evaluate():
    
    

    def __init__(self):
        pass
    
    def addition(self,value1, value2):
        return float(value1) + float(value2)
    
    def subtraction(self,value1, value2):
        return float(value1) - float(value2)
    
    def multiplication(self,value1, value2):
        return float(value1) * float(value2)
    
    def division(self,value1, value2):
        return float(value1) / float(value2)

    ops = {"+":addition,"-":subtraction,"*":multiplication,"/":division}

    def Evaluate(self, expression):
        stack = []
        for i in expression:
            if i.type == TOKEN_TYPE.NUMBER:
                stack.append(i.data)
            if i.type == TOKEN_TYPE.OPERATOR:
                result = self.ops[i.data](self,stack.pop(-2),stack.pop(-1))
                stack.append(result)
            print(stack,"aboba")


if __name__== "__main__":
    j = MyEval('(25+5)*3')
    print(j.tokens)
    
    # j = MyEval()
    # # print(j)
    # g = Token('531').is_token('531')
    # print(Token('123+'))
    # print(g)
    # t = j.tokens('(25+5)*3')
    # # print(t[0])
    # k = Sortir()
    # # k.sort(t)
    # u = Evaluate()
    # u.Evaluate(k.sort(t))

    