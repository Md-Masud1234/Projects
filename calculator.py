def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2
    
def mul(n1,n2):
    return n1 * n2
    
def div(n1,n2):
    return n1 / n2
    
operation = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

num1 = float(input("what is the first number?: "))
for symbol in operation:
    print(symbol)
operation_symbol = input("Pick an operation")
num2 = float(input("what is the next number?: "))
print(operation[operation_symbol](num1,num2))
