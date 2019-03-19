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
    return merge_sort(a + b)

def quick_sort(items):
    '''
    Return array of items, sorted in ascending order
    '''
    if len(items) == 1 or len(items) == 0:
        return items
    else:
        pivot = items[0]
        i = 0
        for j in range(len(items)-1):
            if items[j+1] < pivot:
                items[j+1],items[i+1] = items[i+1], items[j+1]
                i += 1
        items[0],items[i] = items[i],item[0]
        first_part = quicksort(items[:i])
        second_part = quicksort(items[i+1:])
        first_part.append(items[i])
        return first_part + second_part
