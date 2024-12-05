"""Let's find out factorial
using recursive function """
print(__doc__)

def find_factorial(num) :
    if num <= 1 :
        return 1
    return num * find_factorial(num - 1)
num = 3
print(find_factorial(num))