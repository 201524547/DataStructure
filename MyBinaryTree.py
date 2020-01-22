class MyNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def setRight(self, data):
        self.left = MyNode(data)

    def setRight(self, data):
        self.left = MyNode(data)

def Search(node, data):
    if node == None:
        return None
    if node.value == data:
        return node

    left_Node = Search(node.left, data)
    right_Node = Search(node.right, data)

    if left_Node == None:
        return right_Node
    else :
        return left_Node


class MyTree():
    def __init__(self):
        self.root = None

    def insert(self, node, left, right):
        ptr = self.root
        if self.root == None:
            self.root = MyNode(node)
            ptr = self.root
        else :
            ptr = Search(ptr,node)

        ptr.left = MyNode(left)
        ptr.right = MyNode(right)

    def Inorder(self,node):
        if node == None or node.value == ".":
            return ""
        msg = ""

        msg += self.Inorder(node.left)
        msg += node.value
        msg += self.Inorder(node.right)

        return msg

    def Preorder(self, node):
        if node == None or node.value == ".":
            return ""
        msg = ""

        msg += node.value
        msg += self.Preorder(node.left)
        msg += self.Preorder(node.right)

        return msg

    def Postorder(self, node):
        if node == None or node.value == ".":
            return ""
        msg = ""

        msg += self.Postorder(node.left)
        msg += self.Postorder(node.right)
        msg += node.value

        return msg

if __name__ == "__main__":
    n = int(input())

    t = MyTree()

    for i in range(n):
        temp = input()
        t.insert(temp[0],temp[2],temp[4])

    print(t.Preorder(t.root))
    print()
    print(t.Inorder(t.root))
    print()
    print(t.Postorder(t.root))
