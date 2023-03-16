import random
import pandas as pd
from datetime import datetime, timedelta

# Define the list of locations
locations = ["Grocery Store", "Gas Station", "Restaurant", "Department Store"]

# Set the starting date and credit amount
start_date = input("Enter starting date (YYYY-MM-DD): ")
credit_amount = float(input("Enter credit amount: "))

# Create an empty list to hold the transactions
transactions = []

# Set the initial balance
balance = credit_amount

# Set the initial date
date = datetime.strptime(start_date, '%Y-%m-%d').date()

# Loop until the balance reaches zero
while balance > 0:

    # Generate a random transaction amount between $10 and $150
    if random.randint(1, 10) == 1:
        transaction_amount = random.randint(500, 1000) # occasional Amazon purchase
    else:
        transaction_amount = random.randint(10, 150)

    # Select a random location
    location = random.choice(locations)

    # Calculate the new balance
    balance -= transaction_amount

    # Add the transaction to the list
    transactions.append({'Date': date, 'Amount': f'${transaction_amount:.2f}', 'Place': location, 'Debit': f'${transaction_amount:.2f}', 'Credit': '', 'Balance': f'${balance:.2f}'})

    # Advance the date by 2 days for every $1000 spent
    if (credit_amount - balance) % 1000 == 0:
        date += timedelta(days=2)

# Create a pandas DataFrame from the list of transactions
df = pd.DataFrame(transactions)

# Print the DataFrame
print(df)
