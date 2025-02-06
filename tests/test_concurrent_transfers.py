import pytest
from utils.api_client import APIClient
from utils.helpers import run_concurrent_transfers
from utils.logger import log_test_result


@pytest.fixture(scope="module")
def setup_accounts():
    """Create two accounts and deposit a large balance for concurrent transactions."""
    debit = APIClient.create_account("USD")
    credit = APIClient.create_account("EUR")

    assert debit.status_code == 201 and credit.status_code == 201, "Failed to create accounts"

    APIClient.deposit(debit.json()["id"], 1000000, "USD")
    return debit.json()["id"], credit.json()["id"]

def test_concurrent_transfers(setup_accounts):
    """Test multiple concurrent transfers (100 transfers)."""
    test_name = "test_concurrent_transfers"
    debit_id, credit_id = setup_accounts

    try:
        run_concurrent_transfers(debit_id, credit_id, num_transfers=100)
        log_test_result(test_name, "PASS")
    except Exception as e:
        log_test_result(test_name, "FAIL", str(e))
        raise

def test_concurrent_transfers_high_load(setup_accounts):
    """Perform 2500 simultaneous transactions to test system load."""
    test_name = "test_concurrent_transfers_high_load"
    debit_id, credit_id = setup_accounts

    try:
        run_concurrent_transfers(debit_id, credit_id, num_transfers=2500)
        log_test_result(test_name, "PASS")
    except Exception as e:
        log_test_result(test_name, "FAIL", str(e))
        raise