def calc_nwd(x, y):
    while y > 0:
        modulo = x % y
        x = y
        y = modulo

    return x


print("Hello, I will compute Euklides")
value1 = int(input("Please give me fist number: "))
value2 = int(input("Please give me second number: "))

nwd = calc_nwd(value1, value2)

print(f"Computed value is {nwd}")
