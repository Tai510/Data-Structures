import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    # max number of nodes it can hold
    # current number of nodes it is holding
    # we want to hold key-value in order
    # We want to hold key-value entries in order
    # DLL: remove from the tail
    #Array: pop()
    #Array: if we add to back, remove from front: unshift()
    # We want to add things to the front (the most recently used thing)
     # Array: add to front
     #DLL: add to head
     # Alternative: add to back of an array, then sort(), then pop from back
     # Decision: Use DLL!
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.storage = {}
        self.dll = DoublyLinkedList()
    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
    # if it's in the cache, move the node to the end of our DLL
         # Pull value from dict by key
        # update position in list or return None
         if (key in self.storage):
         # print('key in storage')
            node = self.storage[key]
            self.dll.move_to_end(node)
         # print(f'value to return {node.value[1]}')
            return node.value[1]
         else:
            return None
    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # Add pair to the cache - add to dict and to the DLL nodes
        # Mark as most recently used - Put in head of DLL
        # If at max capacity dump oldest - remove from DLL tail
        # If already exists, overwrite value - update dict
      # Cases to handle: does the key already exist in the cache yes or no
      # are you on a cap or not
     # If key is already in cache
        if (key in self.storage):
             # key here so replace value
            node = self.storage[key]
            node.value = (key, value)
            self.dll.move_to_end(node)
        else:
            # If cache limit reached
            if (self.size == self.limit):
                #remove from dll and storage
                del self.storage[self.dll.head.value[0]]
                self.dll.remove_from_head()
                self.size -= 1
                # # Add new key-values to storage and dll
            self.dll.add_to_tail((key,value))
            self.storage[key] = self.dll.tail
            self.size += 1