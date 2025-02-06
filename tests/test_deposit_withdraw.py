import pytest
from utils.api_client import APIClient
from utils.logger import log_test_result

@pytest.fixture(scope="module")
def setup_account():
    """Create an account and return its ID."""
    response = APIClient.create_account("GBP")
    assert response.status_code == 201
    return response.json()["id"]

def test_deposit_money(setup_account):
    """Test depositing money into an account."""
    test_name = "test_deposit_money"
    response = APIClient.deposit(setup_account, 200, "GBP")

    try:
        assert response.status_code == 200, f"Deposit failed: {response.text}"
        log_test_result(test_name, "PASS")
    except AssertionError as e:
        log_test_result(test_name, "FAIL", str(e))
        raise

def test_withdraw_money(setup_account):
    """Test withdrawing money from an account."""
    test_name = "test_withdraw_money"
    response_deposit = APIClient.deposit(setup_account, 200, "GBP")
    assert response_deposit.status_code == 200, f"Initial deposit failed: {response_deposit.text}"

    response = APIClient.withdraw(setup_account, 100, "GBP")
    try:
        assert response.status_code == 200, f"Withdrawal failed: {response.text}"
        log_test_result(test_name, "PASS")
    except AssertionError as e:
        log_test_result(test_name, "FAIL", str(e))
        raise