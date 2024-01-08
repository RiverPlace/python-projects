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

def calculator():  
    equation['num1'] = float(input("What's your first number? "))    
    
    should_continue = True
    while should_continue:
        equation['operator'] = input("Pick an operation (+ - * /): ")
        equation['num2'] = float(input("What's your next number? "))
        equation['result'] = ops[equation['operator']](equation['num1'], equation['num2'])
        
        print(f'{equation["num1"]} {equation["operator"]} {equation["num2"]} = {equation['result']}')
        
        continue_calc = input(f'Do you want to perform another calculation on {equation['result']}? y = yes, n = no: ')
        
        if continue_calc == 'y':
            equation['num1'] = equation['result']
        else:
            should_continue = False
            calculator()

calculator()