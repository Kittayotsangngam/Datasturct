"""ให้น้องๆสร้าง AVL Tree ด้วย Class โดยผลลัพธ์ให้แสดงเป็น Tree ในแต่ละรอบหลังจาก Insert ให้ตรวจสอบว่า balance หรือยัง หากไม่ให้ ปรับ Balance ให้เรียบร้อยแล้วและแสดงผล

** ถ้าสงสัยสามารถดู visualization ของ AVL ได้ที่ website นี้ : https://www.cs.usfca.edu/~galles/visualization/AVLtree.html
"""
class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 0

    def __str__(self):
        return str(self.val)
  
class AVL_Tree(object):
    def __init__(self):
        self.root = None
    
    def rr(self,px):
        py = px.right
        px.right = py.left
        py.left = px
        return py
    
    def ll(self,px):
        py = px.left
        px.left = py.right
        py.right = px
        return py
    
    def changeHeight(self,a):
        if a!=None:
            a.height = max(self.changeHeight(a.left),self.changeHeight(a.right))+1
            return a.height
        else:
            return -1
    
    def insert(self,node,data):
        data = int(data)
        if self.root is None:
            self.root = TreeNode(data)
            return self.root
        else:
            if node != None:
                if data < node.val:
                    node.left = self.insert(node.left,data)
                else:
                    node.right = self.insert(node.right,data)
            else:
                return TreeNode(data)
            
            
            l = node.left.height if node.left is not None else -1
            r = node.right.height if node.right is not None else -1
            if abs(l-r)>1:
                a = self.root
                if l>r:
                    if data<node.left.val:
                        a = self.ll(node)
                        print('l')
                        print('Not Balance, Rebalance!')
                    else:
                        node.left = self.rr(node.left)
                        node = self.ll(node)
                        a = node
                        print('rl')
                        print('Not Balance, Rebalance!')
                else:
                    if data<node.right.val:
                        node.right = self.ll(node.right)
                        node = self.rr(node)
                        a = node
                        print('lr')
                        print('Not Balance, Rebalance!')
                    else:
                        print('r')
                        print('Not Balance, Rebalance!')
                        a = self.rr(node)
                self.changeHeight(a)
                return a
            else:
                node.height = max(l,r)+1
                return node
    

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)
  
myTree = AVL_Tree() 
root = None

data = input("Enter Input : ").split()
for e in data:
    print("insert :",e)
    root = myTree.insert(root, e)
    printTree90(root)
    print("===============")
"""Enter Input : 1 2 3 4 5 6 7 8
insert : 1
 1
===============
insert : 2
      2
 1
===============
insert : 3
Not Balance, Rebalance!
      3
 2
      1
===============
insert : 4
           4
      3
 2
      1
===============
insert : 5
Not Balance, Rebalance!
           5
      4
           3
 2
      1
===============
insert : 6
Not Balance, Rebalance!
           6
      5
 4
           3
      2
           1
===============
insert : 7
Not Balance, Rebalance!
           7
      6
           5
 4
           3
      2
           1
===============
insert : 8
                8
           7
      6
           5
 4
           3
      2
           1
===============
Enter Input : 50 40 35 30 20 10 5
insert : 50
 50
===============
insert : 40
 50
      40
===============
insert : 35
Not Balance, Rebalance!
      50
 40
      35
===============
insert : 30
      50
 40
      35
           30
===============
insert : 20
Not Balance, Rebalance!
      50
 40
           35
      30
           20
===============
insert : 10
Not Balance, Rebalance!
           50
      40
           35
 30
      20
           10
===============
insert : 5
Not Balance, Rebalance!
           50
      40
           35
 30
           20
      10
           5
==============="""


