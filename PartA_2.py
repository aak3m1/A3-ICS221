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
        #this method is to inset a new post into the BST if the tree is empty
        #this node becomes the root
        self.root = self.insert_recursive(self.root, datetime, post) #starting the recursive insertion process from the root

    def insert_recursive(self, node, datetime, post):
        #this method recursively find the correct spot to insert the new node and
        #update subtree sizes
        if not node:
            return TreeNode(datetime, post) #creeates a new node if there is no node
        if datetime < node.datetime:
            #insertingthe left subtree if the datetime is less than the current node's datetime
            node.left = self.insert_recursive(node.left, datetime, post)
        elif datetime > node.datetime:
            #inserting in the right subtree if the datetime is greater than the current node's datetime
            node.right = self.insert_recursive(node.right, datetime, post)
        else:
            #raising an error if a post with the same datetime exists (no duplicates allowed)
            raise ValueError("A post with the same datetime already exists.")
        #updating the subtree size after insertion.
        node.subtree_size = 1 + self.getsize(node.left) + self.getsize(node.right)
        return node #return the node after updating it
    def find_range(self, startDatetime, endDatetime):
        #all posts within the given datetime range as a list of tuples
        result = []
        #starting recursive range finding from the root.
        self.rangeRecursive(self.root, startDatetime, endDatetime, result)
        return result

    def rangeRecursive(self, node, startDatetime, endDatetime, result):
        #recursively searches for and collects posts that fall within
        #datetime range
        if not node:
            return #if the node is None, just return (base case)
        if startDatetime <= node.datetime <= endDatetime:
            #if the node's datetime is within the range
            # add it to the result list
            result.append((node.datetime, node.post))  # Append the tuple of datetime and post
        if startDatetime < node.datetime:
            #exploring the left subtree if the range starts before the node's datetime
            self.rangeRecursive(node.left, startDatetime, endDatetime, result)
        if node.datetime < endDatetime:
            #exploring right subtree if the range ends after the node's datetime
            self.rangeRecursive(node.right, startDatetime, endDatetime, result)


    def getsize(self, node): #returining the size of the subtree
        return node.subtree_size if node else 0 #returning 0 if the node is None


#example usage of the augmented BST
augBST = AugmentBST()

#inserting posts into the BST
augBST.insert('2024-04-03T12:00:00', 'Cats and Dogs')
augBST.insert('2024-04-20T12:30:00', 'New country is visited!')
augBST.insert('2023-12-18T13:00:00', 'Say Hi to my new puppy:)')

#finding posts in a range
posts_in_range = augBST.find_range('2023-12-18T13:00:00', '2024-04-20T12:35:00')

for i, (datetime, post) in enumerate(posts_in_range, 1):
    print(f"Post {i}: [{datetime}] {post}")
