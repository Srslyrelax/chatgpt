import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# User input
credit_limit = 7554.34
num_transactions = 30
min_amount = 10
max_amount = 150
amazon_amount = 500
amazon_frequency = 5
start_date = datetime.strptime('2023-03-16', '%Y-%m-%d')

# Create a date range based on the number of transactions
dates = pd.date_range(start_date, periods=num_transactions, freq='D')

# Create a DataFrame with the dates
df = pd.DataFrame({'Date': dates})

# Initialize the balance to the credit limit
balance = credit_limit

# Generate random transaction amounts
df['Amount'] = np.random.randint(min_amount, max_amount+1, size=num_transactions)

# Add Amazon transactions at specified frequency
for i in range(num_transactions):
    if i % amazon_frequency == 0:
        df.loc[i, 'Amount'] = amazon_amount
        df.loc[i, 'Place'] = 'Amazon'

# Calculate the debits and credits based on the transaction amounts
df['Debit'] = np.where(df['Place']=='Amazon', 0, df['Amount'])
df['Credit'] = np.where(df['Place']=='Amazon', df['Amount'], 0)

# Calculate the balance after each transaction
df['Balance'] = balance - df['Debit'].cumsum() + df['Credit'].cumsum()

# Format the columns as needed
df['Amount'] = df['Amount'].apply(lambda x: f'${x:,.2f}')
df['Debit'] = df['Debit'].apply(lambda x: f'${x:,.2f}' if x > 0 else '')
df['Credit'] = df['Credit'].apply(lambda x: f'${x:,.2f}' if x > 0 else '')
df['Balance'] = df['Balance'].apply(lambda x: f'${x:,.2f}')

# Print the resulting DataFrame
print(df)
