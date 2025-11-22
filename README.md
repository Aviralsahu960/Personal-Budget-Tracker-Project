#  Personal Budget Tracker

## 1. Project Overview and Motivation

This project is a command-line utility developed in **Python** to help individuals, particularly students, track their personal income and expenses. It falls under the **Finance & Banking** and **Productivity & Automation** theme.

### Problem Solved
The core problem addressed is the lack of **financial visibility** and **control**. The application provides a clear, persistent system for logging transactions and generating immediate, category-based summaries, allowing users to monitor their net financial standing.

### Core Concepts Applied (Fundamentals in Programming)
The solution was designed using the following concepts learned in the course:
* **Data Structures:** Using **Lists** to manage the transaction history and **Dictionaries** to structure individual transactions and calculate category totals.
* **File Handling (I/O):** Reading and writing persistent data to the external file (`transactions.txt`).
* **Modular Programming:** The solution is broken into specialized functions (`load_transactions`, `add_transaction`, `view_summary`) for clear top-down design.
* **Control Flow & Validation:** Implemented `while` loops for continuous menu navigation and robust `try-except` blocks for input validation (rejecting negative amounts, non-numeric amounts, and impossible dates).

---

## 2. Project Features

The application meets all core requirements with the following functionalities:

* **Persistent Data:** Transactions are automatically loaded from and saved to `transactions.txt` upon program start and exit.
* **Add Transaction:** Allows logging of financial events, categorizing them as Income (I) or Expense (E).
* **Robust Input Validation:** Strictly rejects any input that is non-numeric, zero, negative, or an invalid calendar date (e.g., month > 12).
* **Comprehensive Summary:** Calculates the **Net Balance** (Total Income - Total Expense) and provides a detailed breakdown of total spending per category.

---

## 3. Instructions to Run the Project (CRITICAL FOR EVALUATION)

The evaluator must follow these specific steps to clone and execute the project successfully.

1.  **Navigate to Target Directory:**
    Open the Command Prompt or PowerShell and navigate to the directory where you want the project folder to be created.
    ```bash
    cd Desktop
    ```

2.  **Clone the Repository:**
    Run the `git clone` command using the verified URL to download the entire project.
    ```bash
    git clone https://github.com/Aviralsahu960/Personal-Budget-Tracker-Project.git
    ```

3.  **Navigate into the Project Folder:**
    ```bash
    cd Personal-Budget-Tracker-Project
    ```

4.  **Execute the Python Script:**
    Run the main application file.
    ```bash
    python budget_tracker.py
    ```

5.  **Interaction:**
    Follow the on-screen menu prompts (1, 2, or 3) to interact with the budget tracker.

---

## 4. Visual Documentation

All required visual proofs have been organized into the mandated directories for automated evaluation:

* **Screenshots:** Located in the **`screenshots/`** directory, demonstrating the application's menu, input validation, and final summary report.
* **Screen Recording:** A short video demonstration of the full application cycle (adding data, viewing the report, and saving) is available in the **`recordings/`** directory.

---




