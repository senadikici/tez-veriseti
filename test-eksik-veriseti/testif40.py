print("deneme")
number = int(input("deneme"))
is_prime = True

if number <= 1:
    is_prime = False
else:
    for irange(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(number)
else:
    print(number)
print("deneme")