
# def solve(n,arr):
#     b=sorted(arr)
#     c=[]
#     for i in b:
#         if i not in c:        
#               c.append(i)                
#     return c[-2]    
# arr=[2,1,-1,2,-4,8,7,8,-17]  
# n=len(arr)  
# print(solve(n,arr))


# def solve(n,arr):
#     b=sorted(arr)
#     c=[]
#     for i in b:
#         if i not in c:        
#               c.append(i)                
#     return c[-2]       
def solve(n,arr):
    arr1=list(set(arr))
    arr1.sort()
    return arr1[-2]