# Collatz Conjecture
# Start with a number n > 1. Find the number of steps it takes to reach one using the following process: If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.

def collatz_conjecture(num, count):
    if num <= 1:
        return count
    if num % 2 == 0:
        return collatz_conjecture(num/2, count+1)
    else:
        return collatz_conjecture(num*3+1, count+1)
    


n = int(input('Input number: '))
print(collatz_conjecture(n, 0))