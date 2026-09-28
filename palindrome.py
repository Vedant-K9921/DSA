a=int(input("Enter Num:"))
s=a
sum=0
while a!=0:
    digit=a%10
    sum=(sum*10)+digit
    a=a//10
if s==sum:
    print("Palindrome")
else:
    print("Not")