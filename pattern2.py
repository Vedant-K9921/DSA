n=int(input("Enter the number :"))
if n%2==0:
    n=n+1
mid=int(n/2)+1
print(mid)
for i in range(n):
    for j in range(n):
        if(j==mid or i==mid):
            print('*',end=' ')
        else:
            print(" ",end='')
    print()