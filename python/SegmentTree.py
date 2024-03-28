import math

class SegmentTree:
    def __init__(self, arr, op, identity):
        self.arr = [0] * len(arr) * 2
        self.arr[len(arr):] = arr
        self.n = len(arr)
        self.op = op
        self.identity = identity
        self._ty = ""
        for i in reversed(range(1, len(arr))):
            self.arr[i] = op(self.arr[i * 2], self.arr[i * 2 + 1])

    def query(self, i: int, j: int):
        '''
        Returns the result of applying the operation on arr[i:j]
        '''
        i += self.n
        j += self.n
        s = self.identity

        while i < j:
            if i % 2 == 1:
                s = self.op(s, self.arr[i])
                i += 1
            if j % 2 == 1:
                j -= 1
                s = self.op(s, self.arr[j])
            i //= 2
            j //= 2
        
        return s
    
    def __str__(self, *args, **kwargs):
        return f"{self._ty}SegmentTree({self.arr[-self.n:].__str__(*args, **kwargs)})"
    
    def __repr__(self, *args, **kwargs):
        return f"{self._ty}SegmentTree({self.arr[-self.n:].__repr__(*args, **kwargs)})"

class SumSegmentTree(SegmentTree):
    def __init__(self, arr):
        super().__init__(arr, op=int.__add__, identity=0)
        self._ty = "Sum"

class MulSegmentTree(SegmentTree):
    def __init__(self, arr):
        super().__init__(arr, op=int.__mul__, identity=1)
        self._ty = "Mul"

class MaxSegmentTree(SegmentTree):
    def __init__(self, arr):
        super().__init__(arr, op=max, identity=-math.inf)
        self._ty = "Max"

class MinSegmentTree(SegmentTree):
    def __init__(self, arr):
        super().__init__(arr, op=min, identity=math.inf)
        self._ty = "Min"

if __name__ == "__main__":
    t = SumSegmentTree([2, 3, -1, 5, -2, 4, 8, 10])
    assert t.query(3, 7) == 15  # 5 - 2 + 4 + 8
    assert t.query(3, 6) == 7   # 5 - 2 + 4

    u = MaxSegmentTree([6, 10, 5, 2, 7, 1, 0, 9])
    assert u.query(3, 7) == 7  # max {2, 7, 1, 0}
    assert u.query(3, 8) == 9  # max {2, 7, 1, 0, 9}