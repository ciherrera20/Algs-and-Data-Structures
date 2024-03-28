class MaxHeap:
    '''
    Implements a max heap on objects that can be directly compared

    Heap invariant: nodes in the binary tree have greater or equal values than all their descendants

    Example:

            15
            /\\
           /  \\
          /    \\
         /      \\
        7        14
       /\\       /\\
      /  \\     /  \\
     3     6   10   13
    /\\   /\\ /\\   /\\
    1 2   4 5 8 9  11 12

    The tree can be represented as an array:
    [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14]
    [15,  7, 14,  3,  6, 10, 13,  1,  2,  4,  5,  8,  9, 11, 12]

    Getting children:
    0 -> (1, 2)
    1 -> (3, 4)
    2 -> (5, 6)
    3 -> (7, 8)
    4 -> (9, 10)
    5 -> (11, 12)
    6 -> (13, 14)
    .
    .
    .
    i -> (2*(i+1)-1, 2*(i+1))

    1 + 2 + 4 + 8
    [1] + [2, 3] + [4, 5, 6, 7] + [8, 9, 10, 11, 12, 13, 14, 15]

    1 + ... + 2^k = 2^{k+1} - 1
    '''
    def __init__(self):
        self._data = []
    
    ### Helper functions ###

    def _children(self, i: int) -> (int, int):
        '''
        Gets the indices of the two children of node i
        '''
        return (2 * (i + 1) - 1, 2 * (i + 1))
    
    def _parent(self, i: int) -> int:
        '''
        Gets the index of the parent of node i
        Returns -1 if the node is the root node (i.e. if i = 0)
        '''
        return int((i + 1) / 2) - 1
    
    def _swap(self, i: int, j: int) -> int:
        '''
        Swap two nodes
        Return the new index of the node that used to be at index i (i.e. j)
        '''
        temp = self._data[i]
        self._data[i] = self._data[j]
        self._data[j] = temp
        return j
    
    ### Interface ###

    def peek(self) -> int:
        '''
        Return the maximum element
        '''
        return self._data[0]
    
    def push(self, n: int) -> None:
        '''
        Add an element
        '''
        i = len(self._data)
        j = self._parent(i)
        self._data.append(n)
        while j != -1 and self._data[i] > self._data[j]:
            i = self._swap(i, j)
            j = self._parent(i)
    
    def pop(self) -> int:
        '''
        Remove the maximum element and return it
        '''
        old_max = self._data[0]
        n = self._data.pop()

        if len(self._data) != 0:
            self._data[0] = n
            i = 0
            j, k = self._children(i)
            while (j < len(self._data) and n < self._data[j]) or (k < len(self._data) and n < self._data[k]):
                if j < len(self._data) and k < len(self._data):
                    _, m = max((self._data[j], j), (self._data[k], k))
                    i = self._swap(i, m)
                elif j < len(self._data):
                    i = self._swap(i, j)
                else:
                    i = self._swap(i, k)
                j, k = self._children(i)
                
        return old_max

# [12, 8, 3, 1, 8, 2, 1, 0]
#     12
#   8   3
#  1 8 2 1
# 0

# [0, 8, 3, 1, 8, 2, 1]

#    0
#  8   3
# 1 8 2 1