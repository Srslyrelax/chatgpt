import random
import pandas as pd
from datetime import datetime, timedelta

# Ask the user to input the locations
locations = input("Enter locations separated by commas: ").split(',')

# Set the starting date and credit amount
start_date = input("Enter starting date (YYYY-MM-DD): ")
credit_amount = float(input("Enter credit amount: "))

# Create an empty list to hold the transactions
transactions = []

# Set the initial balance
balance = credit_amount

## Set the initial date
#date = datetime.strptime(start_date, '%Y-%m-%d').date()
#
## Loop until the balance reaches zero
#while balance > 0:
#
#    # Generate a random transaction amount between $10 and $150
#    if random.randint(1, 10) == 1:
#        transaction_amount = random.randint(500, 1000) # occasional Amazon purchase
#    else:
#        transaction_amount = round(random.uniform(10, 150), 2)
#
#    # Select a random location
#    location = random.choice(locations)
#
#    # Calculate the new balance
#    balance -= transaction_amount
#
#    # Add the transaction to the list
#    transactions.append({'Date': date, 'Amount': f'${transaction_amount:.2f}', 'Place': location, 'Debit': f'${transaction_amount:.2f}', 'Credit': '', 'Balance': f'${balance:.2f}'})
#
#    # Advance the date by 2 days for every $1000 spent
#    if (credit_amount - balance) % 1000 == 0:
#        date += timedelta(days=2)
# Set the initial date
date = datetime.strptime(start_date, '%Y-%m-%d').date()

# Set the number of days to spread the transactions over
num_days = 31

# Determine the amount to spend each day
daily_spending = round((credit_amount / num_days), 2)

# Create a dictionary to keep track of places used on a given day
places_used = {}

# Loop over each day
for i in range(num_days):
    # Reset the places used for the day
    places_used = {}

    # Loop until the daily spending limit is reached
    while daily_spending > 0:
        # Select a random location that hasn't been used yet on this day
        location = random.choice([place for place in locations if place not in places_used])

        # Generate a random transaction amount between $10 and $150
        if random.randint(1, 10) == 1:
            transaction_amount = random.randint(500, 1000)  # occasional Amazon purchase
        else:
            transaction_amount = round(random.uniform(10, min(150, daily_spending)), 2)

        # Calculate the new balance
        balance -= transaction_amount

        # Add the transaction to the list
        transactions.append({'Date': date, 'Amount': f'${transaction_amount:.2f}', 'Place': location, 'Debit': f'${transaction_amount:.2f}', 'Credit': '', 'Balance': f'${balance:.2f}'})

        # Update the places used for the day
        places_used[location] = True

        # Update the daily spending
        daily_spending -= transaction_amount

        # Advance the date by one day
        date += timedelta(days=1)

    # Reset the daily spending
    daily_spending = round((credit_amount / num_days), 2)


# Create a pandas DataFrame from the list of transactions
df = pd.DataFrame(transactions)

# Print the DataFrame
print(df)
