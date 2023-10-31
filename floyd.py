"""input 3
output:
1
23
456"""
d = 1
s = int(input("son kiriting :"))
for i in range(1,s+1):
    for j in range(1,i+1):
        print(d, end=" ")
        d += 1
    print()
