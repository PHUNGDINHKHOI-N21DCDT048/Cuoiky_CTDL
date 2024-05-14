class ExpressionConverter:
    def precedence(self, op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        return 0
    
    def to_postfix(self, expression):
        postfix = []
        ops = []
        i = 0
        while i < len(expression):
            if expression[i] == ' ':
                i += 1
                continue
            elif expression[i].isdigit():
                val = ''
                while (i < len(expression) and
                       (expression[i].isdigit() or expression[i] == '.')):
                    val += expression[i]
                    i += 1
                postfix.append(val)
            elif expression[i] == '(':
                ops.append(expression[i])
                i += 1
            elif expression[i] == ')':
                while len(ops) != 0 and ops[-1] != '(':
                    postfix.append(ops.pop())
                ops.pop()
                i += 1
            else:
                while (len(ops) != 0 and
                       self.precedence(ops[-1]) >= self.precedence(expression[i])):
                    postfix.append(ops.pop())
                ops.append(expression[i])
                i += 1
        while len(ops) != 0:
            postfix.append(ops.pop())
        return ' '.join(postfix)

expression = "2 + 3 * 5"
converter = ExpressionConverter()
postfix = converter.to_postfix(expression)
print("Biểu thức hậu tố là:", postfix)
