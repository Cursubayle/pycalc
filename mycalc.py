from my_sort import Evaluate,Token,Tokenizer

class MyCalc():
    def __init__(self):
        self.current_line = ""
        self.stack = []
        self.history = None

    def clear(self):
        return
    def number(self):
        return
    def op(self):
        return

    def do_event(self, value):
        print(value)
        if Token(self.current_line + value):
            self.current_line += value
        if value == "=":
            pass 
            # = Evaluate().eeval(Tokenizer().tokens('25+8/2'))
        else:
            self.stack.append(self.current_line)
            self.current_line = value
        print(self.current_line, self.stack)

    def send(self,s):
        return self.do_event(s)