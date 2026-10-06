n=int(input("Enter the number :"))
for i in range(n):
    for j in range(i):
        print(chr(65+j),end=" ")
    print()

num=0
for i in range(n):
    for j in range(i):
        print(chr(65+num),end=" ")
        num+=1;
    print()

for i in range(n):
    print(' '*(n-i+5),end=" ")
    for j in range(2*i+1):
        print(chr(65+j),end="")
    print()

for i in range(n):
    print(' '*(n-i+5),end=" ")
    for j in range(2*i+1):
        if j==0 or j==2*i or i==n-1:
            print(chr(65+j),end="")
        else:
            print(end=" ")
    print()
