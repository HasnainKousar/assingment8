#######################
# Test for operations
#######################

import pytest
from typing import Union
from app.operations import add, subtract, multiply, divide

# Define a type alias for Number
Number = Union[int, float]


# ----------------------------------------
# Unit tests for add function
# ----------------------------------------


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),  # Test positive integers
        (1.5, 2.5, 4.0),  # Test positive floats
        (-1, -2, -3),  # Test negative integers
        (-1.5, -2.5, -4.0),  # Test negative floats
        (0, 0, 0),  # Test zero
        (1, -1, 0),  # Test positive and negative integers

    ],
    ids=[
        "positive_integers",
        "positive_floats",
        "negative_integers",
        "negative_floats",
        "zero",
        "positive_negative_integers",
    ]
)
def test_add(a: Number, b: Number, expected: Number) -> None:
    """
    Test the add function with various inputs including positive and negative integers and floats.

    This test uses parameterized inputs to cover a range of scenarios,
    ensuring that the add function behaves as expected.
    
    Parameters:
    - a (Number): The first number to add.
    - b (Number): The second number to add.
    - expected (Number): The expected result of the addition.

    Steps:
    1. Call the add function with the provided inputs.
    2. Assert that the result matches the expected value.

    Example:
    >>> test_add(1, 2, 3)
    >>> test_add(1.5, 2.5, 4.0)
    """

    # Call the add function with the provided inputs
    result = add(a, b)

    # Assert that the result matches the expected value
    assert result == expected, f"Expected add({a}, {b}) to be {expected}, but got {result}"


# ----------------------------------------
# Unit tests for subtract function
# ----------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),  # Test positive integers
        (5.5, 2.5, 3.0),  # Test positive floats
        (-1, -2, 1),  # Test negative integers
        (-1.5, -2.5, 1.0),  # Test negative floats
        (0, 0, 0),  # Test zero
        (1, -1, 2),  # Test positive and negative integers
    ],
    ids=[
        "positive_integers",
        "positive_floats",
        "negative_integers",
        "negative_floats",
        "zero",
        "positive_negative_integers",
    ]
)
def test_subtract(a: Number, b: Number, expected: Number) -> None:
    """
    Test the subtract function with various inputs including positive and negative integers and floats.

    This test uses parameterized inputs to cover a range of scenarios,
    ensuring that the subtract function behaves as expected.
    
    Parameters:
    - a (Number): The number to subtract from.
    - b (Number): The number to subtract.
    - expected (Number): The expected result of the subtraction.

    Steps:
    1. Call the subtract function with the provided inputs.
    2. Assert that the result matches the expected value.

    Example:
    >>> test_subtract(5, 3, 2)
    >>> test_subtract(5.5, 2.5, 3.0)
    """

    # Call the subtract function with the provided inputs
    result = subtract(a, b)

    # Assert that the result matches the expected value
    assert result == expected, f"Expected subtract({a}, {b}) to be {expected}, but got {result}"


# ----------------------------------------
# Unit tests for multiply function
# ----------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),  # Test positive integers
        (2.5, 4, 10.0),  # Test positive floats
        (-2, -3, 6),  # Test negative integers
        (-2.5, -4, 10.0),  # Test negative floats
        (0, 5, 0),  # Test zero
        (1, -1, -1),  # Test positive and negative integers
    ],
    ids=[
        "positive_integers",
        "positive_floats",
        "negative_integers",
        "negative_floats",
        "zero",
        "positive_negative_integers",
    ]
)
def test_multiply(a: Number, b: Number, expected: Number) -> None:
    """
    Test the multiply function with various inputs including positive and negative integers and floats.

    This test uses parameterized inputs to cover a range of scenarios,
    ensuring that the multiply function behaves as expected.
    
    Parameters:
    - a (Number): The first number to multiply.
    - b (Number): The second number to multiply.
    - expected (Number): The expected result of the multiplication.

    Steps:
    1. Call the multiply function with the provided inputs.
    2. Assert that the result matches the expected value.

    Example:
    >>> test_multiply(2, 3, 6)
    >>> test_multiply(2.5, 4, 10.0)
    """

    # Call the multiply function with the provided inputs
    result = multiply(a, b)

    # Assert that the result matches the expected value
    assert result == expected, f"Expected multiply({a}, {b}) to be {expected}, but got {result}"

# ----------------------------------------
# Unit tests for divide function
# ----------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2),  # Test positive integers
        (7.5, 2.5, 3.0),  # Test positive floats
        (-6, -3, 2),  # Test negative integers
        (-7.5, -2.5, 3.0),  # Test negative floats
        (0, 1, 0),  # Test zero
        (1, -1, -1),  # Test positive and negative integers
    ],
    ids=[
        "positive_integers",
        "positive_floats",
        "negative_integers",
        "negative_floats",
        "zero",
        "positive_negative_integers",
    ]
)
def test_divide(a: Number, b: Number, expected: Number) -> None:
    """
    Test the divide function with various inputs including positive and negative integers and floats.

    This test uses parameterized inputs to cover a range of scenarios,
    ensuring that the divide function behaves as expected.
    
    Parameters:
    - a (Number): The number to be divided.
    - b (Number): The number to divide by.
    - expected (Number): The expected result of the division.

    Steps:
    1. Call the divide function with the provided inputs.
    2. Assert that the result matches the expected value.

    Example:
    >>> test_divide(6, 3, 2)
    >>> test_divide(7.5, 2.5, 3.0)
    """

    # Call the divide function with the provided inputs
    result = divide(a, b)

    # Assert that the result matches the expected value
    assert result == expected, f"Expected divide({a}, {b}) to be {expected}, but got {result}"


# ----------------------------------------
# Unit tests for divide function with zero division error
# ----------------------------------------

def test_divide_by_zero() -> None:
    """
    Test the divide function for zero division error.

    This test checks that dividing by zero raises a ValueError as expected.
    
    Steps:
    1. Attempt to call the divide function with a non-zero numerator and zero denominator.
    2. Use pytest.raises to assert that a ValueError is raised.
    3. Assert that the error message is as expected.

    Example:
    >>> test_divide_by_zero()
    """
    
    # Attempt to call the divide function with a non-zero numerator and zero denominator
    with pytest.raises(ValueError) as exc_info:
        # Attempt to divide by zero
        divide(5, 0)

    # Assert that a ValueError is raised
    assert "Cannot divide by zero." in str(exc_info.value), \
        f"Expected error message 'Cannot divide by zero.', but got '{exc_info.value}'"
