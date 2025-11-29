from expenseTracker import ExpenseTracker
from models.category import Category

# ---- CLI App------
def main():
    # category = Category()
    controller = ExpenseTracker()

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
                # user.set_user(name)
                username = input("Enter username: ")
                # user.set_username(username)
                controller.add_user(name, username)
            case 2:
                # print("Name: ", user.get_user())
                username = input("Enter username:")
                # if username in controller.user_mp:
                controller.remove_user(username)
            case 3:
                username = input("Enter username:")
                if username in controller.users:
                    print("Categories")
                    print(Category.Food.value, Category.Food.name)
                    print(Category.Clothes.value, Category.Clothes.name)
                    print(Category.Health.value, Category.Health.name)
                    category = int(input("Enter the Category No: "))
                    amount = float(input("Enter Amount: "))
                    # print(username)

                    match category:
                        case 1:
                            # expense.set_expense("Food", amount)
                            controller.add_expense(username, Category.Food.name, amount)
                        case 2:
                            # expense.set_expense("Clothes", amount)
                            controller.add_expense(username, Category.Clothes.name, amount)
                        case 3:
                            # expense.set_expense("Health", amount)
                            controller.add_expense(username, Category.Health.name, amount)
                        case _:
                            print("Invalid Category!")
                else:
                    print("User Not Found!")
            case 4:
                username = input("Enter username: ")
                controller.get_expense(username)
            case 5:
                username = input("Enter username: ")
                print("Total Expenses Value:- ", controller.total_expense_value(username))
            case 6:
                username = input("Enter username: ")
                category = input("Enter category name: ")
                print(f"Total Value Based On Category {category}:- ", controller.total_category_value(username, category))
            case 7: 
                # print(expense.get_expense())
                username = input("Enter username:")
                index = int(input("Enter Index No: "))
                if username in controller.users:
                    controller.remove_expense(username, index)
                else:
                    print("User Not Found!")
            case 8:
                print("Exiting ExpenseTracker, Goodbye!")
            case _:
                print("Invalid Choice!")


if __name__ == "__main__":
    main()
    
                    



                    
    
    