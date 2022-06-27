n=int(input())
a=[]
for i in range(0,n):
    b=input()
    a.append(b)
dic={}       
for j in a:
    count=0 
    for k in a:
        if j==k:
            count=count+1
    dic.update({j:count})           
print(dic) 
print(len(dic))
for k in dic:
    print(dic[k],end=" ")
print() 





## Enter your code here. Read input from STDIN. Print output to STDOUT
# n_ish = int(input())
# counter_dict = {}
# words_list = []

# word = input()
# words_list.append(word)
# if word in counter_dict:
#     counter_dict[word] += 1
# else:
#     counter_dict[word] = 1
    
# print(len(counter_dict))
# print(' '.join([str(counter_dict[word]) for word in counter_dict]))