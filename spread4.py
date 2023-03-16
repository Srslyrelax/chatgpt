import random
import datetime

# Define a list of places
places = ["Amazon", "Walmart", "Target", "Costco", "Best Buy"]

# Define the starting date and credit amount
start_date = datetime.date(2023, 3, 1)
credit = 1000.00

# Initialize the balance
balance = credit

# Loop through 31 days
for i in range(31):

    # Add 2 days for every $1000 spent
    delta = datetime.timedelta(days=int(balance // 1000) * 2)

    # Increment the date
    date = start_date + datetime.timedelta(days=i) + delta

    # Generate a list of places for the day
    day_places = random.sample(places, random.randint(1, len(places)))

    # Generate debits between $10 and $150, with occasional debits between $500 and $1000 for Amazon
    for place in day_places:
        if place == "Amazon":
            if random.random() < 0.1:
                amount = round(random.uniform(500, 1000), 2)
            else:
                amount = round(random.uniform(10, 150), 2)
        else:
            amount = round(random.uniform(10, 150), 2)

        # Print the transaction
        print(date.strftime("%Y-%m-%d"), "${:.2f}".format(amount), place)

        # Update the balance
        balance -= amount
