# from expense import Expense
# from file_manager import save_expenses


# def add_expense(expenses):
#     amount = float(input("Amount: "))
#     category = input("Category: ")
#     date = input("Date (YYYY-MM-DD): ")
#     description = input("Description: ")

#     expense = Expense(amount, category, date, description)
#     expenses.append(expense)

#     save_expenses(expenses)
#     print("✅ Expense added successfully!")


# def show_menu():
#     print("\n--- Personal Finance Manager ---")
#     print("1. Add Expense")
#     print("2. Exit")






# from expense import Expense
# from file_manager import save_expenses
# from utils import validate_date


# def add_expense(expenses):
#     amount = float(input("Amount: "))
#     category = input("Category: ")
#     date = input("Date (YYYY-MM-DD): ")

#     if not validate_date(date):
#         print("❌ Invalid date format")
#         return

#     description = input("Description: ")
#     expenses.append(Expense(amount, category, date, description))
#     save_expenses(expenses)
#     print("✅ Expense added")


# def view_expenses(expenses):
#     print("\n--- All Expenses ---")
#     for i, exp in enumerate(expenses):
#         print(f"{i}. {exp.date} | {exp.category} | {exp.amount} | {exp.description}")


# def delete_expense(expenses):
#     view_expenses(expenses)
#     index = int(input("Enter index to delete: "))

#     if 0 <= index < len(expenses):
#         expenses.pop(index)
#         save_expenses(expenses)
#         print("✅ Expense deleted")
#     else:
#         print("❌ Invalid index")


# def update_expense(expenses):
#     view_expenses(expenses)
#     index = int(input("Enter index to update: "))

#     if 0 <= index < len(expenses):
#         exp = expenses[index]
#         exp.amount = float(input("New amount: "))
#         exp.category = input("New category: ")
#         exp.date = input("New date (YYYY-MM-DD): ")
#         exp.description = input("New description: ")

#         save_expenses(expenses)
#         print("✅ Expense updated")
#     else:
#         print("❌ Invalid index")


# def show_menu():
#     print("\n--- Personal Finance Manager ---")
#     print("1. Add Expense")
#     print("2. View Expenses")
#     print("3. Update Expense")
#     print("4. Delete Expense")
#     print("5. Category Report")
#     print("6. Monthly Report")
#     print("7. Exit")








# from expense import Expense
# from utils import validate_amount, validate_date
# from file_manager import save_expenses, backup_data, restore_data
# from reports import show_summary

# # def menu():
# #     print("""
# # ==== PERSONAL FINANCE MANAGER ====
# # 1. Add Expense
# # 2. View Expenses
# # 3. View Summary
# # 4. Backup Data
# # 5. Restore Data
# # 6. Exit
# # """)

# def add_expense(expenses):
#     amt = validate_amount(input("Amount: "))
#     if amt is None:
#         return

#     category = input("Category: ").strip()
#     date = validate_date(input("Date (YYYY-MM-DD): "))
#     if date is None:
#         return

#     desc = input("Description: ")

#     expenses.append(Expense(amt, category, date, desc))
#     save_expenses(expenses)
#     print("✅ Expense added")

# def view_expenses(expenses):
#     for i, e in enumerate(expenses, start=1):
#         print(f"{i}. ₹{e.amount} | {e.category} | {e.date} | {e.description}")






# from charts import category_bar_chart, monthly_line_chart
# def show_menu():
#     print("""
# =============================
#  PERSONAL FINANCE MANAGER
# =============================
# 1. Add Expense
# 2. View Expenses
# 3. View Report
# 4. update expense 
# 5. delete expense
# 6. category report
# 7. monthly report      
# 8. Backup Data
# 9. Restore Data
# 10. View Charts
# 11. Exit
# """)









def show_menu():
    print("""
1. Add Expense
2. View Expenses
3. Generate Report
4. Backup Data
5. Restore Data
6. View Charts
7. Exit
""")
