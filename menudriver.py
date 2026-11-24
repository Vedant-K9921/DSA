def SumSeries(x):
    sum=0
    for i in range(1,21):
        if i%2!=0:
            sum+=x**i
        else:
            sum-=x**i
    return sum

def DisplaySeries():
    c=1
    for i in range(4):
        print(c,end=" ")
        c=(c*10)+1

S=SumSeries(2)
print(S)
D=DisplaySeries()
print(D)