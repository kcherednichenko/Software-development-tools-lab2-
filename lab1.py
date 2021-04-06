def addition(x, y):

    
    """Does action of adding value x to value y and convert values to integer.

    Args:
        x (any): number
        y (any): number

    Returns:
        [integer]: An integer holding the result
    """    
    
    return int(x) + int(y)
   

def divide(x, y):
    """Divide value x by value y and convert values to integer.

    Args:
        x (any): dividend
        y (any): divisor

    Raises:
        ZeroDivisionError: divisor can't be 0

    Returns:
        [integer]: An integer holding the result
    """    
    if y != 0:
        return int(x) / int(y)
    else:
        print("Error! Divisor can't be 0")
        raise ZeroDivisionError


def substract(x, y):
    """Does action of substraction value x to value y and convert values to integer.

    Args:
        x (any): minuend
        y (any): subtrahend

    Returns:
        [integer]: An integer holding the result
    """    
    return int(x) - int(y)


def multiply(x, y):
    """Does multiply value x to value y and convert values to integer.


    Args:
        x (any): multiplier
        y (any): multiplier

    Returns:
        [integer]: An integer holding the result
    """    
    return int(x) * int(y)




