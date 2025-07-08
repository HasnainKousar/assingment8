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
