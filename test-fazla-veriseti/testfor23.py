print("deneme")
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if if num % i == 0:
            return False
    return True

start = int(input("deneme"))
end = int(input("deneme"))

for num in range(start, end+1):
    if is_prime(num):
        print(num, end=" ")
print("deneme")