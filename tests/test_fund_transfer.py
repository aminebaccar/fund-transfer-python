import pytest
from utils.api_client import APIClient
from utils.logger import log_test_result


@pytest.fixture(scope="module")
def setup_accounts():
    """Create two USD accounts and deposit funds into one."""
    debit = APIClient.create_account("USD")
    credit = APIClient.create_account("USD")

    assert debit.status_code == 201 and credit.status_code == 201, "Failed to create accounts"

    debit_id = debit.json()["id"]
    credit_id = credit.json()["id"]

    APIClient.deposit(debit_id, 60, "USD")  # Ensure enough balance
    return debit_id, credit_id

def test_transfer_rollback_on_failure(setup_accounts):
    """Ensure failed transactions do not deduct money."""
    test_name = "test_transfer_rollback_on_failure"
    debit_id, credit_id = setup_accounts
    debit_before = APIClient.get_account(debit_id).json()["balance"]

    response = APIClient.transfer(debit_id, credit_id, 9999999, "EUR")

    debit_after = APIClient.get_account(debit_id).json()["balance"]

    try:
        assert response.status_code == 400, "Expected failure for insufficient funds"
        assert debit_after == debit_before, "Balance changed despite transaction failure"
        log_test_result(test_name, "PASS")
    except AssertionError as e:
        log_test_result(test_name, "FAIL", str(e))
        raise

def test_successful_transfer(setup_accounts):
    """Test transferring funds between two accounts."""
    test_name = "test_successful_transfer"
    debit_id, credit_id = setup_accounts
    response = APIClient.transfer(debit_id, credit_id, 50, "EUR")

    try:
        assert response.status_code == 200, f"Unexpected response: {response.text}"
        log_test_result(test_name, "PASS")
    except AssertionError as e:
        log_test_result(test_name, "FAIL", str(e))
        raise