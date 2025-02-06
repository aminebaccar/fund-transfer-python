from utils.config import Config
import requests

class APIClient:
    BASE_URL = Config.BASE_URL

    @staticmethod
    def create_account(currency):
        url = f"{APIClient.BASE_URL}/account"
        payload = {"currency": currency}
        response = requests.post(url, json=payload)
        return response

    @staticmethod
    def get_account(account_id):
        url = f"{APIClient.BASE_URL}/account/{account_id}"
        return requests.get(url)

    @staticmethod
    def deposit(account_id, amount, currency):
        url = f"{APIClient.BASE_URL}/transaction/deposit"
        payload = {"accountId": account_id, "amount": amount, "currency": currency}
        return requests.post(url, json=payload)

    @staticmethod
    def withdraw(account_id, amount, currency):
        url = f"{APIClient.BASE_URL}/transaction/withdraw"
        payload = {"accountId": account_id, "amount": amount, "currency": currency}
        return requests.post(url, json=payload)

    @staticmethod
    def transfer(debit_id, credit_id, amount, currency):
        url = f"{APIClient.BASE_URL}/transaction/transfer"
        payload = {"debitAccountId": debit_id, "creditAccountId": credit_id, "amount": amount, "currency": currency}
        return requests.post(url, json=payload)
