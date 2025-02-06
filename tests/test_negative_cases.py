import pytest
from utils.api_client import APIClient
from utils.logger import log_test_result


@pytest.fixture(scope="module")
def setup_accounts():
    """Create accounts for negative test cases."""
    debit = APIClient.create_account("USD")
    credit = APIClient.create_account("EUR")

    assert debit.status_code == 201 and credit.status_code == 201, "Failed to create accounts"
    return debit.json()["id"], credit.json()["id"]

def test_transfer_invalid_format(setup_accounts):
    """Test transferring with an invalid account format."""
    test_name = "test_transfer_invalid_format"
    invalid_debit_id = 999
    credit_id = setup_accounts[1]

    response = APIClient.transfer(invalid_debit_id, credit_id, 50, "EUR")

    try:
        assert response.status_code == 400, "Invalid transfer format should return 400"
        log_test_result(test_name, "PASS")
    except AssertionError as e:
        log_test_result(test_name, "FAIL", str(e))
        raise

def test_transfer_non_existent_account(setup_accounts):
    """Test transferring funds to a non-existent account."""
    test_name = "test_transfer_non_existent_account"
    debit_id, _ = setup_accounts
    non_existent_id = 999999999

    response = APIClient.transfer(debit_id, non_existent_id, 50, "EUR")

    try:
        assert response.status_code == 404, "Expected 404 for non-existent account"
        log_test_result(test_name, "PASS")
    except AssertionError as e:
        log_test_result(test_name, "FAIL", str(e))
        raise

def test_transfer_insufficient_balance(setup_accounts):
    """Test transferring more than available balance."""
    test_name = "test_transfer_insufficient_balance"
    debit_id, credit_id = setup_accounts
    response = APIClient.transfer(debit_id, credit_id, 10000, "EUR")

    try:
        assert response.status_code == 400, f"Unexpected response: {response.text}"
        log_test_result(test_name, "PASS")
    except AssertionError as e:
        log_test_result(test_name, "FAIL", str(e))
        raise

def test_withdraw_more_than_balance(setup_accounts):
    """Test withdrawing more money than available balance."""
    test_name = "test_withdraw_more_than_balance"
    debit_id, _ = setup_accounts
    response = APIClient.withdraw(debit_id, 1000, "USD")

    try:
        assert response.status_code == 400, "Expected 400 for excessive withdrawal"
        log_test_result(test_name, "PASS")
    except AssertionError as e:
        log_test_result(test_name, "FAIL", str(e))
        raise

def test_minimum_transfer_limit(setup_accounts):
    """Ensure transfers with zero or negative amounts are rejected."""
    test_name = "test_minimum_transfer_limit"
    debit_id, credit_id = setup_accounts

    for invalid_amount in [0, -10]:
        response = APIClient.transfer(debit_id, credit_id, invalid_amount, "EUR")
        try:
            assert response.status_code == 400, f"Expected 400 but got {response.status_code}"
            json_response = response.json()
            assert "fieldErrors" in json_response, "Expected 'fieldErrors' in response"
            assert "amount" in json_response["fieldErrors"], "Expected 'amount' error in 'fieldErrors'"
            assert "strictly positive" in json_response["fieldErrors"]["amount"], (
                f"Expected error message about strictly positive amounts, got: {json_response['fieldErrors']['amount']}"
            )
            log_test_result(test_name, "PASS")
        except AssertionError as e:
            log_test_result(test_name, "FAIL", str(e))
            raise