# This project simulates ATM transactions using NumPy arrays.
# It manages account balances, performs deposits and withdrawals,
# and identifies accounts with low balance.

import numpy as np

balances = np.array([5000, 2500, 1000, 8000, 600])

balances += 500

withdrawals = np.array([0, 1000, 0, 1000, 0])
balances -= withdrawals

low_balance_accounts = balances < 1000

print("Updated Balances:", balances)
print("Accounts with Low Balance:", low_balance_accounts)
