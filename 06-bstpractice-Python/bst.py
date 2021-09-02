class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        # Your code goes here
        newnode = Node(new_val)
        current = self.root
        while current:
            prev = current
            if (new_val < current.value):
                current = current.left
            else:
                current = current.right
        if (prev == None):
            prev = newnode
        elif new_val < prev.value:
            prev.left = newnode
        else:
            prev.right = newnode

    def printSelf(self):
        # Your code goes here
        pass
        
    def search(self, find_val):
        # Your code goes here
        root = self.root
        while root:
            if type(find_val)!=type(root.value):
                return False
            if find_val > root.value:
                root = root.right    
            elif find_val < root.value:
                root = root.left
            else:
                return True
        return False