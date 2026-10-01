n=int(input("Enter number :"))
arr=[]
ar2=[]
for i in range(n):
    arr.append(int(input(f"Enter element : {i+1} : ")))
for i in reversed(range(n)):
    ar2.append(arr[i])
print(ar2)