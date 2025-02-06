import pytest
from utils.api_client import APIClient
from utils.logger import log_test_result

def test_create_account():
    """Test creating an account with a valid currency."""
    test_name = "test_create_account"
    response = APIClient.create_account("USD")

    try:
        assert response.status_code == 201, f"Unexpected response: {response.text}"
        assert response.json()["currency"] == "USD"
        log_test_result(test_name, "PASS")
    except AssertionError as e:
        log_test_result(test_name, "FAIL", str(e))
        raise
