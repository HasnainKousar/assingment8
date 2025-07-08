# tests/e2e/conftest.py
"""
THis file contains the configuration for end-to-end tests using Playwright.
It sets up the Playwright test environment, including the browser context and page fixtures.
"""

from http import server
import subprocess
import time
from turtle import st
import pytest
from playwright.sync_api import sync_playwright
import requests


@pytest.fixture(scope="session")
def fastapi_server():
    """
    Fixture to start the FastAPI server before running tests and stop it after tests are done.
    """
    # Start the FastAPI app
    fastapi_process = subprocess.Popen(['python', 'main.py'])

    # Define the URL to check if the server is up
    server_url = 'http://127,0,0,1:8000/'

    # Wait for the server to start
    timeout = 30 
    start_time = time.time()
    server_up = False


    print("Starting FastAPI server...")

    while time.time() - start_time < timeout:
        try:
            response = requests.get(server_url)
            if response.status_code == 200:
                server_up = True
                break
        except requests.ConnectionError:
            pass
        time.sleep(1)

    if not server_up:
        fastapi_process.terminate()
        raise RuntimeError("FastAPI server failed to start within timeout period")
    
    yield

    

                               