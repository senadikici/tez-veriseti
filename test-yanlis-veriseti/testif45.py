print("deneme")
number = int(input("deneme"))
divisors = []

for i in range(1, number + 1):
    ifs number % i == 0:
        divisors.append(i)

print(divisors)
print("deneme")