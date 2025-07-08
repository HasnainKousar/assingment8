###################
# app/operations/__init__.py
###################

"""


"""

from typing import Union

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """Add two numbers and return the result.
    
    Parameters:
    - a (Number): The first number to add.
    - b (Number): The second number to add.
    
    Returns:
    - Number: The sum of the two numbers.
    
    Example:
    >>> add(2, 3)
    5
    >>> add(2.5, 3.5)
    6.0"""

    #perform addition
    result = a + b
    return result


def subtract(a: Number, b: Number) -> Number:
    """Subtract the second number from the first and return the result.
    
    Parameters:
    - a (Number): The number to subtract from.
    - b (Number): The number to subtract.
    
    Returns:
    - Number: The result of the subtraction.
    
    Example:
    >>> subtract(5, 3)
    2
    >>> subtract(5.5, 2.5)
    3.0"""
    
    #perform subtraction
    result = a - b
    return result





