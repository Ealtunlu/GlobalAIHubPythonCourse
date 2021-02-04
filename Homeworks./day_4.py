#Finding prime numbers between 0 and 100 using functions
def is_pirme(n):
    if n == 0 or n == 1:
         return False
    for x in range(2, n):
        if n % x == 0 :
            return False
    return True
prime_nums = [x for x in range(0,100) if is_pirme(x)]
print(f"Prime Numbers : {prime_nums}")