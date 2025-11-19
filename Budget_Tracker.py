import os
import datetime

# The global list to store all transactions loaded from the file
transactions = []
FILE_NAME = 'transactions.txt'

# --- 1. File Handling Functions ---

def load_transactions():
    """Reads data from the transactions file and loads it into the global list."""
    loaded_data = []
    
    # Check if the file exists before trying to read it
    if not os.path.exists(FILE_NAME):
        print("No existing data file found. Starting a new budget.")
        return loaded_data

    try:
        with open(FILE_NAME, 'r') as file:
            for line in file:
                # Format: date|category|description|type|amount
                parts = line.strip().split('|')
                
                # Basic check for corrupt data
                if len(parts) == 5:
                    # Ensure amount is loaded as a positive value (normalize any sign)
                    try:
                        amt = abs(float(parts[4]))
                    except ValueError:
                        # skip malformed amount lines
                        continue

                    transaction = {
                        'date': parts[0],
                        'category': parts[1],
                        'desc': parts[2],
                        'type': parts[3],
                        'amount': amt  # Always store positive amount
                    }
                    loaded_data.append(transaction)
    except Exception as e:
        print(f"Error loading data: {e}. Starting with an empty list.")
        
    return loaded_data

def save_transactions():
    """Writes the current list of transactions to the file."""
    try:
        with open(FILE_NAME, 'w') as file:
            for t in transactions:
                # Ensure saved amount is written without any sign (always positive)
                line = f"{t['date']}|{t['category']}|{t['desc']}|{t['type']}|{abs(t['amount'])}\n"
                file.write(line)
        print("✅ Data saved successfully!")
    except Exception as e:
        print(f"❌ Error saving data: {e}")

# --- 2. Data Entry Function ---

def add_transaction():
    """Prompts user for transaction details, validates the date, and rejects zero/negative amounts."""
    global transactions
    print("\n--- Add New Transaction ---")
    
    # 1. Date Validation Loop
    while True:
        date_str = input("Date (YYYY-MM-DD): ")
        try:
            # strptime checks for valid format (YYYY-MM-DD) and valid calendar dates (e.g., rejects Feb 30th)
            datetime.datetime.strptime(date_str, '%Y-%m-%d')
            
            # Additional check for realistic year range
            year = int(date_str.split('-')[0])
            if year < 2000 or year > 2100:
                 print("⚠️ Please enter a realistic year (2000-2100).")
                 continue
            break
        except ValueError:
            print("🚫 Invalid date: Please use YYYY-MM-DD format (e.g., 2025-01-15) and ensure the date is possible.")
            
    # 2. Category and Description Inputs
    category = input("Category (e.g., Food, Rent, Income): ")
    desc = input("Description: ")
    
    # 3. Transaction Type Validation (I/E)
    while True:
        t_type = input("Type (I for Income, E for Expense): ").upper()
        if t_type in ['I', 'E']:
            break
        print("Invalid type. Enter 'I' or 'E'.")

    # 4. Amount Validation Loop (Rejects zero amounts; accepts inputs with + or - but stores positive)
    while True:
        try:
            amount_input = input("Amount: ")
            # allow users to type +50 or -50; normalize to positive
            amount = abs(float(amount_input))
            
            # CRITICAL CHECK: Ensure amount is positive (non-zero)
            if amount == 0:
                print("❌ Amount cannot be zero. Please enter a positive value.")
                continue # Forces the user to re-enter the amount
            
            # If successful and positive, exit the loop
            break
        except ValueError:
            print("❌ Invalid input. Please enter a number for the amount.")

    # 5. Create and Store Transaction
    new_transaction = {
        'date': date_str,
        'category': category,
        'desc': desc,
        'type': t_type,
        'amount': amount # Guaranteed to be a positive number (no +/− sign stored)
    }

    transactions.append(new_transaction)
    print("✨ Transaction added successfully!")

# --- 3. Calculation and Reporting Function ---

def view_summary():
    """Calculates and prints the net balance and category totals."""
    if not transactions:
        print("\nNo transactions recorded yet.")
        return

    net_balance = 0.0
    category_totals = {}

    for t in transactions:
        amount = t['amount']
        category = t['category']

        # 1. Update Net Balance
        if t['type'] == 'I':
            net_balance += amount
        elif t['type'] == 'E':
            net_balance -= amount

        # 2. Update Expense Category Totals (Tracking expenses provides better insight)
        if t['type'] == 'E':
            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

    # Print the report
    print("\n====================================")
    print("💰 FINANCIAL SUMMARY REPORT")
    print(f"Current Net Balance: ${net_balance:,.2f}")
    
    print("------------------------------------")
    print("📊 Expense Breakdown by Category")
    
    # Sort categories alphabetically for a cleaner report
    for category in sorted(category_totals.keys()):
        total = category_totals[category]
        print(f"- {category:<15}: ${total:,.2f}")
        
    print("====================================")

# --- 4. Main Program Flow ---

def main_menu():
    """The main loop that runs the program and calls other functions."""
    global transactions
    # Load data first thing
    transactions = load_transactions()  

    while True:
        print("\n--- Personal Budget Tracker Menu ---")
        print("1. Add New Transaction")
        print("2. View Summary Report")
        print("3. Exit and Save")
        
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            save_transactions()
            print("Program finished. Thank you!")
            break
        else:
            print("🚫 Invalid choice. Please try again.")

# --- Program Entry Point ---

if __name__ == "__main__":
    main_menu()
