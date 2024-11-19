from calculation import Evaluate,Token

class MyCalc():
    def __init__(self):
        self.current_line = ""
        self.stack = []

    def do_event(self, value):
        print(value)
        if Token(self.current_line + value):
            self.current_line += value
        elif value == "=":
            self.stack.append(self.current_line)
            result = ''.join(self.stack)
            print(result)
            self.current_line = str(Evaluate(result).eeval())
        else:
            self.stack.append(self.current_line)
            self.current_line = value
        print(self.current_line, self.stack)

    def send(self,s):
        return self.do_event(s)
