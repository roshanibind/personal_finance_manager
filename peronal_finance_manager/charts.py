# import matplotlib.pyplot as plt
# from collections import defaultdict
# from datetime import datetime

# def category_bar_chart(expenses):
#     if not expenses:
#         print("❌ No data available for chart.")
#         return

#     category_totals = defaultdict(float)
#     for e in expenses:
#         category_totals[e.category] += e.amount

#     categories = list(category_totals.keys())
#     amounts = list(category_totals.values())

#     plt.figure()
#     plt.bar(categories, amounts)
#     plt.title("Category-wise Expenses")
#     plt.xlabel("Category")
#     plt.ylabel("Amount (₹)")
#     plt.tight_layout()
#     plt.show()


# def monthly_line_chart(expenses):
#     if not expenses:
#         print("❌ No data available for chart.")
#         return

#     monthly_totals = defaultdict(float)

#     for e in expenses:
#         month = datetime.strptime(e.date, "%Y-%m-%d").strftime("%Y-%m")
#         monthly_totals[month] += e.amount

#     months = sorted(monthly_totals.keys())
#     amounts = [monthly_totals[m] for m in months]

#     plt.figure()
#     plt.plot(months, amounts, marker='o')
#     plt.title("Monthly Expense Trend")
#     plt.xlabel("Month")
#     plt.ylabel("Amount (₹)")
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.show()











import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime

def category_chart(expenses):
    data = defaultdict(float)
    for e in expenses:
        data[e.category] += e.amount

    plt.bar(data.keys(), data.values())
    plt.title("Category-wise Expenses")
    plt.show()

def monthly_chart(expenses):
    data = defaultdict(float)
    for e in expenses:
        month = datetime.strptime(e.date, "%Y-%m-%d").strftime("%Y-%m")
        data[month] += e.amount

    plt.plot(data.keys(), data.values(), marker="o")
    plt.title("Monthly Expenses")
    plt.show()
