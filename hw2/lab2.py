
class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.val:
            root.left = self._insert(root.left, key)
        elif key > root.val:
            root.right = self._insert(root.right, key)
        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self._delete(root.left, key)
        elif key > root.val:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.val = self._min_value_node(root.right)
            root.right = self._delete(root.right, root.val)
        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.val

    def bfs(self):
        result = []
        if self.root is not None:
            queue = [self.root]
            while queue:
                node = queue.pop(0)
                result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result

    def inorder(self):
        return self._inorder(self.root, [])

    def _inorder(self, root, result):
        if root:
            result = self._inorder(root.left, result)
            result.append(root.val)
            result = self._inorder(root.right, result)
        return result

# ПРИМЕРЧЕК:
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("BFS обход(в ширину):", bst.bfs())
print("DFS обход(в глубину):", bst.inorder())

bst.delete(50)
print("BFS обход после удаления 50:", bst.bfs())