def is_prime(sum_th):
    def wrapper(*args):
        sum = sum_th (*args)
        a = (True for i in range (2, sum // 2) if sum % i == 0)
        for el in a:
            if el == True:
                print (f'Составное')
                return sum
        print (f'Простое')
        return sum
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three (12, 567, 9)
print (result)
result = sum_three (5, 0, 6)
print (result)
result = sum_three (1453, 317, 613)
print (result)
result = sum_three (1453, 317, 612)
print (result)