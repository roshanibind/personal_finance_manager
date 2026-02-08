# def is_valid_date(date):
#     return len(date) == 10 and date.count("-") == 2


# def validate_date(date):
#     if len(date) != 10:
#         return False
#     if date[4] != "-" or date[7] != "-":
#         return False
#     return True





# from datetime import datetime

# def validate_amount(amount):
#     try:
#         amount = float(amount)
#         if amount <= 0:
#             raise ValueError
#         return amount
#     except ValueError:
#         print("Amount must be a positive number")
#         return None

# def validate_date(date_str):
#     try:
#         datetime.strptime(date_str, "%Y-%m-%d")
#         return date_str
#     except ValueError:
#         print("Date must be YYYY-MM-DD")
#         return None








from datetime import datetime

MONTHLY_BUDGET = 20000  # You can change this

def validate_amount(amount):
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError
        return amount
    except ValueError:
        print("❌ Enter a valid positive amount")
        return None

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        print("❌ Date format must be YYYY-MM-DD")
        return None

def check_budget(expenses):
    total = sum(e.amount for e in expenses)
    if total > MONTHLY_BUDGET:
        print(f"⚠️ Budget exceeded! Limit ₹{MONTHLY_BUDGET}, Spent ₹{total}")
