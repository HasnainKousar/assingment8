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


