def zero(n= None): #your code here
    if n is None:
        return 0
    else:
        return n(0)
        
def one(n = None): #your code here
     if n is None:
         return 1
     else: 
        return n(1)
def two(n = None): #your code here
    if n is None:
	    return 2
    else:
        return n(2)
def three(n = None): #your code here
    if n is None:
        return 3
    else:
        return n(3)
def four(n = None): #your code here
    if n is None:
        return 4
    else:
        return n(4)
def five(n = None): #your code here
    if n is None:
        return 5
    else:
        return n(5)
def six(n = None): #your code here    
    if n is None:
        return 6
    else:
        return n(6)
def seven(n = None): #your code here
    if n is None:
        return 7
    else:
        return n(7)
def eight(n = None): #your code here
    if n is None:
        return 8
    else:
        return n(8)
def nine(n = None): #your code here
    if n is None:
        return 9
    else:
        return n(9)

def plus(n): #your code here
    return lambda x: n+x
def minus(n): #your code here
    return lambda x: n-x
def times(n): #your code here
     return lambda x: n * x
def divided_by(n): #your code here
     return lambda x: n/x


print(seven(times(five())))
