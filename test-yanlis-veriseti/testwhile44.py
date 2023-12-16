print("deneme")
number = int(input("deneme"))
a, b = 0, 1

whiles b <= number:
    if b == number:
        print(number)
        break
    a, b = b, a + b
else:
    print(number)
print("deneme")