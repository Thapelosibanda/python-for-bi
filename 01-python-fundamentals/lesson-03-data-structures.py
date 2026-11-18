# ============================================================
# Lesson 03 — Python Data Structures
# ============================================================
# Purpose:
# This script demonstrates how I organise related information using
# lists, tuples, dictionaries and sets. It also combines data structures
# to represent customer and transaction records and introduces a
# conversion of transaction records into a Pandas DataFrame.


# ------------------------------------------------------------
# 1. Lists
# ------------------------------------------------------------
# A list stores an ordered collection of items and is mutable, which
# means its contents can be changed after the list has been created.
# Square brackets [] are used to create a list.
products = ["Laptop", "Keyboard", "Mouse", "Monitor", "Printer"]

print(products)

# List indexing starts at 0, so index 0 refers to the first item.
print(products[0])
print(products[2])
print(products[4])

# Negative indexes count backwards from the end of the list.
# -1 refers to the last item; -2 refers to the second-last item.
print(products[-1])
print(products[-2])

# append() adds an item at the end. insert() adds an item at a chosen
# position. remove() removes the first matching item from the list.
products = ["Laptop", "Keyboard", "Mouse", "Monitor"]
products.append("Printer")
products.insert(1, "USB Cable")
products.remove("Printer")

# remove() changes the list and returns None, so I call it separately.
print(products)

# len() counts the items. Slicing [start:stop] returns a section of a list;
# the stop index is excluded from the returned section.
print("Number of products:", len(products))
print("First two products:", products[:2])


# ------------------------------------------------------------
# 2. Tuples
# ------------------------------------------------------------
# A tuple is ordered like a list, but immutable: its existing items
# cannot be reassigned after it has been created. Parentheses () are
# commonly used to define a tuple.
sales_record = ("INV001", "Laptop", 5, 12500.00)

print(sales_record)
print(sales_record[0])  # First value: invoice or record ID.
print(sales_record[1])  # Second value: product name.

# The following assignment would raise a TypeError because tuple items
# cannot be reassigned. It remains commented out so this script runs.
# sales_record[0] = "INV002"


# ------------------------------------------------------------
# 3. Dictionaries
# ------------------------------------------------------------
# A dictionary stores information as key-value pairs. Curly braces {}
# define a dictionary, and each key identifies its corresponding value.
employee = {
    "employee_id": 101,
    "name": "Thabo",
    "department": "Data Analytics",
    "salary": 18500.50,
    "is_permanent": True
}

print(employee)

# A value can be accessed using its key inside square brackets.
print(employee["name"])
print(employee["salary"])

# get() retrieves a value. If a key is missing, it can return a default
# value instead of raising a KeyError.
print(employee.get("department"))
print(employee.get("location", "Not specified"))

# Assigning to an existing key updates its value. Assigning to a new key
# adds another key-value pair to the dictionary.
employee["salary"] = 20000.00
employee["location"] = "Johannesburg"

print(employee)

# These dictionary methods provide access to keys, values, or key-value pairs.
print(employee.keys())
print(employee.values())
print(employee.items())

# A dictionary can represent a business record, such as a customer.
customer = {
    "customer_id": 1001,
    "customer_name": "John",
    "city": "Johannesburg",
    "total_orders": 12
}

print(customer)


# ------------------------------------------------------------
# 4. Sets
# ------------------------------------------------------------
# A set stores unique values. Duplicate values are removed automatically.
# Sets are unordered, so I should not rely on a particular item position
# or display order.
cities = {"Johannesburg", "Cape Town", "Durban", "Johannesburg"}

print(cities)

# add() inserts a value. discard() removes a value if present and does
# not raise an error when the value is absent.
cities.add("Pretoria")
cities.discard("Durban")

print(cities)

# intersection() returns values found in both sets.
# union() combines sets and keeps unique values.
# difference() returns values found in the first set but not the second.
department_a = {"Thabo", "John", "Sarah"}
department_b = {"Sarah", "Peter", "John"}

print("Common employees:", department_a.intersection(department_b))
print("All unique employees:", department_a.union(department_b))
print("Only in department A:", department_a.difference(department_b))


# ------------------------------------------------------------
# 5. Combining data structures
# ------------------------------------------------------------
# A list can contain several dictionaries. The list represents a group
# of customers, while each dictionary represents one customer record.
customers = [
    {
        "customer_id": 1001,
        "name": "Thabo",
        "city": "Johannesburg",
        "total_spent": 15000.00
    },
    {
        "customer_id": 1002,
        "name": "Sarah",
        "city": "Cape Town",
        "total_spent": 22000.00
    },
    {
        "customer_id": 1003,
        "name": "John",
        "city": "Durban",
        "total_spent": 8500.00
    }
]

# The first list item is a dictionary. A second set of square brackets
# accesses a field inside that customer's dictionary.
print(customers[0])
print(customers[0]["name"])

# A for loop processes each customer dictionary in the customers list.
# During each repetition, customer refers to the current record.
for customer in customers:
    print(customer["name"])

# A running total starts at zero. += adds each customer's spending to
# the existing total and stores the updated value back in the variable.
total_spending = 0

for customer in customers:
    total_spending += customer["total_spent"]

print("Total spending:", total_spending)


# ------------------------------------------------------------
# 6. Exercise 1 — Product catalogue
# ------------------------------------------------------------
# QUESTION:
# Create a list containing Laptop, Keyboard, Mouse, Monitor and Printer.
# Display the full list, the first item and the last item. Remove Mouse,
# then display the updated list, the number of remaining products, and
# the first three products using list slicing.
#
# MY SOLUTION:
product_list = ["Laptop", "Keyboard", "Mouse", "Monitor", "Printer"]

print(product_list)
print(product_list[0])
print(product_list[-1])

product_list.remove("Mouse")

print("Updated catalogue:", product_list)
print("Number of products:", len(product_list))
print("First three products:", product_list[:3])


# ------------------------------------------------------------
# 7. Exercise 2 — Sales analysis
# ------------------------------------------------------------
# QUESTION:
# Use the daily sales figures below to calculate total sales, average
# daily sales, the highest sales figure, the lowest sales figure, and
# the number of days recorded.
#
# MY SOLUTION:
daily_sales = [1500, 2300, 1800, 950, 3200, 2750, 4100]

print("Total sales:", sum(daily_sales))

# / calculates the average and can return a decimal value. // performs
# floor division and would discard the fractional part of the result.
print("Average daily sales:", sum(daily_sales) / len(daily_sales))
print("Highest sales figure:", max(daily_sales))
print("Lowest sales figure:", min(daily_sales))
print("Number of days recorded:", len(daily_sales))


# ------------------------------------------------------------
# 8. Exercise 3 — Customer information
# ------------------------------------------------------------
# QUESTION:
# Create a dictionary containing a customer ID, name, city, total spent
# and active status. Display the customer's name and total spending.
# Update the city to Pretoria, add an email address, and use items() to
# display every key and its corresponding value.
#
# MY SOLUTION:
customer_dict = {
    "customer_id": 1001,
    "name": "Thabo",
    "city": "Johannesburg",
    "total_spent": 18500.75,
    "is_active": True
}

print("Customer name:", customer_dict["name"])
print("Total spending:", customer_dict["total_spent"])

customer_dict["city"] = "Pretoria"              # Update an existing key.
customer_dict["email"] = "thabo@example.com"   # Add a new key-value pair.

# items() provides each key and its corresponding value for the loop.
for key, value in customer_dict.items():
    print(key, ":", value)


# ------------------------------------------------------------
# 9. Exercise 4 — Data quality check with sets
# ------------------------------------------------------------
# QUESTION:
# Convert the customer city list into a set to remove duplicate city
# names. Display the unique cities and their count. Add Bloemfontein to
# the set, then check whether Pretoria is present.
#
# MY SOLUTION:
customer_cities = [
    "Johannesburg",
    "Cape Town",
    "Durban",
    "Johannesburg",
    "Pretoria",
    "Cape Town",
    "Durban"
]

customer_set = set(customer_cities)

print("Unique cities:", customer_set)
print("Number of unique cities:", len(customer_set))

customer_set.add("Bloemfontein")

print("Updated unique cities:", customer_set)

# The in operator checks whether a value is present in the set.
print("Is Pretoria present?", "Pretoria" in customer_set)


# ------------------------------------------------------------
# 10. Exercise 5 — Mini data engineering challenge
# ------------------------------------------------------------
# QUESTION:
# Use a list of transaction dictionaries. Each transaction contains an
# ID, product, quantity and unit price. Calculate the value of each
# transaction by multiplying quantity by unit price. Display the ID,
# product and transaction value for each record, then calculate and
# display the total sales across all transactions.
#
# MY SOLUTION:
transactions = [
    {
        "transaction_id": 1001,
        "product": "Laptop",
        "quantity": 2,
        "unit_price": 12500.00
    },
    {
        "transaction_id": 1002,
        "product": "Keyboard",
        "quantity": 5,
        "unit_price": 450.00
    },
    {
        "transaction_id": 1003,
        "product": "Monitor",
        "quantity": 3,
        "unit_price": 3200.00
    }
]

# Start the overall sales total at zero. Each transaction value is
# calculated separately before it is added to the running total.
total_sales = 0

for record in transactions:
    # Transaction value = quantity purchased multiplied by unit price.
    transaction_value = record["quantity"] * record["unit_price"]

    # Display the key details and calculated value for this record.
    print("Transaction ID:", record["transaction_id"])
    print("Product:", record["product"])
    print("Transaction value:", transaction_value)

    # Add this transaction's value to the overall sales total.
    total_sales += transaction_value

print("Total sales:", total_sales)


# ------------------------------------------------------------
# 11. Converting transaction records into a Pandas DataFrame
# ------------------------------------------------------------
# A DataFrame is a tabular data structure made up of rows and columns.
# pandas converts a list of dictionaries into a DataFrame: each
# dictionary becomes a row, and its keys become the column names.
import pandas as pd

df = pd.DataFrame(transactions)

# This calculated column contains the transaction value for each row.
df["transaction_value"] = df["quantity"] * df["unit_price"]

print(df)
