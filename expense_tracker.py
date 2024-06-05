import csv
from collections import defaultdict

def get_expense():
    """
    Prompts user to input expense details.

    Returns:
        tuple: A tuple containing date, category, description, and amount.
    """
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Transportation): ")
    description = input("Enter the description of the expense: ")
    try:
        amount = float(input("Enter the amount spent: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return get_expense()
    return date, category, description, amount

def save_expense(date, category, description, amount):
    """
    Saves the expense details to a CSV file.

    Args:
        date (str): The date of the expense.
        category (str): The category of the expense.
        description (str): A brief description of the expense.
        amount (float): The amount spent.
    """
    with open('expenses.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

def read_expenses():
    """
    Reads expenses from the CSV file.

    Returns:
        list: A list of expense records.
    """
    expenses = []
    try:
        with open('expenses.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                expenses.append(row)
    except FileNotFoundError:
        print("No expenses recorded yet.")
    return expenses

def monthly_summary():
    """
    Generates a summary of expenses by month.

    Returns:
        dict: A dictionary with months as keys and total expenses as values.
    """
    expenses = read_expenses()
    summary = defaultdict(float)
    for date, category, description, amount in expenses:
        month = date[:7]  # Extract YYYY-MM
        summary[month] += float(amount)
    return summary

def category_summary():
    """
    Generates a summary of expenses by category.

    Returns:
        dict: A dictionary with categories as keys and total expenses as values.
    """
    expenses = read_expenses()
    summary = defaultdict(float)
    for date, category, description, amount in expenses:
        summary[category] += float(amount)
    return summary

def main():
    """
    Main function to run the Expense Tracker application.
    """
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Category Summary")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            date, category, description, amount = get_expense()
            save_expense(date, category, description, amount)
        elif choice == '2':
            summary = monthly_summary()
            if summary:
                print("\nMonthly Summary:")
                for month, total in summary.items():
                    print(f"{month}: ${total:.2f}")
            else:
                print("No expenses recorded yet.")
        elif choice == '3':
            summary = category_summary()
            if summary:
                print("\nCategory Summary:")
                for category, total in summary.items():
                    print(f"{category}: ${total:.2f}")
            else:
                print("No expenses recorded yet.")
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
