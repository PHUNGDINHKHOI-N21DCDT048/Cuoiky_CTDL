class ExpressionEvaluator:
    def precedence(self, op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        return 0
    
    def apply_op(self, a, b, op):
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
        if op == '/':
            if b == 0:
                raise ValueError("Division by zero")
            return a / b
        
    def evaluate_expression(self, expression):
        values = []
        ops = []
        i = 0
        while i < len(expression):
            if expression[i] == ' ':
                i += 1
                continue
            elif expression[i].isdigit():
                val = 0
                while (i < len(expression) and
                       expression[i].isdigit()):
                    val = (val * 10) + int(expression[i])
                    i += 1
                values.append(val)
            elif expression[i] == '(':
                ops.append(expression[i])
                i += 1
            elif expression[i] == ')':
                while len(ops) != 0 and ops[-1] != '(':
                    val2 = values.pop()
                    val1 = values.pop()
                    op = ops.pop()
                    values.append(self.apply_op(val1, val2, op))
                ops.pop()
                i += 1
            else:
                while (len(ops) != 0 and
                       self.precedence(ops[-1]) >= self.precedence(expression[i])):
                    val2 = values.pop()
                    val1 = values.pop()
                    op = ops.pop()
                    values.append(self.apply_op(val1, val2, op))
                ops.append(expression[i])
                i += 1
        while len(ops) != 0:
            val2 = values.pop()
            val1 = values.pop()
            op = ops.pop()
            values.append(self.apply_op(val1, val2, op))
        return values[-1]


expression = "3 + 4 * 2 - ( 1 + 2 )"
evaluator = ExpressionEvaluator()
result = evaluator.evaluate_expression(expression)
print("Giá trị của biểu thức là:", result)
