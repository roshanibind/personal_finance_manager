from expense import Expense
from utils import validate_amount, validate_date, check_budget
from file_manager import load_expenses, save_expenses, backup_data, restore_data, export_summary
from reports import generate_report
from charts import category_chart, monthly_chart
from menu import show_menu

def main():
    expenses = load_expenses()

    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            amt = validate_amount(input("Amount: "))
            if amt is None: continue
            cat = input("Category: ")
            date = validate_date(input("Date (YYYY-MM-DD): "))
            if date is None: continue
            desc = input("Description: ")

            expenses.append(Expense(amt, cat, date, desc))
            save_expenses(expenses)
            check_budget(expenses)
            print("✅ Expense added")

        elif choice == "2":
            for e in expenses:
                print(e.amount, e.category, e.date, e.description)

        elif choice == "3":
            summary = generate_report(expenses)
            export_summary(summary)

        elif choice == "4":
            backup_data()

        elif choice == "5":
            restore_data()
            expenses = load_expenses()

        elif choice == "6":
            category_chart(expenses)
            monthly_chart(expenses)

        elif choice == "7":
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()
