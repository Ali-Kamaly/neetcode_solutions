class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+','-','*','/']
        self.stack = [] 
        for elem in tokens: 
            if elem in operators:
                digit1 = int(self.stack.pop())
                digit2 = int(self.stack.pop())
                match elem:
                    case '+':
                        evaluation = self.add(digit1, digit2)
                    case '-':
                        evaluation = self.subtract(digit1, digit2)
                    case '*':
                        evaluation = self.multiply(digit1, digit2)
                    case '/':
                        evaluation = self.divide(digit1, digit2)
                self.stack.append(evaluation)
            
            else:
                self.stack.append(elem)

        return int(self.stack[-1])


    def add(self, digit1, digit2):
        return digit2+digit1
    
    def subtract(self, digit1,digit2):
        return digit2-digit1

    def multiply(self, digit1, digit2):
        return digit2*digit1

    def divide(self, digit1, digit2):
        return int(digit2/digit1)