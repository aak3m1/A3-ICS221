class TreeNode:
    """
    this class represents the augmented the BST which stores a post
    it os a datetime and the size of the subtree
    """
    def __init__(self, datetime, post):
        self.datetime = datetime #storing the datetime associated with the post
        self.post = post # storing the content of the social media post
        self.left = None #left child to None
        self.right = None #the right child to None.
        self.subtree_size = 1 #augmented data

class AugmentBST:
    """
    this class represents the augmented BST for the eeficient range
    queries of posts
    """
    def __init__(self):
        self.root=None #Start with an empty BST.


    def insert(self,datetime,post):
        #inserting a new post into the bst
        self.root = self.insert_recursive(self.root, datetime, post)

    def insert_recursive(self, node, datetime, post):
        if not node:
            return TreeNode(datetime, post)
        if datetime < node.datetime:
            node.left = self.insert_recursive(node.left, datetime, post)
        elif datetime > node.datetime:
            node.right = self.insert_recursive(node.right, datetime, post)
        else:
            raise ValueError("A post with the same datetime already exists.")
        node.subtree_size = 1 + self.getsize(node.left) + self.getsize(node.right)
        return node

    def find_range(self, startDatetime, endDatetime):
        """Finds all posts within a specific datetime range."""
        result = []
        self._find_range_recursive(self.root, startDatetime, endDatetime, result)
        return result

    def _find_range_recursive(self, node, startDatetime, endDatetime, result):
        if not node:
            return
        if startDatetime <= node.datetime <= endDatetime:
            result.append(node.post)
        if startDatetime < node.datetime:
            self._find_range_recursive(node.left, startDatetime, endDatetime, result)
        if node.datetime < endDatetime:
            self._find_range_recursive(node.right, startDatetime, endDatetime, result)

    def getsize(self, node): #returining the size of the subtree
        return node.subtree_size if node else 0


#using an example
augBST = AugmentBST()
augBST.insert('2024-04-03T12:00:00', 'Cats and Dogs')
augBST.insert('2024-04-20T12:30:00', 'New country is visited!')
augBST.insert('2023-12-18T13:00:00', 'Say Hi to my new puppy:)')

# Find posts in a range
posts_in_range = augBST.find_range('2023-12-18T13:00:00', '2024-04-20T12:35:00')
print(posts_in_range)