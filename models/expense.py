# --- Expense class---
class Expense:
    def __init__(self):
        self.expenses = []
        
    def set_expense(self, category, amount):
        self.expenses.append((category, amount))
    
    def get_expense(self):
        return self.expenses

