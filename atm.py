class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 0
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
        else:
            print("Insufficient funds!")

    def transfer(self, amount, recipient):
        if amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to {recipient.user_id}")
            recipient.transaction_history.append(f"Received ${amount} from {self.user_id}")
        else:
            print("Insufficient funds!")

    def show_transaction_history(self):
        for transaction in self.transaction_history:
            print(transaction)


class ATM:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, pin):
        if user_id not in self.users:
            self.users[user_id] = User(user_id, pin)
            print("User added successfully!")
        else:
            print("User already exists!")

    def authenticate_user(self, user_id, pin):
        if user_id in self.users:
            if self.users[user_id].pin == pin:
                return True
            else:
                print("Incorrect PIN!")
        else:
            print("User not found!")
        return False

    def start(self):
        user_id = input("Enter your user ID: ")
        pin = input("Enter your PIN: ")

        if self.authenticate_user(user_id, pin):
            user = self.users[user_id]
            while True:
                print("\n1. View Transaction History")
                print("2. Withdraw")
                print("3. Deposit")
                print("4. Transfer")
                print("5. Quit")

                choice = input("Enter your choice: ")

                if choice == "1":
                    user.show_transaction_history()
                elif choice == "2":
                    amount = float(input("Enter amount to withdraw: "))
                    user.withdraw(amount)
                elif choice == "3":
                    amount = float(input("Enter amount to deposit: "))
                    user.deposit(amount)
                elif choice == "4":
                    recipient_id = input("Enter recipient's user ID: ")
                    if recipient_id in self.users:
                        amount = float(input("Enter amount to transfer: "))
                        recipient = self.users[recipient_id]
                        user.transfer(amount, recipient)
                    else:
                        print("Recipient not found!")
                elif choice == "5":
                    print("Thank you for using the ATM!")
                    break
                else:
                    print("Invalid choice!")


# Usage example:
atm = ATM()
atm.add_user("123456", "7890")  # Add a user
atm.start()  # Start the ATM
