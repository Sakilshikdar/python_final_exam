from random import randint
###################################################
# ADMIN PASSWORD: admin
# #################################################


class Account:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.loan_taken = 0
        self.account_number = randint(100, 10000)
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded. Insufficient balance.")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew: {amount}")

    def check_balance(self):
        print(f"Available balance: {self.balance}")

    def check_transactions(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)

    def take_loan(self, amount):
        if self.loan_taken < 2:
            self.balance += amount
            self.loan_taken += 1
            self.transactions.append(f"Loan taken: {amount}")
        else:
            print("You have already taken the maximum allowed number of loans.")

    def transfer(self, recipient, amount):
        if recipient:
            if self.balance >= amount:
                self.balance -= amount
                recipient.balance += amount
                self.transactions.append(
                    f"Transferred: {amount} to Account {recipient.account_number}")
            else:
                print("Insufficient balance for transfer.")
        else:
            print("Account does not exist. Transfer failed.")


class Admin:
    def __init__(self):
        self.user_accounts = []

    def create_account(self, name, email, address, account_type):
        new_account = Account(name, email, address, account_type)
        self.user_accounts.append(new_account)
        print(
            f"Account created with Account Number: {new_account.account_number}")

    def delete_account(self, account_number):
        for account in self.user_accounts:
            if account.account_number == account_number:
                self.user_accounts.remove(account)
                print(f"Account {account_number} deleted successfully.")
                return
        print("Account not found.")

    def list_accounts(self):
        print("List of User Accounts:")
        for account in self.user_accounts:
            print(
                f"Account Number: {account.account_number}, Name: {account.name}, Balance: {account.balance}, Type: {account.account_type}")

    def total_available_balance(self):
        total_balance = sum(account.balance for account in self.user_accounts)
        print(f"Total available balance in the bank: {total_balance}")

    def total_loan_amount(self):
        total_loan = sum(account.loan_taken for account in self.user_accounts)
        print(f"Total loan amount in the bank: {total_loan}")

    def toggle_loan_feature(self, status):
        Account.allow_loan = status
        print(
            f"Loan feature {'enabled' if status else 'disabled'} for the bank.")


# Main program
admin_system = Admin()

while True:
    print("\nWelcome to the Banking Management System!")
    print("1: User")
    print("2: Admin")
    print("3: Exit")
    choice = input("Enter your role: ")

    if choice == "1":
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        address = input("Enter your address: ")
        account_type = input(
            "Enter your account type (Savings/Current): ").capitalize()

        user_account = Account(name, email, address, account_type)
        admin_system.user_accounts.append(user_account)
        print(
            f"Account created with Account Number: {user_account.account_number}")

        while True:
            print("\nUser Menu:")
            print("1: Deposit")
            print("2: Withdraw")
            print("3: Check Balance")
            print("4: Check Transactions")
            print("5: Take Loan")
            print("6: Transfer Money")
            print("7: Exit")
            user_choice = input("Enter your choice: ")

            if user_choice == "1":
                amount = float(input("Enter deposit amount: "))
                user_account.deposit(amount)
            elif user_choice == "2":
                amount = float(input("Enter withdrawal amount: "))
                user_account.withdraw(amount)
            elif user_choice == "3":
                user_account.check_balance()
            elif user_choice == "4":
                user_account.check_transactions()
            elif user_choice == "5":
                if user_account.loan_taken < 2:
                    amount = float(input("Enter loan amount: "))
                    user_account.take_loan(amount)
                else:
                    print("You have already taken the maximum allowed number of loans.")
            elif user_choice == "6":
                recipient_number = int(
                    input("Enter recipient account number: "))
                amount = float(input("Enter amount to transfer: "))
                recipient_account = next(
                    (account for account in admin_system.user_accounts if account.account_number == recipient_number), None)
                user_account.transfer(recipient_account, amount)
            elif user_choice == "7":
                break
            else:
                print("Invalid choice. Please try again.")

    elif choice == "2":
        admin_password = input("Enter admin password: ")
        if admin_password == "admin":
            while True:
                print("\nAdmin Menu:")
                print("1: Create Account")
                print("2: Delete Account")
                print("3: List Accounts")
                print("4: Total Available Balance")
                print("5: Total Loan Amount")
                print("6: Toggle Loan Feature")
                print("7: Exit")
                admin_choice = input("Enter your choice: ")

                if admin_choice == "1":
                    name = input("Enter user name: ")
                    email = input("Enter user email: ")
                    address = input("Enter user address: ")
                    account_type = input(
                        "Enter account type (Savings/Current): ").capitalize()
                    admin_system.create_account(
                        name, email, address, account_type)
                elif admin_choice == "2":
                    account_number = int(
                        input("Enter account number to delete: "))
                    admin_system.delete_account(account_number)
                elif admin_choice == "3":
                    admin_system.list_accounts()
                elif admin_choice == "4":
                    admin_system.total_available_balance()
                elif admin_choice == "5":
                    admin_system.total_loan_amount()
                elif admin_choice == "6":
                    loan_status = input(
                        "Enter 1 to enable, 0 to disable loan feature: ")
                    admin_system.toggle_loan_feature(loan_status == "1")
                elif admin_choice == "7":
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Invalid password. Access denied.")

    elif choice == "3":
        break

    else:
        print("Invalid choice. Please try again.")
