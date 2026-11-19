class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None
class bst:
    def __init__(self):
        self.root=None
    def insert(self,new_node):
        if self.root is None:
            self.root=new_node
            return
        else:
            temp=self.root
            while True:
                if new_node.data<temp.data:
                    if temp.left is None:
                        temp.left=new_node
                        return
                    else:
                        temp=temp.left
                else:
                    if temp.right is None:
                        temp.right=new_node
                        return
                    else:
                        temp=temp.right
    def inorder(self):
        if self.root is None:
            return
        else:
            self.inorder(self.left)
            print(self.data,end=" ")
            self.inorder(self.right)

btree=bst()
btree.insert(Node(10))
btree.insert(Node(5))
btree.insert(Node(2))
btree.insert(Node(25))
btree.insert(Node(13))
btree.insert(Node(40))
