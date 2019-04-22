"""
A priority queue acts like a queue in that you dequeue an item by removing it 
from the front. However, in a priority queue the logical order of items inside
a queue is determined by their priority. The highest priority items are at 
the front of the queue and the lowest priority items are at the back. When 
you enqueue an item on a priority queue, the new item may move all the way to
the front.
A binary heap will allow both enqueue and dequeue items in O(logn) time.
This is a min heap.
"""


class BinaryHeap(object):
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2

    def perc_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.percUp(self.current_size)

    def min_child(self, i):
        if (i * 2 + 1) > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def del_min(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.perc_down(1)
        return retval

    def is_empty(self):
        return self.current_size == 0

    def size(self):
        return self.current_size

    def build_heap(self, keys):
        i = len(keys) // 2
        self.current_size = len(keys)
        self.heap_list = [0] + keys[:]
        while (i > 0):
            self.perc_down(i)
            i = i - 1
