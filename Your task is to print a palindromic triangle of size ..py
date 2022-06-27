# n=int(input("enter the num;-"))
# for i in range(1,n+1):
#     print (((10**i - 1)//9)**2)

# def solve(n):
#     # CODE HERE
#     for i in range(1,n+1):
#         print (((10**i - 1)//9)**2  )
# solve(n=int(input("enter the num;=")))        


def solve(n):
    # CODE HERE
    ls=[]
    for i in range(1,n+1):
        c=(((10**i)-1)//9)**2
        ls.append(c)
    return ls  