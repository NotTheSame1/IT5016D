# Activity2.py
# @ Author: Norma Seym
# Date: December 2023
"""
Directions:
- Copy out the example shown in the module lesson "Tuples" and make sure that it works.
- Amend the program so that it also shows:
    - The names of all customers with less than $100
    - The names of customers with no address and no phone number
    - The highest and lowest balances
    - Then sum of balances from all customers
    - Write code that prints all the details, for all the customers.
        HINT: This will use a nested `for` statement to print each tuple
    - The full details for customers with more than $5000 or customers who are overdrawn
"""

bank_accounts = (
    ("Joe", 33, "234 Great South Road", "022629107"),
    ("Tama", 6000),
    ("Suzanne", 21025, "45 Green Lane"),
    ("Anihera", -75),
)

print("The number of bank accounts is ", len(bank_accounts))

# showing names and balances
for i in bank_accounts:
    print("\nThe name is ", i[0], " and the balance is $", i[1])

# showing only names with addresses
for i in bank_accounts:
    if len(i) > 2:
        print("\nThe name is ", i[0], " and the address is ", i[2])

    # Displays names of customers with no address or phone number
    else:
        print(f"\n{i[0]} has no address or phone number on record")

# The names of all customers with less than $100
for i in bank_accounts:
    if int(i[1]) < 100:
        print(f"\n{i[0]} has less than $100 in their account")

# Shows names of customers with no address and no phone number
for i in bank_accounts:
    if int(i[1]) > 100:
        print(i[0])
