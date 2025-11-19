import os

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
                    transaction = {
                        'date': parts[0],
                        'category': parts[1],
                        'desc': parts[2],
                        'type': parts[3],
                        'amount': float(parts[4])  # Convert amount back to float
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
                # Format the transaction into a pipe-separated string
                line = f"{t['date']}|{t['category']}|{t['desc']}|{t['type']}|{t['amount']}\n"
                file.write(line)
        print("✅ Data saved successfully!")
    except Exception as e:
        print(f"❌ Error saving data: {e}")

# --- 2. Data Entry Function ---

def add_transaction():
    """Prompts user for transaction details and adds it to the list."""
    print("\n--- Add New Transaction ---")
    date = input("Date (YYYY-MM-DD): ")
    category = input("Category (e.g., Food, Rent, Income): ")
    desc = input("Description: ")
    
    # Validation for transaction type
    while True:
        t_type = input("Type (I for Income, E for Expense): ").upper()
        if t_type in ['I', 'E']:
            break
        print("Invalid type. Enter 'I' or 'E'.")

    # Validation for amount
    while True:
        try:
            # Use abs() to ensure amount is stored as a positive number regardless of user input
            amount = abs(float(input("Amount: "))) 
            if amount <= 0:
                print("Amount must be positive.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number for the amount.")

    # Create the new transaction dictionary
    new_transaction = {
        'date': date,
        'category': category,
        'desc': desc,
        'type': t_type,
        'amount': amount
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