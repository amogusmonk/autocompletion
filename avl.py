class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Height is initially 1 when the node is inserted

class AVLTree:
    def search(self,root, key): 
        key = key.lower()
        if root is None:  
            return None
        elif root.key == key: 
            return root
        elif key > root.key:  
            return self.search(root.right, key)
        else:  
            return self.search(root.left, key)
        
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = max(self.get_height(z.left), self.get_height(z.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        return y

    def left_rotate(self, z):
        y = z.right
        T3 = y.left
        y.left = z
        z.right = T3
        z.height = max(self.get_height(z.left), self.get_height(z.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        return y

    def insert(self, root, key):
        key = key.lower()

        if root is None:
            return Node(key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        elif key < root.key:
            root.left = self.insert(root.left, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right)) 
        balance = self.get_balance(root)

        if balance > 1:
            if key < root.left.key:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        elif balance < -1:
            if key < root.right.key:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
            else:
                return self.left_rotate(root)
        
        return root

    def prefix_search(self, root, prefix):
        #find first prefix match
        if root is None:
            return None
        prefix = prefix.lower()
        if root.key.startswith(prefix):
            return root
        if root.key > prefix:
            return self.prefix_search(root.left, prefix)
        else:
            return self.prefix_search(root.right, prefix)
    
    def word_collection(self, root, prefix) -> list:
        #use in-order traversal
        word_list = []
        if root is None:
            return []
        prefix = prefix.lower()
        if root.left:
            word_list.extend(self.word_collection(root.left, prefix))
        if root.key.startswith(prefix):
            word_list.append(root.key)
        if root.right:
            word_list.extend(self.word_collection(root.right, prefix))
        return word_list

    def autocomplete(self, root, prefix):
        prefix_node = self.prefix_search(root, prefix)
        if prefix_node is None:
            return []
        return self.word_collection(prefix_node, prefix)

