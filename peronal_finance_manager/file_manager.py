# import csv
# import os

# DATA_DIR = "data"
# DATA_FILE = os.path.join(DATA_DIR, "expenses.csv")


# def save_expenses(expenses):
#     # Create data folder if it does not exist
#     if not os.path.exists(DATA_DIR):
#         os.makedirs(DATA_DIR)

#     with open(DATA_FILE, "w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow(["Amount", "Category", "Date", "Description"])

#         for exp in expenses:
#             writer.writerow([exp.amount, exp.category, exp.date, exp.description])


# def load_expenses():
#     expenses = []

#     if not os.path.exists(DATA_FILE):
#         return expenses

#     with open(DATA_FILE, "r") as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             expenses.append(row)

#     return expenses






# import csv
# import os
# from expense import Expense

# DATA_DIR = "data"
# DATA_FILE = os.path.join(DATA_DIR, "expenses.csv")


# def ensure_data_file():
#     if not os.path.exists(DATA_DIR):
#         os.makedirs(DATA_DIR)

#     if not os.path.exists(DATA_FILE):
#         with open(DATA_FILE, "w", newline="") as file:
#             writer = csv.writer(file)
#             writer.writerow(["amount", "category", "date", "description"])


# def load_expenses():
#     ensure_data_file()
#     expenses = []

#     with open(DATA_FILE, "r") as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             expenses.append(
#                 Expense(
#                     float(row["amount"]),
#                     row["category"],
#                     row["date"],
#                     row["description"]
#                 )
#             )
#     return expenses


# def save_expenses(expenses):
#     ensure_data_file()

#     with open(DATA_FILE, "w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow(["amount", "category", "date", "description"])

#         for exp in expenses:
#             writer.writerow(
#                 [exp.amount, exp.category, exp.date, exp.description]
#             )






# import csv
# import os
# import shutil
# from expense import Expense

# DATA_FILE = "data/expenses.csv"
# BACKUP_FILE = "backups/expenses_backup.csv"

# def ensure_folders():
#     os.makedirs("data", exist_ok=True)
#     os.makedirs("backups", exist_ok=True)

# def load_expenses():
#     ensure_folders()
#     expenses = []
#     if not os.path.exists(DATA_FILE):
#         return expenses

#     with open(DATA_FILE, "r", newline="") as file:
#         reader = csv.reader(file)
#         for row in reader:
#             expenses.append(Expense(*row))
#     return expenses

# def save_expenses(expenses):
#     ensure_folders()
#     with open(DATA_FILE, "w", newline="") as file:
#         writer = csv.writer(file)
#         for exp in expenses:
#             writer.writerow(exp.to_list())

# def backup_data():
#     ensure_folders()
#     shutil.copy(DATA_FILE, BACKUP_FILE)
#     print("✅ Backup created")

# def restore_data():
#     ensure_folders()
#     shutil.copy(BACKUP_FILE, DATA_FILE)
#     print("✅ Data restored from backup")








import csv, os, shutil
from expense import Expense

DATA_FILE = "data/expenses.csv"
BACKUP_FILE = "backups/expenses_backup.csv"
EXPORT_FILE = "exports/summary_report.csv"

def ensure_dirs():
    os.makedirs("data", exist_ok=True)
    os.makedirs("backups", exist_ok=True)
    os.makedirs("exports", exist_ok=True)

def load_expenses():
    ensure_dirs()
    expenses = []
    if not os.path.exists(DATA_FILE):
        return expenses

    with open(DATA_FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            expenses.append(Expense(*row))
    return expenses

def save_expenses(expenses):
    ensure_dirs()
    with open(DATA_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        for e in expenses:
            writer.writerow(e.to_list())

def backup_data():
    ensure_dirs()
    if os.path.exists(DATA_FILE):
        shutil.copy(DATA_FILE, BACKUP_FILE)
        print("✅ Backup created")

def restore_data():
    ensure_dirs()
    if os.path.exists(BACKUP_FILE):
        shutil.copy(BACKUP_FILE, DATA_FILE)
        print("✅ Data restored")

def export_summary(summary):
    ensure_dirs()
    with open(EXPORT_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Category", "Amount"])
        for k, v in summary.items():
            writer.writerow([k, v])
    print("✅ Summary exported")
