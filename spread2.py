import random
from datetime import datetime, timedelta

# Specify the starting balance, starting date, and number of transactions
balance = 8000.0
start_date = datetime(2023, 3, 16)
num_transactions = 50

# Generate a list of dates for the specified number of transactions starting from the starting date
date_list = [start_date + timedelta(days=x) for x in range(num_transactions)]

# Generate a list of Amazon purchase amounts for the specified number of transactions
amazon_amounts = [random.randint(500, 700) for _ in range(num_transactions)]

# Generate a list of random amounts for the specified number of transactions
amount_list = [round(random.uniform(10, 200), 2) for _ in range(num_transactions)]

# Generate a list of locations for the specified number of transactions
location_list = ['' for _ in range(num_transactions)]

# Create a list to store the transaction data
transaction_data = []

# Loop through the transactions and update the balance accordingly
for i in range(num_transactions):
    balance -= amount_list[i]
    if amazon_amounts[i]:
        balance -= amazon_amounts[i]
        location_list[i] = 'Amazon'
    transaction_data.append([date_list[i].strftime('%Y-%m-%d'), 
                             '${:,.2f}'.format(amount_list[i]), 
                             location_list[i], 
                             '${:,.2f}'.format(amount_list[i] + amazon_amounts[i]), 
                             '', 
                             '${:,.2f}'.format(balance)])
    
# Print the transaction data
for data in transaction_data:
    print('\t'.join(data))
