def sum_array(array):
    '''
    Return sum of all items in array
    '''
    total = 0
    for i in array:
        total += i
    return total

def fibonacci(n):
    '''
    Return nth term in fibonacci sequence
    '''
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def factorial(n):
    '''
    Return n!
    '''
<<<<<<< HEAD
    if n == 1:
        return n
=======
    if n == 1 or n == 0:
        return 1
>>>>>>> 97a53f53b4a85643ec4415da575d46226053d60c
    else:
     return n * factorial(n-1)


def reverse(word):
    '''
    Return word in reverse
    '''
    return word[::-1]
