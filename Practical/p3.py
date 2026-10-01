n=int(input("Enter number :"))
arr=[]
for i in range(n):
    arr.append(int(input(f"Enter element : {i+1} : ")))
even,odd=0,0
for i in range(n):
    if arr[i]%2==0:
        even+=1
    elif arr[i]%2!=0:
        odd+=1
    else:
        print(" zero ")
print("Even : ",even," Odd : ",odd)