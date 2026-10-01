n=int(input("Enter number :"))
arr=[]
for i in range(n):
    arr.append(int(input(f"Enter element : {i+1} : ")))
highest,lowest=0,99999
for i in range(n):
    if arr[i]>highest:
        highest=arr[i]
    if arr[i]<lowest:
        lowest=arr[i]
print("Highest : ",highest," ,Lowest : ",lowest)