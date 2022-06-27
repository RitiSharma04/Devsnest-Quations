# n=int(input("enter the num:-"))
# x=0
# y=1
# z=0
# while z<=n:
#     print(z)
#     x=y
#     y=z
#     z=x+y


def solve(n):
    # CODE HERE
    a = 0
    b = 1
    if n == 0:
        return 0
       
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b