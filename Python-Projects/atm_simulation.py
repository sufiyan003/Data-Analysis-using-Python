"""
Project: Simple ATM Simulation
Goal: To practice basic Python control flow (if-else statements), 
      variable manipulation, and user input handling.
"""

balance = 1000
pin = "1234"

user_pin = input("Enter your PIN: ")
if user_pin == pin:
    print("1. Check Balance\n2. Withdraw Money")
    choice = input("Select option: ")
    if choice == "1":
        print(f"Your balance is: ${balance}")
    elif choice == "2":
        amount = int(input("Enter amount: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrawal successful! New balance: ${balance}")
        else:
            print("Insufficient funds!")
else:
    print("Incorrect PIN!")