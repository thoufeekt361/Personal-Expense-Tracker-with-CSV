import csv
import os
from datetime import datetime
from collections import defaultdict

FILE = "expenses.csv"
FIELDS = ["date", "category", "description", "amount"]

def initialize_file():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()

def load_expenses():
    initialize_file()
    try:
        with open(FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return list(reader)
    except FileNotFoundError:
        return []

def save_expense(row):
    initialize_file()
    with open(FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writerow(row)

def get_valid_date():
    while True:
        date = input("Enter date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date! Please use YYYY-MM-DD.")

def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount (Rs.): "))
            if amount < 0:
                print("Amount cannot be negative!")
            else:
                return amount
        except ValueError:
            print("Please enter a valid number!")

def add_expense():
    print("\n========== ADD EXPENSE ==========")
    date = get_valid_date()
    category = input("Enter category: ").strip()
    while not category:
        print("Category cannot be empty!")
        category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()
    while not description:
        print("Description cannot be empty!")
        description = input("Enter description: ").strip()
    amount = get_valid_amount()
    expense = {
        "date": date,
        "category": category.title(),
        "description": description,
        "amount": f"{amount:.2f}"
    }
    save_expense(expense)
    print("\nExpense added successfully!")

def display_expenses(expenses):
    if not expenses:
        print("\nNo expenses found!")
        return
    print("\n" + "-" * 85)
    print(f"{'DATE':<15}{'CATEGORY':<18}{'DESCRIPTION':<30}{'AMOUNT':>12}")
    print("-" * 85)
    for expense in expenses:
        print(
            f"{expense['date']:<15}"
            f"{expense['category']:<18}"
            f"{expense['description']:<30}"
            f"Rs. {float(expense['amount']):>8.2f}"
        )
    print("-" * 85)

def view_expenses():
    print("\n========== ALL EXPENSES ==========")
    expenses = load_expenses()
    display_expenses(expenses)

def filter_expenses():
    print("\n========== FILTER EXPENSES ==========")
    print("1. Filter by Category")
    print("2. Filter by Month")
    choice = input("Enter your choice: ").strip()
    expenses = load_expenses()
    if choice == "1":
        category = input("Enter category: ").strip().lower()
        filtered = [
            e for e in expenses
            if e["category"].lower() == category
        ]
        print(f"\nExpenses in category: {category.title()}")
        display_expenses(filtered)
    elif choice == "2":
        month = input("Enter month (YYYY-MM): ").strip()
        try:
            datetime.strptime(month, "%Y-%m")
            filtered = [
                e for e in expenses
                if e["date"][:7] == month
            ]
            print(f"\nExpenses for month: {month}")
            display_expenses(filtered)
        except ValueError:
            print("Invalid month! Use YYYY-MM format.")
    else:
        print("Invalid choice!")

def totals_by_category(expenses):
    totals = defaultdict(float)
    for expense in expenses:
        category = expense["category"]
        amount = float(expense["amount"])
        totals[category] += amount
    return dict(totals)

def expense_summary():
    print("\n========== EXPENSE SUMMARY ==========")
    expenses = load_expenses()
    if not expenses:
        print("No expenses available for summary.")
        return
    totals = totals_by_category(expenses)
    print("\nCategory-wise Spending:")
    print("-" * 40)
    for category, total in sorted(totals.items()):
        print(f"{category:<20} Rs. {total:>10.2f}")
    grand_total = sum(
        float(expense["amount"])
        for expense in expenses
    )
    biggest_expense = max(
        expenses,
        key=lambda e: float(e["amount"])
    )
    print("-" * 40)
    print(f"{'Grand Total':<20} Rs. {grand_total:>10.2f}")
    print("\nBiggest Single Expense:")
    print(f"Category    : {biggest_expense['category']}")
    print(f"Description : {biggest_expense['description']}")
    print(f"Amount      : Rs. {float(biggest_expense['amount']):.2f}")
    print("-" * 40)

def main():
    initialize_file()
    while True:
        print("\n")
        print("=" * 45)
        print("       PERSONAL EXPENSE TRACKER")
        print("=" * 45)
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter Expenses")
        print("4. Expense Summary")
        print("5. Quit")
        print("=" * 45)
        choice = input("Enter your choice (1-5): ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_expenses()
        elif choice == "4":
            expense_summary()
        elif choice == "5":
            print("\nThank you for using Personal Expense Tracker!")
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice! Please select 1-5.")

if __name__ == "__main__":
    main()