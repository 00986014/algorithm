from collections import deque

class BST(object):
    def __init__(self):
        self.root = None
        self.count = 0

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def insert(self, key, value):
        self.root = self.__insert(self.root, key, value)

    def __insert(self, node, key, value):
        if not node:
            self.count += 1
            return Node(key, value)
        
        if key == node.key:
            node.value = value
        elif key<node.key:
            node.left = self.__insert(node.left, key, value)
        else:
            node.right = self.__insert(node.right, key, value)

        return node

    def contain(self, key):
        return self.__contain(self.root, key)

    def __contain(self, node, key):
        if not node:
            return False
        
        if key == node.key:
            return True
        elif key<node.key:
            return self.__contain(node.left, key)
        else:
            return self.__contain(node.right, key)

    def search(self, key):
        return self.__search(self.root, key)

    def __search(self, node, key):
        if not node:
            return None

        if key == node.key:
            return node.value
        elif key<node.key:
            return self.__search(node.left, key)
        else:
            return self.__search(node.right, key)

    def preOrder(self):
        return self.__preOrder(self.root)

    def __preOrder(self, node):
        if not node:
            return
        print node.key
        self.__preOrder(node.left)
        self.__preOrder(node.right)

    def inOrder(self):
        return self.__inOrder(self.root)

    def __inOrder(self, node):
        if not node:
            return
        self.__inOrder(node.left)
        print node.key
        self.__inOrder(node.right)

    def postOrder(self):
        return self.__postOrder(self.root)

    def __postOrder(self, node):
        if not node:
            return
        self.__postOrder(node.left)
        self.__postOrder(node.right)
        print node.key

    def levelOrder(self):
        q = deque()
        q.append(self.root)
        while q:
            node = q.popleft()
            print node.key
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def minimum(self):
        assert self.count != 0
        node = self.__minimum(self.root)
        return node.key

    def __minimum(self, node):
        if not node.left:
            return node
        return self.__minimum(node.left)

    def maximum(self):
        assert self.count != 0
        node = self.__maximum(self.root)
        return node.key

    def __maximum(self, node):
        if not node.right:
            return node
        return self.__maximum(node.right)

    def removeMin(self):
        if not self.root:
            return
        self.root = self.__removeMin(self.root)

    def __removeMin(self, node):
        if not node.left:
            rightnode = node.right
            del node
            self.count -= 1
            return rightnode
        node.left = self.__removeMin(node.left)
        return node

    def removeMax(self):
        if not self.root:
            return
        self.root = self.__removeMax(self.root)

    def __removeMax(self, node):
        if not node.right:
            leftnode = node.left
            del node
            self.count -= 1
            return leftnode
        node.right = self.__removeMax(node.right)
        return node

    def remove(self, key):
        return self.__remove(self.root, key)

    def __remove(self, node, key):
        if not node:
            return None

        if key<node.key:
            node.left = self.__remove(node.left, key)
            return node
        elif key>node.key:
            node.right = self.__remove(node.right, key)
            return node
        else:
            if not node.left:
                rightnode = node.right
                del node
                self.count -= 1
                return rightnode
            if not node.right:
                leftnode = node.left
                del node
                self.count -= 1
                return leftnode

            successor = self.__minimum(node.right)
            node.key, node.value = successor.key, successor.value
            node.right = self.__removeMin(node.right)
            
            del successor
            return node

    def floor(self, key):
        node = self.__floor(self.root, key)
        if node:
            return node.key

    def __floor(self, node, key):
        if not node:
            return None
        if node.key == key:
            return node
        if key < node.key:
            return self.__floor(node.left, key)
        t = self.__floor(node.right, key)
        if t: return t
        else: return node

    def ceiling(self, key):
        node = self.__ceiling(self.root, key)
        if node:
            return node.key

    def __ceiling(self, node, key):
        if not node:
            return None
        if node.key == key:
            return node
        if key > node.key:
            return self.__ceiling(node.right, key)
        t = self.__ceiling(node.left, key)
        if t: return t
        else: return node


class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


if __name__ == '__main__':
    b = BST()
    b.insert(41,'a')
    b.insert(22,'b')
    b.insert(58,'c')
    b.insert(15,'d')
    b.insert(33,'e')
    b.insert(50,'f')
    b.insert(13,'g')
    b.insert(37,'h')
    b.insert(42,'i')
    b.insert(53,'j')
    b.insert(60,'k')
    b.insert(59,'l')
    b.insert(63,'m')
