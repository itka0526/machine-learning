def factorial (n, x = 1):
    if n == 0 or n < 0:
        return x 
    return factorial(n - 1, n * x)

def binomial_coefficient(n, k):
    return factorial(n)/(factorial(k)*factorial(n-k))

def pascal(n):
    space = " "
    for row in range(n):
        left_spaces = space * 5 * (n-row)
        print(left_spaces, end=space)
        for col in range(row+1):
            val = int(binomial_coefficient(row, col))
            print ( "{:^10s}".format(str(val)), end=space)
        print('') 
        
pascal(13)
