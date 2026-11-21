# Loafly – Production-Ready Python Pipeline

## Project Overview

Loafly is a Python-based order processing pipeline developed as part of the Codebasics Data Engineering Bootcamp assignment.

The project demonstrates how to transform a basic Python script into a modular, configurable, and production-ready application using functions, object-oriented programming, packages, logging, exception handling, API retries, and environment variables.

## Project Structure

```text
Loafly Project/
│
├── loafly/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── raw_orders.csv
├── gateway.py
├── legacy_orders.py
├── run_pipeline.py
├── .env                  # Local secrets (not committed)
├── env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Assignment Implementation

### Q1. Functions

- Created reusable `clean_price()` function to clean and convert price values.
- Created `apply_discount()` function to calculate discounted prices.
- Removed repeated inline transformations and hard-coded discount logic.

### Q2. Object-Oriented Programming

- Implemented an `Order` class to represent individual orders.
- Added attributes such as order ID, customer, and items.
- Implemented methods to add items and calculate order totals.

### Q3. Modules and Packages

Organized the application into a reusable `loafly` Python package:

- `config.py` – Application configuration.
- `models.py` – Order class and data model.
- `extract.py` – Reads raw order data from CSV.
- `transform.py` – Cleans prices and applies discounts.
- `load.py` – Sends processed orders to the API.

The `run_pipeline.py` file coordinates the complete workflow:

**Extract → Transform → Load**

### Q4. Configuration-Driven Design

Centralized application settings in `config.py`, including:

- Input file path
- Discount rate
- Currency
- API URL
- Retry count

This reduces hard-coded values throughout the application and makes configuration easier to maintain.

### Q5. Logging and Exception Handling

- Replaced print-based messages with Python logging.
- Configured timestamped INFO, WARNING, ERROR, and DEBUG messages.
- Logs are written to both the terminal and `loafly.log`.
- Added exception handling for missing and invalid prices.
- Used `finally` to record completion of each price-processing attempt.
- Invalid-price records are skipped without stopping the pipeline.

### Q6. Retry, Environments and Secrets

- Implemented API retry handling using a configurable retry count.
- Added a two-second delay between failed attempts.
- Logged successful API calls, retry warnings, and final failures.
- Used `python-dotenv` and `os.getenv()` to load the API key from environment variables.
- Added `.env` to `.gitignore` to prevent accidental exposure of secrets.
- Included `env.example` as a template for environment configuration.
- Added `requirements.txt` for dependency management.

The provided `gateway.py` API client was kept unchanged.

## Technologies Used

- Python
- CSV
- Object-Oriented Programming
- Python Logging
- Exception Handling
- python-dotenv
- Git and GitHub

## Setup and Execution

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd "Loafly Project"
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Windows CMD:

```cmd
.venv\Scripts\activate.bat
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Configure environment variables

Copy `env.example` to `.env` and add your API key:

```text
LOAFLY_API_KEY=your_api_key_here
```

### 6. Run the pipeline

```bash
python run_pipeline.py
```

## Expected Output

The pipeline:

1. Extracts order records from the CSV file.
2. Cleans prices and applies discounts.
3. Skips records with missing or invalid prices.
4. Sends valid records to the simulated orders API.
5. Retries failed API requests.
6. Logs pipeline execution and completion.

## Learning Outcomes

This assignment provided practical experience in writing reusable Python code, designing modular applications, handling unreliable API calls, managing configuration and secrets, and implementing production-style logging and exception handling.