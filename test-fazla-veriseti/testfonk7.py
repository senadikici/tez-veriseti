print("deneme")
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if if num % i == 0:
            return False
    return True

result = is_prime(17)
print(result)
print("deneme")