import threading
from utils.api_client import APIClient

def run_concurrent_transfers(debit_id, credit_id, num_transfers):
    """Helper function to execute multiple transfers concurrently."""

    def transfer_funds():
        response = APIClient.transfer(debit_id, credit_id, 10, "EUR")
        assert response.status_code in [200, 429], f"Transfer failed: {response.text}"

    threads = [threading.Thread(target=transfer_funds) for _ in range(num_transfers)]

    for t in threads:
        t.start()
    for t in threads:
        t.join()