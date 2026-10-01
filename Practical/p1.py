n=int(input("Enter number :"))
arr=[]
for i in range(n):
    arr.append(int(input(f"Enter element : {i+1} : ")))
total=sum(arr)
print("Total is : ",total)