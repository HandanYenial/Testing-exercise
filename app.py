def adder(x,y):
    """Add two numbers together"""
    return x+y

assert adder(4,6)==9,"expected 4+6 to be 10."

def reverse_str(s):
    """
    Returns reverse of input str(s)
    """
    return s[::-1]
#slicing = [start:stop:step] so [::-1] beginning:end:backwards by 1, if it was positive it will be forward
