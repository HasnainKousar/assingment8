# tests/e2e/conftest.py
"""
THis file contains the configuration for end-to-end tests using Playwright.
It sets up the Playwright test environment, including the browser context and page fixtures.
"""

import subprocess
import time
import pytest
from playwright.sync_api import sync_playwright
import requests


