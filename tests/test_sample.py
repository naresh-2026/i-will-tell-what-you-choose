import pytest
import sys
import os

# Ensure the app module is in the system path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    client = app.test_client()
    yield client  # Provide the test client to use in tests

def test_home_page(client):
    """Test if the first page (startPage.html) loads when the app is run."""
    response = client.get("/")
    assert response.status_code == 200  # Check if the response is OK
    assert b"game of magic" in response.data  # Ensure 'startPage' content is in response
