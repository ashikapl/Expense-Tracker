from expenseTracker.expenseTracker import ExpenseTracker
from models.category import Category

# ---- CLI App------
def main():
    expenseTracker = ExpenseTracker()

    while True:
        print()
        print("----Expense Tracker----")
        print()
        print("1. Add User")
        print("2. Remove User")
        print("3. Add Expense")
        print("4. View Expense")
        print("5. Total Expense Value")
        print("6. Total Value Based On Category")
        print("7. Remove Expense")
        print("8. Exit")
        print()
        choice = int(input("Enter your choice: "))
        print()

        match choice:
            case 1:
                name = input("Enter your name: ")
                username = input("Enter username: ")
                expenseTracker.add_user(name, username)
            case 2:
                username = input("Enter username:")
                expenseTracker.remove_user(username)
            case 3:
                username = input("Enter username:")
                if username in expenseTracker.users:
                    print("Categories")
                    print(Category.Food.value, Category.Food.name)
                    print(Category.Clothes.value, Category.Clothes.name)
                    print(Category.Health.value, Category.Health.name)
                    category = int(input("Enter the Category No: "))
                    amount = float(input("Enter Amount: "))
                    # print(username)

                    match category:
                        case 1:
                            expenseTracker.add_expense(username, Category.Food.name, amount)
                        case 2:
                            expenseTracker.add_expense(username, Category.Clothes.name, amount)
                        case 3:
                            expenseTracker.add_expense(username, Category.Health.name, amount)
                        case _:
                            print("Invalid Category!")
                else:
                    print("User Not Found!")
            case 4:
                username = input("Enter username: ")
                expenseTracker.get_expense(username)
            case 5:
                username = input("Enter username: ")
                print("Total Expenses Value:- ", expenseTracker.total_expenses_value(username))
            case 6:
                username = input("Enter username: ")
                category = input("Enter category name: ")
                print(f"Total Value Based On Category {category}:- ", expenseTracker.total_category_based_value(username, category))
            case 7: 
                username = input("Enter username:")
                index = int(input("Enter Index No: "))
                if username in expenseTracker.users:
                    expenseTracker.remove_expense(username, index)
                else:
                    print("User Not Found!")
            case 8:
                print("Exiting ExpenseTracker, Goodbye!")
            case _:
                print("Invalid Choice!")


if __name__ == "__main__":
    main()
    
                    



                    
    
    