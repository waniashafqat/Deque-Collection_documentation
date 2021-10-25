# Python program for Queue implementation using collections documentation.
from collections import deque
q = deque()

# Adding elements to a queue.
q.append('a')   # First element in the queue added.
q.append('b')
q.append('c')
q.append('d')
q.append('e')  # Last element in the queue added.

# Display the whole queue.
print("\nOriginal queue: ")
print(q)

# Creating a shallow copy of a queue.
q.copy()
print(q)

# Removing elements from a queue.
# First element pushed into the queue will be removed first. (FIFO Method)
print("\nElements removed from the queue: ")
print(q.popleft())  # First element is removed.
print(q.popleft())  # Second element is removed.

# Displaying queue after removing elements.
print("\nQueue after removing elements: ")
print(q)

# Reversing the order of remained elements in the queue.
q.reverse()
print("\nReversed queue: ")
print(q)

# Checking whether the queue is empty or not.
if len(q) == 0:
    print("\nThe queue is EMPTY!")
else:
    print("\nThe queue is not EMPTY!")

# Removing all the elements from the queue.
q.clear()
print("\nAll the elements have been removed.")
print("The queue is EMPTY!")
print(q)

