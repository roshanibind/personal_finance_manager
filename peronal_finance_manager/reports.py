# def show_all_expenses(expenses):
#     print("\n--- Expense Report ---")
#     for exp in expenses:
#         print(exp)







# from collections import defaultdict


# def category_report(expenses):
#     summary = defaultdict(float)

#     for exp in expenses:
#         summary[exp.category] += exp.amount

#     print("\n--- Category-wise Report ---")
#     for cat, total in summary.items():
#         print(f"{cat}: ₹{total}")


# def monthly_report(expenses):
#     summary = defaultdict(float)

#     for exp in expenses:
#         month = exp.date[:7]
#         summary[month] += exp.amount

#     print("\n--- Monthly Report ---")
#     for month, total in summary.items():
#         print(f"{month}: ₹{total}")







# from collections import defaultdict

# def show_summary(expenses):
#     if not expenses:
#         print("No expenses found")
#         return

#     total = sum(e.amount for e in expenses)
#     avg = total / len(expenses)

#     category_totals = defaultdict(float)
#     for e in expenses:
#         category_totals[e.category] += e.amount

#     print("\n📊 SUMMARY REPORT")
#     print(f"Total Expenses: ₹{total:.2f}")
#     print(f"Average Expense: ₹{avg:.2f}")
#     print("\nCategory-wise:")
#     for cat, amt in category_totals.items():
#         print(f"{cat}: ₹{amt:.2f}")
# from collections import defaultdict

# def show_report(expenses):
#     if not expenses:
#         print("❌ No expenses available.")
#         return

#     total = sum(e.amount for e in expenses)
#     average = total / len(expenses)

#     category_totals = defaultdict(float)
#     for e in expenses:
#         category_totals[e.category] += e.amount

#     print("\n📊 EXPENSE REPORT")
#     print(f"Total Expenses: ₹{total:.2f}")
#     print(f"Average Expense: ₹{average:.2f}")
#     print("\nCategory-wise Expenses:")
#     for cat, amt in category_totals.items():
#         print(f"{cat}: ₹{amt:.2f}")









from collections import defaultdict

def generate_report(expenses):
    summary = defaultdict(float)
    for e in expenses:
        summary[e.category] += e.amount

    total = sum(summary.values())
    avg = total / len(expenses) if expenses else 0

    print("\n📊 REPORT")
    print(f"Total: ₹{total}")
    print(f"Average: ₹{avg:.2f}")
    for cat, amt in summary.items():
        print(f"{cat}: ₹{amt}")

    return summary
