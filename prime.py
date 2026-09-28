a=int(input("Enter number :"))
flag=0
for i in range(2,(a//2)+1):
    if a%i==0:
        flag=1
        print("Not Prime")
        break
if flag==0:
    print("Prime")