##############################################
# tests/integration/test_fastapi_calculator.py
##############################################

"""
This module contains integration tests for the FastAPI calculator application.

"""

import pytest
from fastapi.testclient import TestClient
from main import app  # Import the FastAPI app from the main module

#-----------------------
# Pytest fixture for the FastAPI client
#-----------------------

@pytest.fixture
def client():
    """
    Fixture to create a TestClient for the FastAPI application.
    
    This allows us to initialize the TestClient instance that can be used 
    to simulate requests to the FastAPI application without needing to run the live server.

    """
    with TestClient(app) as client:
        yield client # This will provide the client to the tests


#-----------------------
# Test add_api
#-----------------------

def test_add_api(client):
    """
    Test the Addition API endpoint.
    
    This test verifies the /add endpoint correctly addes two numbers
    provided in the JSON payload and returns the expected result.

    Steps:
    1. Send a POST request to the /add endpoint with a JSON data containing two numbers.
    2. Assert that the response status code is 200 (OK).
    3. Assert that the response JSON contains the expected result.
    """
    # Send a POST request to the /add endpoint with two numbers
    response = client.post("/add", json={"a": 3, "b": 5})

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    # Assert that the response JSON contains the expected result
    assert response.json() == {"result": 8}, f"Expected JSON response {{'result': 8}}, got {response.json()}"


#-----------------------
# Test subtract_api
#-----------------------

def test_subtract_api(client):
    """
    Test the Subtraction API endpoint.
    
    This test verifies the /subtract endpoint correctly subtracts two numbers
    provided in the JSON payload and returns the expected result.

    Steps:
    1. Send a POST request to the /subtract endpoint with a JSON data containing two numbers.
    2. Assert that the response status code is 200 (OK).
    3. Assert that the response JSON contains the expected result.
    """
    # Send a POST request to the /subtract endpoint with two numbers
    response = client.post("/subtract", json={"a": 10, "b": 4})

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    # Assert that the response JSON contains the expected result
    assert response.json() == {"result": 6}, f"Expected JSON response {{'result': 6}}, got {response.json()}"

#-----------------------
# Test multiply_api
#-----------------------

def test_multiply_api(client):
    """
    Test the Multiplication API endpoint.
    
    This test verifies the /multiply endpoint correctly multiplies two numbers
    provided in the JSON payload and returns the expected result.

    Steps:
    1. Send a POST request to the /multiply endpoint with a JSON data containing two numbers.
    2. Assert that the response status code is 200 (OK).
    3. Assert that the response JSON contains the expected result.
    """
    # Send a POST request to the /multiply endpoint with two numbers
    response = client.post("/multiply", json={"a": 4, "b": 5})

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    # Assert that the response JSON contains the expected result
    assert response.json() == {"result": 20}, f"Expected JSON response {{'result': 20}}, got {response.json()}"


#-----------------------
# Test divide_api
#-----------------------

def test_divide_api(client):
    """
    Test the Division API endpoint.
    
    This test verifies the /divide endpoint correctly divides two numbers
    provided in the JSON payload and returns the expected result.

    Steps:
    1. Send a POST request to the /divide endpoint with a JSON data containing two numbers.
    2. Assert that the response status code is 200 (OK).
    3. Assert that the response JSON contains the expected result.
    """
    # Send a POST request to the /divide endpoint with two numbers
    response = client.post("/divide", json={"a": 10, "b": 2})

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    # Assert that the response JSON contains the expected result
    assert response.json() == {"result": 5}, f"Expected JSON response {{'result': 5}}, got {response.json()}"


#-----------------------
# Test divide_by_zero_api
#-----------------------

def test_divide_by_zero_api(client):
    """
    Test the Division by Zero API endpoint.
    
    This test verifies that the /divide endpoint raises a ValueError when attempting to divide by zero.

    Steps:
    1. Send a POST request to the /divide endpoint with a JSON data containing a number and zero.
    2. Assert that the response status code is 400 (Bad Request).
    3. Assert that the response JSON contains an error message indicating division by zero is not allowed.
    """
    # Send a POST request to the /divide endpoint with a number and zero
    response = client.post("/divide", json={"a": 10, "b": 0})

    # Assert that the response status code is 400 (Bad Request)
    assert response.status_code == 400, f"Expected status code 400, got {response.status_code}"

    # Assert that the JSON response contains an 'error' field
    assert 'error' in response.json(), "Response JSON does not contain 'error' field"
    
    # Assert that the 'error' field contains the correct error message
    assert "Cannot divide by zero." in response.json()['error'], \
        f"Expected error message 'Cannot divide by zero.', got '{response.json()['error']}'"
    
