#importing the heapq module for heap operation
import heapq

class Post:
    def __init__ (self, message, views):
        self.message = message #initializing the message of the post
        self.views = views #initializing the number of views the post has

    def __lt__(self, other):
        #defining the lessthan operator as the opposite to implement
        #max heap based on views
        return self.views > other.views
    def __repr__(self):
        return f"Post(message='{self.message}', views={self.views})"

class MaxHeap:
    def __init__(self):
        self.heap = []

    def push (self, post):
        heapq.heappush(self.heap,post)
    def pop(self):
        return heapq.heappop(self.heap) if self.heap else None
    def peek(self):
        return self.heap[0] if self.heap else None

max = MaxHeap()
max.push(Post("Cats and Dogs!", 100))
max.push(Post("Say Hi to my new puppy:)", 200))
max.push(Post("New country is visited!", 300))

print(max.pop())
print(max.peek())
