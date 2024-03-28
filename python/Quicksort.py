def quicksort(nums, lo=None, hi=None, debug=0):
    '''
    Implementation of the quicksort algorithm
    '''
    if lo == None:
        lo = 0
    if hi == None:
        hi = len(nums) - 1
    if debug > 0:
        print("Input:      ", nums[lo:hi+1], lo, hi)
    if hi - lo <= 1:
        return nums
    pivot = nums[(hi + lo) // 2]
    p = partition(nums, pivot, lo, hi)
    if debug > 0:
        print("pivot =", pivot, "p =", (hi + lo) // 2, "p' =", p)
        print("Partitioned:", nums[lo:hi+1], lo, hi)
    quicksort(nums, lo, p - 1, debug=debug)
    quicksort(nums, p + 1, hi, debug=debug)
    return nums

def partition(nums, pivot, lo, hi, debug=0):
    '''
    Partition the list in place so that the numbers less than the pivot are to the left and the numbers greater are to the right
    Note: p should be in [lo, hi]
    '''
    i = lo
    j = hi
    while True:
        if debug > 0:
            s = [" "] * 3 * len(nums)
            s[3 * i] = "i"
            s[3 * j] = "j"
            print("    " + "".join(s))
            print("#1", nums, i, j)
        while nums[i] < pivot:
            i += 1
        
        if debug > 0:
            s = [" "] * 3 * len(nums)
            s[3 * i] = "i"
            s[3 * j] = "j"
            print("    " + "".join(s))
            print("#2", nums, i, j)
        while nums[j] > pivot:
            j -= 1

        if debug > 0:
            s = [" "] * 3 * len(nums)
            s[3 * i] = "i"
            s[3 * j] = "j"
            print("    " + "".join(s))
            print("#3", nums, i, j)
        if i >= j:
            return j
        else:
            if nums[i] == pivot and nums[j] == pivot:
                j -= 1
            else:
                swap(nums, i, j)
            
            if debug > 0:
                s = [" "] * 3 * len(nums)
                s[3 * i] = "i"
                s[3 * j] = "j"
                print("    " + "".join(s))
                print("#4", nums, i, j)

def swap(nums, i, j):
    '''
    Swap the numbers at indices i and j
    '''
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

# quicksort([6, 3, 2, 1, 8, 7, 9, 4, 7, 9, 1, 2])

'''
 j
"dabcadbcbb"
{d: 0}

 ij
"dabcadbcbb"
{d: 0, a: 1}

 i j
"dabcadbcbb"
{d: 0, a: 1, b: 2}

 i  j
"dabcadbcbb"
{d: 0, a: 1, b: 2, c: 3}

 i   j
"dabcadbcbb"
{d: 0, a: 1, b: 2, c: 3}

   i j
"dabcadbcbb"
{d: 0, a: 4, b: 2, c: 3}

   i  j
"dabcadbcbb"
{d: 0, a: 4, b: 2, c: 3}
'''
