# def recursion_fibonacci(a):
#     if a == 0:
#         return 0
#     elif a == 1:
#         return 1
#     else:
#         return recursion_fibonacci(a - 1) + recursion_fibonacci(a - 2)
#
#
# fibonacci = [recursion_fibonacci(n) for n in range(20)]
# print(fibonacci)


f1 = f2 = 1
n = 6
print(f1, f2, end=' ')

for i in range(2, n):
    f1, f2 = f2, f1 + f2
    print(f2, end=' ')



