import sys
a=(1,4,5,3,[4,2,4,2])
print(sys.getsizeof(a))
a[-1].extend([x for x in range(10000000)] )
print(sys.getsizeof(a))