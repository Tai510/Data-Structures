import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    self.size += 1
    #item should go to the back of the queue
    return self.storage.append(item)
  
  def dequeue(self):
    # if there are no items in the queue
    if len(self.storage) > 0:
        self.size -= 1
        return self.storage.pop(0)
    else:
        return None
        
  def len(self):
        return len(self.storage)
    
   