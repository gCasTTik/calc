from sympy import *


def calculate(expression):
    try:
    
        x, y = symbols('x y')
        
     
        parsed_expression = parse_expr(expression)
        simplified_expression = simplify(parsed_expression)

      
        if 'x' in expression:
            simplified_expression = simplified_expression.subs(x, 1)
        if 'y' in expression:
            simplified_expression = simplified_expression.subs(y, 2)

       
        result = float(simplified_expression.evalf())
        return result
    except Exception as e:
        return f"Ошибка: {str(e)}"


expression = input("Введите математическое выражение: ")

result = calculate(expression)
print(f"Результат: {result}")