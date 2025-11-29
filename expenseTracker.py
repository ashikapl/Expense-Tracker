from models.user import User
from models.expense import Expense

# ---- Controller ----
class ExpenseTracker:
    # map of username and user(name, username)
    # map of username and []expense(category, amount)
    # add user, remove user
    # add exp, remove exp
    users = {}
    expenses = {}


    def add_user(self, name, username):
        if username not in self.users:
            user = User(name, username)
            self.users[username] = user
            print(self.users)
        else:
            print("User Already Exists!")
        

    def remove_user(self, username):
        if username in self.users:
            print("Removed user- ",self.users.pop(username))
        else:
            print("User Not Found!")


    def add_expense(self, username, category, amount):
        if username not in self.users:
            print("User not found!")
            return

        expense = Expense()

        if username not in self.expenses:
            self.expenses[username] = []

        expense.set_expense(category, amount)
        self.expenses[username].extend(expense.expenses)


    def get_expense(self, username):
        if username in self.expenses:
            # print(self.expenses)
            for i, val in enumerate(self.expenses[username]):
                print(i+1, val)
        else:
            print("User Not Found!")


    def remove_expense(self, username, index):
        if username in self.expenses:
            # for i, val in enumerate(self.expenses[username]):
            #     print(i+1, val)
            for i, tup in enumerate(self.expenses[username]):
                print(i+1, tup, index)
                if i+1 == index:
                    print(tup)
                    self.expenses[username].remove(tup)
                    break
        else:
            print("User Not Found!")


    def total_expenses_value(self, username):
        res = 0
        if username in self.expenses:
            for tup in self.expenses[username]:
                res += tup[1]
            return res
        else:
            print("User Not Found!")
    

    def total_category_based_value(self, username, category):
        if username in self.expenses:
            res = 0
            for tup in self.expenses[username]:
                if tup[0].lower() == category.lower():
                    res += tup[1]
            return res
        else:
            print("User Not Found!")
