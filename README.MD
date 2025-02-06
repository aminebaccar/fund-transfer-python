# Fund Transfer API Test Automation  

## 📌 Overview  
This project contains automated tests for the **Fund Transfer API**, which allows performing **account creation, deposits, withdrawals, fund transfers, and currency conversions**.  
The tests are implemented using **Python + Pytest + Requests** and ensure the application's functionality, error handling, and concurrency support.

---

## 🚀 Prerequisites  
Before running the tests, ensure the following dependencies are installed:  

- **Python 3.8+** (For executing the tests)
- **pip** (Python package manager)  
- **Git** (For cloning the repository)  

Check Python installation:  
```bash
python --version
pip --version
```

Ensure that the **Fund Transfer API backend is running** before running tests.  

---

## 📦 Installation  

1️⃣ **Clone the Repository:**  
```bash
git clone https://github.com/aminebaccar/fund-transfer-python.git
cd fund-transfer-python
```

2️⃣ **Create a Virtual Environment (Recommended)**  
```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows
```

3️⃣ **Install Required Dependencies**  
```bash
pip install -r requirements.txt
```

---

## ⚙️ Ensuring the Fund Transfer API Backend is Running  

Before executing the tests, ensure that the **Fund Transfer API backend** is **running and accessible** at:  
📍 `http://localhost:8080/swagger-ui/index.html`  

If the API is not running, refer to the **backend repository** or your deployment setup for instructions.

---

## ✅ Running the Tests  

Run **all tests**:  
```bash
pytest -v --html=report.html
```

Run **tests for a specific module**:  
```bash
pytest tests/test_fund_transfer.py
```

Run a **single test**:  
```bash
pytest tests/test_fund_transfer.py::test_successful_transfer
```

Run tests **with parallel execution**:  
```bash
pytest -n 4
```

---

## 📂 Project Structure  

```
fund-transfer-api-tests/
│── tests/
│   ├── test_create_account.py
│   ├── test_get_account.py
│   ├── test_deposit_withdraw.py
│   ├── test_fund_transfer.py
│   ├── test_negative_cases.py
│   ├── test_exchange_rate.py
│   ├── test_concurrent_transfers.py
│── utils/
│   ├── api_client.py
│   ├── config.py
│   ├── helpers.py
│   ├── logger.py
│── requirements.txt
│── pytest.ini
│── README.md
```

### **Key Directories & Files**
- **`tests/`** – Contains all test cases.
- **`utils/`** – Contains helper modules like API client, logging configuration and execution handler.
- **`requirements.txt`** – Lists required Python dependencies.
- **`pytest.ini`** – Configures Pytest behavior.
- **`README.md`** – Documentation.

---

## 📋 Test Case Overview  

---

## **🟢 Core Functionality Test Cases (High Priority)**
| **TC No.** | **Test Name** | **Description** | **Test File** |
|-----------|-------------|-----------------|----------------|
| ✅ TC_01 | `test_create_account` | Create an account with a valid currency and verify it is created successfully. | `test_create_account.py` |
| ✅ TC_02 | `test_get_account` | Retrieve account details using a valid account ID and verify response. | `test_get_account.py` |
| ✅ TC_03 | `test_deposit_money` | Deposit money into an account and verify the updated balance. | `test_deposit_withdraw.py` |
| ✅ TC_04 | `test_withdraw_money` | Withdraw money from an account and verify the updated balance. | `test_deposit_withdraw.py` |
| ✅ TC_05 | `test_successful_transfer` | Transfer funds between two accounts with the same currency and verify balance updates. | `test_fund_transfer.py` |
| ✅ TC_06 | `test_successful_currency_exchange` | Transfer funds between two accounts with different currencies and validate the conversion. | `test_exchange_rate.py` |
| ✅ TC_07 | `test_transfer_rollback_on_failure` | Ensure failed transactions do not deduct money. | `test_fund_transfer.py` |
| ✅ TC_08 | `test_transfer_invalid_format` | Attempt to transfer with an invalid account format (not a 9-digit number) and verify failure. | `test_negative_cases.py` |
| ✅ TC_09 | `test_transfer_non_existent_account` | Attempt to transfer with a non-existent account and verify that the API returns a `404`. | `test_negative_cases.py` |
| ✅ TC_10 | `test_transfer_insufficient_balance` | Attempt to transfer more money than available in the debit account and verify failure. | `test_negative_cases.py` |
| ✅ TC_11 | `test_transfer_fails_when_exchange_rate_unavailable` | Attempt to transfer funds with an invalid currency to simulate an exchange rate retrieval failure. | `test_exchange_rate.py` |

---

## **🟡 Additional Validations & Negative Test Cases**
| **TC No.** | **Test Name** | **Description** | **Test File** |
|-----------|-------------|-----------------|----------------|
| ✅ TC_12 | `test_withdraw_more_than_balance` | Attempt to withdraw more money than available and verify that it fails. | `test_negative_cases.py` |
| ✅ TC_13 | `test_minimum_transfer_limit` | Ensure zero or negative transfers are rejected. | `test_negative_cases.py` |

---

## **🔴 Concurrency & Performance Testing**
| **TC No.** | **Test Name** | **Description** | **Test File** |
|-----------|-------------|-----------------|----------------|
| ✅ TC_14 | `test_concurrent_transfers` | Perform 100 simultaneous transactions to test concurrency. | `test_concurrent_transfers.py` |
| ✅ TC_15 | `test_concurrent_transfers_high_load` | Perform 2500 simultaneous transactions to test system load. | `test_concurrent_transfers.py` |

---

## **🚀 Summary of Test Coverage**
✅ **Core API features** like account creation, deposits, withdrawals, and transfers are well-covered.  
✅ **Negative scenarios** like invalid formats, non-existent accounts, and insufficient balance are included.  
✅ **Concurrency testing** ensures the API can handle multiple transactions.  

---

## 📊 Generating Test Reports  

Pytest generates HTML reports for better visualization of test results.  
Run:  
```bash
pytest --html=report.html --self-contained-html
```

View results by opening **`report.html`** in your browser.

---

### **📝 Logging Test Results**  

To track test execution details, a logging system is implemented. Logs are saved both **to a file (`test_results.log`) and displayed in the console** for real-time monitoring.  

#### **📌 Viewing Logs in the Console**
Logs are automatically displayed when running tests:  
```bash
pytest -v
```

#### **📌 Saving Logs to a File**  
All test execution details are saved in **`test_results.log`** for later analysis.  

#### **📌 Manually Checking the Log File**
To view the latest test logs, open:  
```bash
cat test_results.log  # Linux/Mac
type test_results.log # Windows
```

#### **📌 Running Tests with Logging**
Ensure logs are captured properly by running:  
```bash
pytest --log-cli-level=INFO
```

#### **📌 Reset Log File Before Each Run**
If needed, clear the log file before running tests:  
```bash
echo "" > test_results.log  # Linux/Mac
echo. > test_results.log    # Windows
```

This ensures each test run starts with a **fresh log file** instead of appending logs.

---

## 🎯 Additional Notes  
- Ensure that the **API backend is running** before executing tests.  
- The test suite is **modular**, allowing easy additions of new test cases.

---
## 📬 Contact  
For any issues or suggestions, reach out via email.
