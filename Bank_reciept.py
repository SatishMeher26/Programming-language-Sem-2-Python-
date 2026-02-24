import datetime
import random
import sys

class BankAccount:
    def __init__(self, name, account_number, balance=0.0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.bank_name = "MY BANK"

    def deposit(self, amount):
        if amount <= 0:
            print("\n[!] Deposit amount must be greater than zero.")
            return
        
        self.balance += amount
        self.print_receipt("DEPOSIT", amount)

    def withdraw(self, amount):
        if amount <= 0:
            print("\n[!] Withdrawal amount must be greater than zero.")
            return
        
        if amount > self.balance:
            print(f"\n[!] Insufficient balance. Available: ${self.balance:,.2f}")
            return
        
        self.balance -= amount
        self.print_receipt("WITHDRAWAL", amount)

    def print_receipt(self, transaction_type, amount):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaction_id = f"TXN-{random.randint(10000, 99999)}"
        masked_account = f"*****{str(self.account_number)[-4:]}"

        print("\n" + "=" * 40)
        print(f"{self.bank_name:^40}")
        print("=" * 40)
        print(f"Date/Time:      {current_time}")
        print(f"Transaction ID: {transaction_id}")
        print(f"Customer:       {self.name}")
        print(f"Account No:     {masked_account}")
        print("-" * 40)
        print(f"Type:           {transaction_type}")
        print(f"Amount:         ${amount:,.2f}")
        print("-" * 40)
        print(f"TOTAL BALANCE:  ${self.balance:,.2f}")
        print("=" * 40)
        print(f"{'Thank you for banking with us!':^40}")
        print("=" * 40 + "\n")


def main():
    print("--- Welcome to My Bank ---")
    
    user_name = input("Enter Account Holder Name: ")
    account_number = random.randint(1000000000, 9999999999)
    
    print("Your Account Number:", account_number)

    account = BankAccount(user_name, account_number, 1000.00)

    while True:
        print("\nChoose an option:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        try:
            if choice == '1':
                amount = float(input("Enter deposit amount: $"))
                account.deposit(amount)

            elif choice == '2':
                amount = float(input("Enter withdrawal amount: $"))
                account.withdraw(amount)

            elif choice == '3':
                print(f"\n[=] Available Balance: ${account.balance:,.2f}")

            elif choice == '4':
                print("Thank you for using My Bank!")
                sys.exit()

            else:
                print("\n[!] Invalid choice. Try again.")

        except ValueError:
            print("\n[!] Please enter a valid number.")


if __name__ == "__main__":
    main()