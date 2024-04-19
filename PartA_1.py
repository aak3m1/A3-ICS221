class Node:
    """
    this class represents in a binary search tree which stores a post
    and its datetime
    """
    def __init__(self, datetime, post):
        self.datetime = datetime #storing the datetime asoociated with the post
        self.post = post #stores the content of the soical media
        self.left = None #left child of the node to none
        self.right = None #right child of the node to none

class BST:
    """
    binary search tree to manage social media posts
    by datetime
    """
    def __init__(self):
        self.root = None #starting with an empty tree (no root node)

    def insert(self, datetime, post):
        #instering a new post into the BTS based on the date time
        if self.root is None:
            self.root = Node(datetime, post)#if the tree is empty then set a nre node as the root
        else:
            self._insert_recursive(self.root, datetime, post) #otherwise, call the recursice insert function

    def _insert_recursive(self, current, datetime,post):
        #private method to recursively find the correct possition for a new node
        if datetime < current.datetime:
            if current.left is None:
                current.left = Node(datetime, post)#inserting a new node to the left if spot is empty
            else:
                self._insert_recursive(current.left, datetime, post) #recurce to the left
        elif datetime > current.datetime:
            if current.right is None:
                current.right = Node(datetime, post)#inserting a new node to the right if spot is empty
            else:
                self._insert_recursive(current.right, datetime, post) #recurse to the right.
        else:
            raise ValueError("A post with the same datetime already exists.")#handels the duplicates datetime values

    def find(self, datetime):
        """this method finds and returns a post by its datetime."""
        return self._find_recursive(self.root, datetime)

    def _find_recursive(self, current, datetime):
        #this method to recursively search for a node by datetime
        if current is None:
            return None #returining none iif node not found (base case)
        elif datetime == current.datetime:
            return current.post #returnin the post if datetime matches
        elif datetime < current.datetime:
            return self._find_recursive(current.left, datetime) #recurscing left if searching datetime is less
        else:
            return self._find_recursive(current.right, datetime) #recurscing right if searching datetime is greater

    def traversal_recursive(self, node, result):
        """helper method for in-order traversal that adds node values to the result list."""
        if node is not None:
            self.traversal_recursive(node.left, result) #traverse left subtree
            result.append(node.post) #visit node and append post content to result
            self.traversal_recursive(node.right, result) #traverse right subrtee

    def order_traversal(self):
        """this function helps to output the content of the tree for debugging."""
        result = [] #list to hold the results of the traversal
        self.traversal_recursive(self.root, result) #start the recursive traversal from the root
        return result

#this example is to test the BST
bst = BST()
bst.insert('2024-04-03T12:00:00', 'Cats and Dogs')
bst.insert('2024-04-20T12:30:00', 'New country is visited !')
bst.insert('2023-12-18T13:00:00', 'Say Hi to my new puppy:)')

#displaying the posts in chronological order with clear statement of each post's position
print("All posts in chronological order:") #the content of the post
posts = bst.order_traversal()
for index, post in enumerate(posts, start=1):
    print(f"Post {index}: {post}")


print("")
#finding a post
print("Found post:", bst.find('2024-04-03T12:00:00'))


print("")
# Test case 1 where the Empty Tree Test
print("Test case 1: Empty Tree Test")
empty_bst = BST()
assert empty_bst.find('2024-01-01T00:00:00') is None, "Test Failed: Should return None for empty tree"
print("Passed: No post found in an empty tree.")

print("")
# Test case 2 Single Node Test
print("Test case 2: Single Node Test")
assert bst.find('2024-04-03T12:00:00') == 'Cats and Dogs', "Test Failed: Should return 'Cats and Dogs'"
print("Passed: Correct retrieval from a single-node setup (already inserted).")

