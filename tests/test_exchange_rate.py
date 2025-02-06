import pytest
from utils.api_client import APIClient

@pytest.fixture(scope="module")
def setup_accounts_with_different_currencies():
    """Create two accounts with different currencies and deposit funds into one."""
    debit = APIClient.create_account("USD")
    credit = APIClient.create_account("EUR")

    assert debit.status_code == 201 and credit.status_code == 201, "Failed to create accounts"

    debit_id = debit.json()["id"]
    credit_id = credit.json()["id"]

    APIClient.deposit(debit_id, 1000, "USD")  # Deposit sufficient funds
    return debit_id, credit_id

def test_successful_currency_exchange(setup_accounts_with_different_currencies):
    """Test fund transfer with currency conversion."""
    debit_id, credit_id = setup_accounts_with_different_currencies

    debit_before = APIClient.get_account(debit_id).json()["balance"]
    credit_before = APIClient.get_account(credit_id).json()["balance"]

    response = APIClient.transfer(debit_id, credit_id, 100, "EUR")
    assert response.status_code == 200, f"Currency exchange transfer failed: {response.text}"

    debit_after = APIClient.get_account(debit_id).json()["balance"]
    credit_after = APIClient.get_account(credit_id).json()["balance"]

    assert debit_after < debit_before, "Debit account balance should decrease"
    assert credit_after > credit_before, "Credit account balance should increase"

def test_transfer_fails_when_exchange_rate_unavailable(setup_accounts_with_different_currencies):
    """Test fund transfer fails if exchange rate cannot be retrieved (invalid currency)."""
    debit_id, credit_id = setup_accounts_with_different_currencies

    invalid_currency = "XXX"  # Fake currency to force failure
    response = APIClient.transfer(debit_id, credit_id, 100, invalid_currency)

    assert response.status_code == 400, f"Expected 400 but got {response.status_code}"

    json_response = response.json()
    assert "fieldErrors" in json_response, "Response should contain fieldErrors"
    assert "currency" in json_response["fieldErrors"], "Error should be related to currency"
    assert "not an uppercase char sequence of 3 letters" in json_response["fieldErrors"]["currency"]
