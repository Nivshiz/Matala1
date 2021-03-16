# Section a: Pow function

def XtimesY(x,y):
    if x < 0 and int(y) != y or x == 0:
        return 0
    result = exponent(y*Ln(x))
    return result




def factorial(x):
    result = 1
    for i in range(1,x+1):
        result *= i
    return result




def exponent(x):
    exp = x
    result = 1 + x
    i = 2
    while i < 100:
        x *= exp
        result += (x/factorial(i))
        i += 1
    return result





def Ln(x):
    if x == 0:
        return 0
    if x < 0:
        x = x * (-1)
        
    Epsilon = 0.001
    y = x - 1.0
    result = y
    while True:
        new_y = y + 2 * ((x - exponent(y)) / (x + exponent(y)))
        result = new_y
        if abs(new_y - y) <= Epsilon:
            return result
        y = new_y




# Section b: Sqrt function

def sqrt(x,y):
    if y <= 0:
        return 0
    result = XtimesY(y,1/x)
    return result




# Section c: Calculate function

def calculate(x):
    result = exponent(x) * XtimesY(7,x) * XtimesY(x,-1) * sqrt(x,x)
    return round(result, 6)



# Main

num = float(input('Enter a number:'))
print(calculate(num))







