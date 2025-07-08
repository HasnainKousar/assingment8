#######################
# test_e2e.py
#######################

import pytest

# The following decorator and functions define end-to-end tests for the FastAPI calculator application.

@pytest.mark.e2e
def test_hello_world(page, fastapi_server):
    """
    This will test the homepage displaying "Hello World!".

    The test verifies that when user navigates to the homepage of the FastAPI application,
    the main header (<h1>) contains the text "Hello World!".
    
    """
    # Navigate to the homepage of the FastAPI application
    page.goto('http://localhost:8000/')

    # Assert that the main header contains "Hello World!"
    assert page.inner_text('h1') == 'Hello World'

@pytest.mark.e2e
def test_calculator_addition(page, fastapi_server):
    """
    This will test the addition endpoint of the FastAPI calculator application.

    The test verifies that when a POST request is made to the /add endpoint with two numbers,
    the response contains the correct sum.
    """
    
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Fill in the input fields for the first number 
    page.fill('#a', '3')

    # Fill in the input field for the second number
    page.fill('#b', '5')
    # Click the "Add" button to perform the addition operation
    page.click('button:text("Add")')
    
    # Assert that the result is displayed correctly in the result element
    assert page.inner_text('#result') == 'Calculation Result: 8'

@pytest.mark.e2e
def test_calculator_divide_by_zero(page, fastapi_server):
    """
    This will test the division by zero scenario in the FastAPI calculator application.

    The test verifies that when a POST request is made to the /divide endpoint with a number and zero,
    the response contains an error message indicating division by zero is not allowed.
    """
    
    # Navigate to the homepage of the FastAPI application
    page.goto('http://localhost:8000')
    
    # Fill in the input fields for the first number
    page.fill('#a', '10')

    # Fill in the input field for the second number with zero
    page.fill('#b', '0')
    
    # Click the "Divide" button to perform the division operation
    page.click('button:text("Divide")')
    
    # Assert that the result element contains an error message for division by zero
    assert page.inner_text('#result') == 'Error: Cannot divide by zero.'

