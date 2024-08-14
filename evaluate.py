def postfix(val):
    ops = {'+':2, '-':2, '/':1, '*':1, '^':0}

    INPUT = val

    stack, OUTPUT, digit = [], [], False

    for s in INPUT:
        
        if s in '0123456789':
            if len(OUTPUT) == 0:
                OUTPUT = [s] + OUTPUT
            else:
                if OUTPUT[0][-1] in '0123456789' and digit: OUTPUT[0] += s
                else: OUTPUT = [s] + OUTPUT
            digit = True
        else: digit = False
        
        if s == '(':
            stack = [s] + stack
        
        if s == ')':
            while stack != [] and stack[0] != '(': OUTPUT, stack = [stack[0]] + OUTPUT, stack[1:]
            if stack != [] and stack[0] == '(': stack = stack[1:]
        
        if s in ops:
            while stack != [] and stack[0] in ops and ops[s] >= ops[stack[0]]: OUTPUT, stack = [stack[0]] + OUTPUT, stack[1:]
            stack = [s] + stack

    while stack != []: OUTPUT, stack = [stack[0]] + OUTPUT, stack[1:]

    #print('инфиксная запись:\t%s' % (INPUT))
    #print('постфиксная запись:\t%s' % ("".join(reversed(OUTPUT))))
    return "".join(reversed(OUTPUT))
                
print(postfix("5+5"))

# Python program to evaluate value of a postfix expression


# Class to convert the expression
class Evaluate:

	# Constructor to initialize the class variables
	def __init__(self, capacity):
		self.top = -1
		self.capacity = capacity
		
		# This array is used a stack
		self.array = []

	# Check if the stack is empty
	def isEmpty(self):
		return True if self.top == -1 else False

	# Return the value of the top of the stack
	def peek(self):
		return self.array[-1]

	# Pop the element from the stack
	def pop(self):
		if not self.isEmpty():
			self.top -= 1
			return self.array.pop()
		else:
			return "$"

	# Push the element to the stack
	def push(self, op):
		self.top += 1
		self.array.append(op)

	# The main function that converts given infix expression
	# to postfix expression
	def evaluatePostfix(self, exp):

		# Iterate over the expression for conversion
		for i in exp:

			# If the scanned character is an operand
			# (number here) push it to the stack
			if i.isdigit():
				self.push(i)

			# If the scanned character is an operator,
			# pop two elements from stack and apply it.
			else:
				val1 = self.pop()
				val2 = self.pop()
				self.push(str(eval(val2 + i + val1)))

		return int(self.pop())



# Driver code
if __name__ == '__main__':
	exp = postfix("5+5")
	obj = Evaluate(len(exp))
	
	# Function call
	print("postfix evaluation: %d" % (obj.evaluatePostfix(exp)))

	
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
