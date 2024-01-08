import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}
equation = {
    'num1': 0,
    'operator': '',
    'num2': 0,
    'result': 0,
}
should_continue = True

equation['num1'] = float(input("What's your first number? "))

def get_equation():
    equation['operator'] = input("Pick an operation (+ - * /): ")
    equation['num2'] = float(input("What's your next number? "))
    
def display_result():
    equation['result'] = ops[equation['operator']](equation['num1'], equation['num2'])
    print(f'{equation["num1"]} {equation["operator"]} {equation["num2"]} = {equation['result']}')

while should_continue:
    get_equation()
    display_result()
    
    continue_calc = input(f'Do you want to perform another calculation on {equation['result']}? y = yes, n = no: ')
    
    if continue_calc == 'y':
        equation['num1'] = equation['result']
    else:
        should_continue = False
    