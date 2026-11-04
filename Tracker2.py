
income_records = []
expense_records = []


def get_positive_amount(prompt):
    valid = False
 
    while valid == False:
        try:
            amount = float(input(prompt))

            if amount > 0:
                valid = True
            else:
                print("[ERROR] Amount must be greater than 0.")

        except ValueError:
            print("[ERROR] Please enter a valid number.")

    return amount


def get_category():
    categories = ["Food", "Transportation", "School", "Others"]

    print("\n========== EXPENSE CATEGORIES ==========")
    print("1. Food")
    print("2. Transportation")
    print("3. School")
    print("4. Others")

    valid = False

    while valid == False:
        try:
            choice = int(input("Choose a category: "))

            if choice == 1:
                category = categories[0]
                valid = True

            elif choice == 2:
                category = categories[1]
                valid = True

            elif choice == 3:
                category = categories[2]
                valid = True

            elif choice == 4:
                category = categories[3]
                valid = True

            else:
                print("[ERROR] Please choose 1-4.")

        except ValueError:
            print("[ERROR] Please enter a number.")

    return category


def add_income():
    amount = get_positive_amount("Enter income amount: ")

    income_records.append(amount)

    print("Income was added successfully.")


def add_expense():
    category = get_category()
    amount = get_positive_amount("Enter expense amount: ")
  
    if calculate_total_expenses() + amount > calculate_total_income():
        print("[ERROR] You cannot exceed your total income!")
        return

    expense_records.append([category, amount])

    print("Expense was added successfully.")

    remaining = calculate_remaining_budget()
    total_income = calculate_total_income()

    if remaining == 0:
         print("[WARNING] Your budget is completely gone!")


    elif total_income > 0 and remaining <= total_income * 0.20:
       print("[WARNING] Your budget is almost gone!")
       

    elif total_income > 0 and remaining <= total_income * 0.50:
        print("[WARNING] Your budget is getting small!")

def display_income_records():
    print("\n========== INCOME RECORDS ==========")

    if income_records == []:
        print("No income records found.")

    else:
        print("AMOUNT")
        print("-------------------------------------")

        for amount in income_records:
            print("P", amount)

def display_expense_records():
    print("\n========== EXPENSE RECORDS ==========")

    if expense_records == []:
        print("No expense records found.")

    else:
        print(f"{'CATEGORY':<25}{'AMOUNT':>10}")
        print("-------------------------------------")

        for record in expense_records:
            print(f"{record[0]:<25}P {record[1]:>7}")
            
def display_all_transactions():
    display_income_records()
    display_expense_records()

def calculate_total_income():
    total = 0

    for amount in income_records:
        total = total + amount

    return total

def calculate_total_expenses():
    total = 0

    for record in expense_records:
        total = total + record[1]

    return total

def calculate_remaining_budget():
    total_income = calculate_total_income()
    total_expenses = calculate_total_expenses()

    remaining = total_income - total_expenses

    return remaining

def display_summary():
    total_income = calculate_total_income()
    total_expenses = calculate_total_expenses()
    remaining = calculate_remaining_budget()

    print("\n========== BUDGET SUMMARY ==========")
    print("Total Income: P", total_income)
    print("Total Expenses: P", total_expenses)
    print("Remaining Budget: P", remaining)

    if remaining > 0:
        print("[STATUS] You still have available budget.")

    elif remaining == 0:
        print("[STATUS] Your budget has been fully used.")

    else:
        print("[WARNING] Expenses are greater than your income.")


def display_menu():
    print("\n========================================")
    print("     DIGITAL EXPENSE TRACKER SYSTEM")
    print("             WEEKLY BUDGET")
    print("========================================")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. View Budget Summary")
    print("5. Exit")
    print("========================================")

def run_system():
    running = True

    while running:
        display_menu()

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_income()

        elif choice == "2":
            add_expense()

        elif choice == "3":
            display_all_transactions()

        elif choice == "4":
            display_summary()

        elif choice == "5":
            print("\nThank you for using the Digital Expense Tracker System.")
            print("Program ended.")
            running = False

        else:
            print("[ERROR] Invalid choice. Please select 1-5.")


accounts = {}


def register_account():
    print("\n========== ACCOUNT REGISTRATION ==========")

    username = input("Create username: ")

    if username in accounts:
        print("[ERROR] Username already exists.")
        return False

    password = input("Create password: ")

    if password == "":
        print("[ERROR] Password cannot be empty.")
        return False

    accounts[username] = password

    print("Account registered successfully.")
    return True


def login_account():
    print("========== ACCOUNT LOGIN ==========")

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in accounts and accounts[username] == password:
        print("Login successful!")
        print("Welcome,", username)
        return True

    else:
        print("[ERROR] Invalid username or password.")
        return False


def account_system():
    registered = False
    logged_in = False

    while logged_in == False:

        print("========================================")
        print("          ACCOUNT SYSTEM")
        print("========================================")
        print("1. Register Account")
        print("2. Login")
        print("3. Exit")
        print("========================================")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            registered = register_account()

        elif choice == "2":
            if registered == False:
                print("[ERROR] Please register an account first.")
            else:
                logged_in = login_account()

        elif choice == "3":
            print("Program ended.")
            return False

        else:
            print("[ERROR] Invalid choice. Please select 1-3.")

    return True

if account_system():
    run_system()
