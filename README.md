# 💰 Personal Budget Tracker

## 1. Project Overview and Motivation

This project is a simple command-line utility developed in **Python** to help individuals, particularly students, track their personal income and expenses. It falls under the **Finance & Banking** and **Productivity & Automation** theme.

### Problem Solved
The core problem addressed is the lack of **financial visibility**. Users often spend money without knowing their net balance or where the majority of their funds are going. This application solves this by providing a clear, persistent system for logging transactions and generating immediate category-based summaries.

### Core Concepts Applied (Fundamentals in Programming)
The solution was designed using the following concepts learned in the course:
* **Data Structures:** Using **Lists** to manage the transaction history and **Dictionaries** to structure individual transactions and calculate category totals.
* **File Handling (I/O):** Reading data from and writing data to the persistent file (`transactions.txt`).
* **Modular Programming:** Breaking the solution into clear, single-purpose functions (`load_transactions`, `view_summary`, etc.).
* **Control Flow:** Implementation of the `while True` loop for the main menu and `try-except` blocks for robust input validation.

---

## 2. Project Features

The application meets the Minimum Viable Product (MVP) requirements with the following functionalities:

* **Persistent Data:** Transactions are automatically loaded from and saved to `transactions.txt` upon program start and exit.
* **Add Transaction:** Allows logging of financial events, categorizing them as Income (I) or Expense (E).
* **Input Validation:** The system ensures that the user enters valid numerical amounts, preventing program crashes.
* **Comprehensive Summary:** Calculates the **Net Balance** (Total Income - Total Expense) and provides a detailed breakdown of total spending per category (e.g., Food, Rent).

---

## 3. Instructions to Run the Project (CRITICAL FOR EVALUATION)

To run the application, follow these steps in your terminal or PowerShell:

1.  **Clone the Repository:**
    Use the correct username to clone the project.
    ```bash
    git clone [https://github.com/AviralSahu960/Personal-Budget-Tracker-Project.git](https://github.com/AviralSahu960/Personal-Budget-Tracker-Project.git)
    ```
2.  **Navigate to the Directory:**
    ```bash
    cd Personal-Budget-Tracker-Project
    ```
3.  **Run the Python Script:**
    ```bash
    python budget_tracker.py
    ```
4.  Follow the on-screen menu prompts (1, 2, or 3) to interact with the budget tracker.
---

## 4. Visual Documentation

All required visual proofs have been provided in the dedicated folders:

* **Screenshots:** Located in the **`screenshots/`** directory, demonstrating the menu and the final calculated summary report.
* **Screen Recording:** A short video demonstration of the full application cycle (adding data, viewing the report, and saving) is available in the **`recordings/`** directory.

---

