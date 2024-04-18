#importing the heapq module for heap operation
import heapq

class Post:
    """
    this class represents the social media post, storing both the message content and the view count
    also customizes comparison operations to facilitate max-heap behavior based on views
    """
    def __init__ (self, message, views):
        self.message = message #initializing the message of the post
        self.views = views #initializing the number of views the post has

    def __lt__(self, other):
        #defining the lessthan operator as the opposite to implement
        #max heap based on views
        return self.views > other.views  #reversing the comparison to create a max-heap based on views

    def __repr__(self):
        #providing a formal string representation of the Post object
        #helps in debugging
        return f"Post(message='{self.message}', views={self.views})"
class MaxHeap:
    """
    this class implements a max-heap to manage Post objects, allowing for retrieval and removal of
    the post with the highest views in a priority queue manner
    """
    def __init__(self):
        self.heap = [] #creating an empty list to store the heap elements

    def push (self, post):
        #pushing a new post into the heap. 'heapq.heappush' is used, which adds the element
        #reorders the heap to maintain the heap property
        heapq.heappush(self.heap,post)
    def pop(self):
        #removing and return the largest element from the heap (due to max-heap property)
        #if the heap is empty, returns None
        return heapq.heappop(self.heap) if self.heap else None
    def peek(self):
        #returning the largest element without removing it from the heap
        #returing None if the heap is empty
        return self.heap[0] if self.heap else None

#creating an instance of MaxHeap
max = MaxHeap()

#Pushing posts with different view counts into the heap
max.push(Post("Cats and Dogs!", 1091))
max.push(Post("Say Hi to my new puppy:)", 2303))
max.push(Post("New country is visited!", 3209))

#Pop the post with the most views from the heap and print it
print(max.pop())
#Peek at the next post with the most views without removing it and print it
print(max.peek())
