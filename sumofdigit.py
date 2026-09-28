a=int(input("Enter Num:"))
sum=0
while a!=0:
    digit=a%10
    sum+=digit
    a=a//10
print("Sum = ",sum)
