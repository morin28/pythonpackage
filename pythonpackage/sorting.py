def bubble_sort(items):
    '''
    Return array of items, sorted in ascending order
    '''
    for i in range(0, len(items) -1):
	    	for j in range(0, len(items) - 1 - i):
	    		if items[j] > items[j+1]:
		   		 items[j], items[j+1] = items[j+1], items[j]
    return items

def merge_sort(items):
    '''
    Return array of items, sorted in ascending order
    '''
    def merge(A, B):
        new_list = []
        while len(A) > 0 and len(B) > 0:
            if A[0] < B[0]:
                new_list.append(A[0])
            	A.pop(0)
        new_list = []
        while len(A) > 0 and len(B) > 0:
            if A[0] < B[0]:
                new_list.append(A[0])
                A.pop(0)
            else:
                new_list.append(B[0])
                B.pop(0)

        if len(A) == 0:
            new_list = new_list + B
        if len(B) == 0:
            new_list = new_list + A

        return new_list
    len_i = len(items)
    # Base case. A list of size 1 is sorted.
    if len_i <= 1:
        return items
    # Recursive case. Find midpoint of list
    middle = int(len_i / 2)
    # divide list into two halves
    a = merge_sort(items[:middle])
    b = merge_sort(items[middle:])
    # call merge_sort function on each half of list
    return merge(a,b)

def quick_sort(items, index=-1):
    len_i = len(items)

    if len_i <= 1:
        # Logic Error
        # identified with test run [1,5,4,3, 2, 6, 5, 4, 3, 8, 6, 5, 3, 1]
        # len <= 1
        return items

    pivot = items[index]
    small = []
    large = []
    dup = []
    for i in items:
        if i < pivot:
            small.append(i)
        elif i > pivot:
            large.append(i)
        elif i == pivot:
            dup.append(i)

    small = quick_sort(small)
    large = quick_sort(large)

    return small + dup + large
