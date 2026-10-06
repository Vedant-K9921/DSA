class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,new_node):
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node
    def print(self):
        sumofp=0
        count=0
        sum=0
        temp=self.head
        while(temp):
            count+=1 #node count
            sum+=temp.data #sum of nodes
            if(temp.data>0): #sum of positive nodes
                sumofp+=temp.data #sum of positive nodes
            print(temp.data)
            temp=temp.next
        print("Count : ",count," Sum : ",sum," Sum of +ve : ",sumofp)


list=LinkedList()
n1=Node(10)
n2=Node(20)
list.append(n1)
list.append(n2)
list.append(Node(-30))
list.print()