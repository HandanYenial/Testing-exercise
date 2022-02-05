def reverse_str(s):
    """
    Returns reverse of input str(s)
    """
    return s[::-1]
#slicing= [start:stop:step] so [::-1]beginning:end:backwards by 1

    
def is_palindrome(s):
    """Boolean method to check whether given string is a palindrome"""
    reverse=reverse_str(s)
    return s.lower()==reverse.lower()
# it will check if the word is same with the reverse of it as pop

def factorial(n):
    """Calculates factorial iteratively"""
    if not (isinstance(n,int) and n>=0):
        raise ValueError("'n' must be a non-negative integer.")
    result=1
    for i in range(2,n+1):
        result*=i
    return result
