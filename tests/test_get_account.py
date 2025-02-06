import pytest
from utils.api_client import APIClient
from utils.logger import log_test_result

@pytest.fixture(scope="module")
def setup_account():
    """Create an account and return its ID."""
    response = APIClient.create_account("EUR")
    assert response.status_code == 201
    return response.json()["id"]

def test_get_account(setup_account):
    """Retrieve account details using a valid account ID."""
    test_name = "test_get_account"
    response = APIClient.get_account(setup_account)

    try:
        assert response.status_code == 200, f"Unexpected response: {response.text}"
        assert response.json()["id"] == setup_account
        log_test_result(test_name, "PASS")
    except AssertionError as e:
        log_test_result(test_name, "FAIL", str(e))
        raise