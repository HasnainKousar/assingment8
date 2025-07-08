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

