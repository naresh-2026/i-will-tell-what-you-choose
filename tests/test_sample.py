import pytest
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
    assert b"startPage" in response.data  # Ensure 'startPage' content is in response
