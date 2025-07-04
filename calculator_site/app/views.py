# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import View

# class Calculator(View):
#     def get (self, request):
#      return HttpResponse("Hello! Welcome to the Calculator class-based view.")
# Create your views here.
# your_app/views.py
# from django.views import View
# from django.shortcuts import render, redirect
# from django.http import HttpResponse

# class Calculator(View):
#     template_name = 'calculator.html'

#     def get(self, request, *args, **kwargs):
#         context = {
#                 'result': ""
#             }
#         return render(request, self.template_name, context)

#     def post(self, request, *args, **kwargs):
#         expression = request.POST.get('my_post_param')

#         try:
#             result = eval(expression)  
#             context = {
#                 # 'expression': expression,
#                 'result': result
#             }
#         except Exception as e: 
#             context = {
#                 # 'expression': expression,
#                 'result': 'Invalid expression'
#             }

#         return render(request, self.template_name, context)

# class SuccessView(View):
#     def get(self, request):
#         return HttpResponse("Success!")

# import math
# from django.views import View
# from django.shortcuts import render

# class Mathematics:
#     def addition(self, a, b): return a + b
#     def subtraction(self, a, b): return a - b
#     def multiplication(self, a, b): return a * b
#     def division(self, a, b): return a / b
#     def power(self, a, b): return math.pow(a, b)
#     def sin(self, a): return math.sin(math.radians(a))
#     def cos(self, a): return math.cos(math.radians(a))
#     def tan(self, a): return math.tan(math.radians(a))
#     def sqrt(self, a): return math.sqrt(a)
#     def log(self, a): return math.log10(a)
#     def sinh(self, a): return math.sinh(a)
#     def cosh(self, a): return math.cosh(a)
#     def tanh(self, a): return math.tanh(a)

# class Evaluation:
#     def __init__(self):
#         self.math = Mathematics()

#     def evaluate(self, a, b, op):
#         if op == '+': return self.math.addition(a, b)
#         elif op == '-': return self.math.subtraction(a, b)
#         elif op == '*': return self.math.multiplication(a, b)
#         elif op == '/': return self.math.division(a, b)
#         elif op == '^': return self.math.power(a, b)

# class BODMAS:
#     def __init__(self):
#         self.eval = Evaluation()

#     def calculate(self, expression):
#         print("Evaluating expression:", expression) 
#         expression = expression.replace(" ", "")
#         if any(func in expression for func in ['sin', 'cos', 'tan', 'sinh', 'cosh', 'tanh', 'sqrt', 'log']):
#          expression = self.handle_functions(expression)


#         while "(" in expression:
#             open_idx = expression.rfind("(")
#             close_idx = expression.find(")", open_idx)
#             inner = expression[open_idx + 1:close_idx]
#             result = self.calculate(inner)
#             expression = expression[:open_idx] + str(result) + expression[close_idx + 1:]

#         expression = self.evaluate_operations(expression, "^")
#         expression = self.evaluate_operations(expression, "*/")
#         expression = self.evaluate_operations(expression, "+-")
#         return float(expression)

#     def evaluate_operations(self, expr, operators):
#         i = 0
#         while i < len(expr):
#             if expr[i] in operators:
#                 op = expr[i]
#                 left_start = i - 1

#                 while left_start >= 0 and (expr[left_start].isdigit() or expr[left_start] == '.'):
#                     left_start -= 1
#                 left = expr[left_start + 1:i]
#                 right_end = i + 1

#                 while right_end < len(expr) and (expr[right_end].isdigit() or expr[right_end] == '.'):
#                     right_end += 1
#                 right = expr[i + 1:right_end]

#                 result = self.eval.evaluate(float(left), float(right), op)
#                 expr = expr[:left_start + 1] + str(result) + expr[right_end:]
#                 i = left_start + len(str(result))
#             else:
#                 i += 1
#         return expr

#     def handle_functions(self, expr):
#         math_obj = self.eval.math
#         i = 0
#         while i < len(expr):
#             if expr[i:i+4] == 'sqrt':
#                 func = 'sqrt'
#                 j = i + 4
#             elif expr[i:i+4] in ['sinh', 'cosh', 'tanh']:
#                 func = expr[i:i+4]
#                 j = i + 4
#             elif expr[i:i+3] in ['sin', 'cos', 'tan', 'log']:
#                 func = expr[i:i+3]
#                 j = i + 3
#             else:
#                 i += 1
#                 continue
#             try:
#                 if j < len(expr) and expr[j] == '(':
#                     j += 1
#                     start = j
#                     bracket_count = 1
#                     while j < len(expr) and bracket_count > 0:
#                         if expr[j] == '(':
#                             bracket_count += 1
#                         elif expr[j] == ')':
#                             bracket_count -= 1
#                         j += 1
#                     if bracket_count != 0:
#                         raise ValueError("Mismatched parentheses.")
#                     value_str = expr[start:j-1]
#                     value = float(self.calculate(value_str))
#                 else:
#                     start = j
#                     while j < len(expr) and (expr[j].isdigit() or expr[j] == '.'):
#                         j += 1
#                     value = float(expr[start:j])
#             except Exception as e:
#                 raise ValueError(f"Invalid {func}() expression: {e}")
#             if func == 'sinh':
#               result = math_obj.sinh(value)
#             elif func == 'cosh':
#               result = math_obj.cosh(value)
#             elif func == 'tanh':
#               result = math_obj.tanh(value)
#             elif func == 'sin':
#                 result = math_obj.sin(value)
#             elif func == 'cos':
#                 result = math_obj.cos(value)
#             elif func == 'tan':
#                 result = math_obj.tan(value)
#             elif func == 'sqrt':
#                 result = math_obj.sqrt(value)
#             elif func == 'log':
#                 if value <= 0:
#                     raise ValueError("Log domain error.")
#                 result = math_obj.log(value)
        
#             expr = expr[:i] + str(result) + expr[j:]
#             i = i + len(str(result))
#         return expr


# class CalculatorView(View):
#     template_name = 'calculator.html'

#     def get(self, request):
#         return render(request, self.template_name, {'result': ''})

#     def post(self, request):
#         expression = request.POST.get('my_post_param')
#         result = ''
#         try:
#             bodmas = BODMAS()
#             result = bodmas.calculate(expression)
#         except Exception:
#             result = 'Error'
#         return render(request, self.template_name, {'result': result})
import math
from django.views import View
from django.shortcuts import render

class Mathematics:
    def addition(self, a, b): return a + b
    def subtraction(self, a, b): return a - b
    def multiplication(self, a, b): return a * b
    def division(self, a, b): return a / b
    def power(self, a, b): return math.pow(a, b)

    def sin(self, a): return math.sin(math.radians(a))
    def cos(self, a): return math.cos(math.radians(a))
    def tan(self, a): return math.tan(math.radians(a))
    def sqrt(self, a): return math.sqrt(a)
    def log(self, a): return math.log10(a)
    def sinh(self, a): return math.sinh(math.radians(a))
    def cosh(self, a): return math.cosh(math.radians(a))
    def tanh(self, a): return math.tanh(math.radians(a))

class Evaluation:
    def __init__(self):
        self.math = Mathematics()

    def evaluate(self, a, b, op):
        if op == '+': return self.math.addition(a, b)
        elif op == '-': return self.math.subtraction(a, b)
        elif op == '*': return self.math.multiplication(a, b)
        elif op == '/': return self.math.division(a, b)
        elif op == '^': return self.math.power(a, b)

class BODMAS:
    def __init__(self):
        self.eval = Evaluation()

    def calculate(self, expression):
        print("Evaluating expression:", expression)  
        expression = expression.replace(" ", "")

        if any(func in expression for func in ['sin', 'cos', 'tan', 'sinh', 'cosh', 'tanh', 'sqrt', 'log']):
            expression = self.handle_functions(expression)

        while "(" in expression:
            open_idx = expression.rfind("(")
            close_idx = expression.find(")", open_idx)
            inner = expression[open_idx + 1:close_idx]
            result = self.calculate(inner)
            expression = expression[:open_idx] + str(result) + expression[close_idx + 1:]

        expression = self.evaluate_operations(expression, "^")
        expression = self.evaluate_operations(expression, "*/")
        expression = self.evaluate_operations(expression, "+-")
        return float(expression)

    def evaluate_operations(self, expr, operators):
        i = 0
        while i < len(expr):
            if expr[i] in operators:
                op = expr[i]
                left_start = i - 1
                while left_start >= 0 and (expr[left_start].isdigit() or expr[left_start] == '.'):
                    left_start -= 1
                left = expr[left_start + 1:i]

                right_end = i + 1
                while right_end < len(expr) and (expr[right_end].isdigit() or expr[right_end] == '.'):
                    right_end += 1
                right = expr[i + 1:right_end]

                result = self.eval.evaluate(float(left), float(right), op)
                expr = expr[:left_start + 1] + str(result) + expr[right_end:]
                i = left_start + len(str(result))
            else:
                i += 1
        return expr

    def handle_functions(self, expr):
        math_obj = self.eval.math
        i = 0
        while i < len(expr):
            if expr[i:i+4] == 'sqrt':
                func = 'sqrt'
                j = i + 4
            elif expr[i:i+4] in ['sinh', 'cosh', 'tanh']:
                func = expr[i:i+4]
                j = i + 4
            elif expr[i:i+3] in ['sin', 'cos', 'tan', 'log']:
                func = expr[i:i+3]
                j = i + 3
            else:
                i += 1
                continue

            try:
                if j < len(expr) and expr[j] == '(':
                    j += 1
                    start = j
                    bracket_count = 1
                    while j < len(expr) and bracket_count > 0:
                        if expr[j] == '(':
                            bracket_count += 1
                        elif expr[j] == ')':
                            bracket_count -= 1
                        j += 1
                    if bracket_count != 0:
                        raise ValueError("Mismatched parentheses.")

                    value_str = expr[start:j - 1]

            
                    if expr[i:].split('(')[0] == func:
                        value = float(self.calculate(value_str))
                    else:
                        raise ValueError(f"Function name mismatch: expected {func}")
                else:
                    start = j
                    while j < len(expr) and (expr[j].isdigit() or expr[j] == '.'):
                        j += 1
                    value = float(expr[start:j])

                if func == 'sinh':
                    result = math_obj.sinh(value)
                elif func == 'cosh':
                    result = math_obj.cosh(value)
                elif func == 'tanh':
                    result = math_obj.tanh(value)
                elif func == 'sin':
                    result = math_obj.sin(value)
                elif func == 'cos':
                    result = math_obj.cos(value)
                elif func == 'tan':
                    result = math_obj.tan(value)
                elif func == 'sqrt':
                    result = math_obj.sqrt(value)
                elif func == 'log':
                    if value <= 0:
                        raise ValueError("Log domain error.")
                    result = math_obj.log(value)

                expr = expr[:i] + str(result) + expr[j:]
                i = i + len(str(result))
            except Exception as e:
                raise ValueError(f"Invalid {func}() expression: {e}")

        return expr


class CalculatorView(View):
    template_name = 'calculator.html'

    def get(self, request):
        return render(request, self.template_name, {'result': ''})

    def post(self, request):
        expression = request.POST.get('my_post_param')
        result = ''
        try:
            bodmas = BODMAS()
            result = bodmas.calculate(expression)
        except Exception:
            result = 'Error'
        return render(request, self.template_name, {'result': result})







