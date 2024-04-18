class Node:
    """
    this class represents in a binary search tree which stores a post
    and its datetime
    """
    def __init__(self, datetime, post):
        self.datetime = datetime
        self.post = post
        self.left = None
        self.right = None

class BST:
    """
    This class represents a binary search tree to manage social media posts
    by datetime
    """
    def __init__(self):
        self.root = None

    def insert(self, datetime, post):
        #instering a new post into the BTS based on the date time
        if self.root is None:
            self.root = Node(datetime, post)
        else:
            self._insert_recursive(self.root, datetime, post)

    def _insert_recursive(self, current, datetime,post):
        if datetime < current.datetime:
            if current.left is None:
                current.left = Node(datetime, post)
            else:
                self._insert_recursive(current.left, datetime, post)
        elif datetime > current.datetime:
            if current.right is None:
                current.right = Node(datetime, post)
            else:
                self._insert_recursive(current.right, datetime, post)
        else:
            raise ValueError("A post with the same datetime already exists.")

    def find(self, datetime):
        """this class finds and returns a post by its datetime."""
        return self._find_recursive(self.root, datetime)

    def _find_recursive(self, current, datetime):
        if current is None:
            return None
        elif datetime == current.datetime:
            return current.post
        elif datetime < current.datetime:
            return self._find_recursive(current.left, datetime)
        else:
            return self._find_recursive(current.right, datetime)

    def _in_order_traversal_recursive(self, node, result):
        """A helper method for in-order traversal that adds node values to the result list."""
        if node is not None:
            self._in_order_traversal_recursive(node.left, result)
            result.append(node.post)
            self._in_order_traversal_recursive(node.right, result)

    def in_order_traversal(self):
        """this function helps to output the content of the tree for debugging."""
        result = []
        self._in_order_traversal_recursive(self.root, result)
        return result


bst = BST()
bst.insert('2021-04-01T12:00:00', 'Hello World!')
bst.insert('2021-04-01T12:05:00', 'Another post')
bst.insert('2021-04-01T12:10:00', 'More content here')

# Find a post
print(bst.find('2021-04-01T12:05:00'))
print(bst.in_order_traversal())
