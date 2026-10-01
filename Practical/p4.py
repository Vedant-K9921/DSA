n=int(input("Enter number :"))
arr=[]
for i in range(n):
    arr.append(int(input(f"Enter element : {i+1} : ")))
m=int(input("Enter number to search :"))
for i in range(n):
    if arr[i]==m:
        print("The index is ",i)